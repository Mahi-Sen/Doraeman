import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, CHANNELS
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp, get_readable_time
import time

lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    _, ident, chat, lst_msg_id, skip = query.data.split("#")
    if ident == 'yes':
        msg = query.message
        await msg.edit("<b>Indexing started...</b>")
        try:
            chat = int(chat)
        except:
            chat = chat
        await index_files_to_db(int(lst_msg_id), chat, msg, bot, int(skip))
    elif ident == 'cancel':
        temp.CANCEL = True
        await query.message.edit("Trying to cancel Indexing...")

@Client.on_message(filters.command('index') & filters.private & filters.incoming & filters.user(ADMINS))
async def send_for_index(bot, message):
    if lock.locked():
        return await message.reply('Wait until previous process complete.')
    i = await message.reply("Forward last message or send last message link.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await i.delete()
    if msg.text and msg.text.startswith("https://telegram.me"):
        try:
            msg_link = msg.text.split("/")
            last_msg_id = int(msg_link[-1])
            chat_id = msg_link[-2]
            if chat_id.isnumeric():
                chat_id = int(("-100" + chat_id))
        except:
            await message.reply('Invalid message link!')
            return
    elif msg.forward_from_chat and msg.forward_from_chat.type == enums.ChatType.CHANNEL:
        last_msg_id = msg.forward_from_message_id
        chat_id = msg.forward_from_chat.username or msg.forward_from_chat.id
    else:
        await message.reply('This is not forwarded message or link.')
        return
    try:
        chat = await bot.get_chat(chat_id)
    except Exception as e:
        return await message.reply(f'Errors - {e}')
    if chat.type != enums.ChatType.CHANNEL:
        return await message.reply("I can index only channels.")
    s = await message.reply("Send skip message number.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await s.delete()
    try:
        skip = int(msg.text)
    except:
        return await message.reply("Number is invalid.")
    buttons = [[
        InlineKeyboardButton('✅ ʏᴇꜱ ✅', callback_data=f'index#yes#{chat_id}#{last_msg_id}#{skip}')
    ],[
        InlineKeyboardButton('❌ ᴄᴀɴᴄᴇʟ ❌', callback_data='close_data'),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(f'Do you want to index {chat.title} channel?\nTotal Messages: <code>{last_msg_id}</code>', reply_markup=reply_markup)

@Client.on_message(filters.command('channel'))
async def channel_info(bot, message):
    if message.from_user.id not in ADMINS:
        await message.reply('<b>ᴏɴʟʏ ᴛʜᴇ ʙᴏᴛ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ... 😑</b>')
        return
    ids = CHANNELS
    if not ids:
        return await message.reply("Not set CHANNELS")
    text = '**Indexed Channels:**\n\n'
    for id in ids:
        chat = await bot.get_chat(id)
        text += f'{chat.title}\n'
    text += f'\n**Total:** {len(ids)}'
    await message.reply(text)

async def index_files_to_db(lst_msg_id, chat, msg, bot, skip):
    start_time = time.time()
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0
    current = skip
    
    async with lock:
        try:
            async for message in bot.iter_messages(chat, lst_msg_id, skip):
                time_taken = get_readable_time(time.time()-start_time)
                if temp.CANCEL:
                    temp.CANCEL = False
                    await msg.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴀɴᴄᴇʟʟᴇᴅ!\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nꜱᴀᴠᴇᴅ <code>{total_files}</code> ꜰɪʟᴇꜱ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ!\nᴅᴜᴘʟɪᴄᴀᴛᴇ ꜰɪʟᴇꜱ ꜱᴋɪᴘᴘᴇᴅ: <code>{duplicate}</code>\nᴅᴇʟᴇᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ: <code>{deleted}</code>\nɴᴏɴ-ᴍᴇᴅɪᴀ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ: <code>{no_media + unsupported}</code>\nᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ: <code>{unsupported}</code>\nᴇʀʀᴏʀꜱ ᴏᴄᴄᴜʀʀᴇᴅ: <code>{errors}</code>")
                    return
                current += 1
                if current % 100 == 0:
                    btn = [[
                        InlineKeyboardButton('❌ ᴄᴀɴᴄᴇʟ ❌', callback_data=f'index#cancel#{chat}#{lst_msg_id}#{skip}')
                    ]]
                    await msg.edit_text(text=f"ᴛᴏᴛᴀʟ ᴍᴇꜱꜱᴀɢᴇꜱ ʀᴇᴄᴇɪᴠᴇᴅ: <code>{current}</code>\nᴛᴏᴛᴀʟ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴀᴠᴇᴅ: <code>{total_files}</code>\nᴅᴜᴘʟɪᴄᴀᴛᴇ ꜰɪʟᴇꜱ ꜱᴋɪᴘᴘᴇᴅ: <code>{duplicate}</code>\nᴅᴇʟᴇᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ:  <code>{deleted}</code>\nɴᴏɴ-ᴍᴇᴅɪᴀ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ: <code>{no_media + unsupported}</code>\nᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ: <code>{unsupported}</code>\nᴇʀʀᴏʀꜱ ᴏᴄᴄᴜʀʀᴇᴅ: <code>{errors}</code>", reply_markup=InlineKeyboardMarkup(btn))
                    await asyncio.sleep(2)
                if message.empty:
                    deleted += 1
                    continue
                elif not message.media:
                    no_media += 1
                    continue
                elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
                    unsupported += 1
                    continue
                media = getattr(message, message.media.value, None)
                if not media:
                    unsupported += 1
                    continue
                elif media.mime_type not in ['video/mp4', 'video/x-matroska']:
                    unsupported += 1
                    continue
                media.caption = message.caption
                sts = await save_file(media)
                if sts == 'suc':
                    total_files += 1
                elif sts == 'dup':
                    duplicate += 1
                elif sts == 'err':
                    errors += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await msg.reply(f'❌ ɪɴᴅᴇx ᴄᴀɴᴄᴇʟᴇᴅ ᴅᴜᴇ ᴛᴏ ᴇʀʀᴏʀ - {e}')
        else:
            time_taken = get_readable_time(time.time()-start_time)
            await msg.edit(f'Succesfully saved <code>{total_files}</code> to Database!\nCompleted in {time_taken}\n\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>\nUnsupported Media: <code>{unsupported}</code>\nErrors Occurred: <code>{errors}</code>')
