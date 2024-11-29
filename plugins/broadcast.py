from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import users_broadcast, groups_broadcast, temp, get_readable_time
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup 

# No need for lock since you're removing it
# lock = asyncio.Lock()  # Removed

@Client.on_callback_query(filters.regex(r'^broadcast_cancel'))
async def broadcast_cancel(bot, query):
    _, ident = query.data.split("#")
    if ident == 'users':
        await query.message.edit("<b>ᴛʀʏɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴜsᴇʀs ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...</b>")
        temp.USERS_CANCEL = True
    elif ident == 'groups':
        temp.GROUPS_CANCEL = True
        await query.message.edit("<b>ᴛʀʏɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ ɢʀᴏᴜᴘs ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...</b>")

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_users(bot, message):
    # Ask admin if they want to pin the message
    is_pin = True
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    b_sts = await message.reply_text(text='<b>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ʏᴏᴜʀ ᴍᴇssᴀɢᴇs ᴛᴏ ᴜsᴇʀs ⌛️</b>')
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed = 0
    success = 0

    async for user in users:
        time_taken = get_readable_time(time.time() - start_time)
        if temp.USERS_CANCEL:
            temp.USERS_CANCEL = False
            await b_sts.edit(f"ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴀɴᴄᴇʟʟᴇᴅ !\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{total_users}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_users}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>")
            return
        sts = await users_broadcast(int(user['id']), b_msg, is_pin)
        if sts == 'Success':
            success += 1
        elif sts == 'Error':
            failed += 1
        done += 1
        if not done % 20:
            btn = [[InlineKeyboardButton('CANCEL', callback_data=f'broadcast_cancel#users')]]
            await b_sts.edit(f"ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ɪɴ ᴘʀᴏɢʀᴇꜱꜱ...\n\nᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{total_users}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_users}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>", reply_markup=InlineKeyboardMarkup(btn))

    await b_sts.edit(f"Users broadcast completed.\nCompleted in {time_taken}\n\nTotal Users: <code>{total_users}</code>\nCompleted: <code>{done} / {total_users}</code>\nSuccess: <code>{success}</code>")

@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_group(bot, message):
    # Ask admin if they want to pin the message
    is_pin = True
    chats = await db.get_all_chats()
    b_msg = message.reply_to_message
    b_sts = await message.reply_text(text='<b>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ʏᴏᴜʀ ᴍᴇssᴀɢᴇs ᴛᴏ ɢʀᴏᴜᴘs ⏳</b>')
    start_time = time.time()
    total_chats = await db.total_chat_count()
    done = 0
    failed = 0
    success = 0

    async for chat in chats:
        time_taken = get_readable_time(time.time() - start_time)
        if temp.GROUPS_CANCEL:
            temp.GROUPS_CANCEL = False
            await b_sts.edit(f"Groups broadcast Cancelled!\nCompleted in {time_taken}\n\nTotal Groups: <code>{total_chats}</code>\nCompleted: <code>{done} / {total_chats}</code>\nSuccess: <code>{success}</code>\nFailed: <code>{failed}</code>")
            return
        sts = await groups_broadcast(int(chat['id']), b_msg, is_pin)
        if sts == 'Success':
            success += 1
        elif sts == 'Error':
            failed += 1
        done += 1
        if not done % 20:
            btn = [[InlineKeyboardButton('CANCEL', callback_data=f'broadcast_cancel#groups')]]
            await b_sts.edit(f"Groups broadcast in progress...\n\nTotal Groups: <code>{total_chats}</code>\nCompleted: <code>{done} / {total_chats}</code>\nSuccess: <code>{success}</code>\nFailed: <code>{failed}</code>", reply_markup=InlineKeyboardMarkup(btn))

    await b_sts.edit(f"Groups broadcast completed.\nCompleted in {time_taken}\n\nTotal Groups: <code>{total_chats}</code>\nCompleted: <code>{done} / {total_chats}</code>\nSuccess: <code>{success}</code>\nFailed: <code>{failed}</code>")
