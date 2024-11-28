
import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '25776734'))
API_HASH = environ.get('API_HASH', '9bb0c527d53d497506baf1bd17d7426c')
BOT_TOKEN = environ.get('BOT_TOKEN', '8010470950:AAEF7Itm6N8mn3JPkYsWvy12UYMQ_X_UA8s')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6617823463').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/Dev77_xD") # ADMIN USERNAME
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002037872585').split()]
MICL = environ.get('MICL', 'https://telegram.me/MrAK_LinkZzz')
BMICL = environ.get('BMICL', 'https://telegram.me/+P-oPdYbUDWIwNjI9')
BMCL = environ.get('BMCL', 'https://telegram.me/+skgCIvzceP44NTM1')
MCL = environ.get('MCL', 'https://telegram.me/+5qxYQpqg8KY2ZmY1')
MGL = environ.get('MGL', 'https://telegram.me/New_Movies_Request_Group_MrAK')
BMGL = environ.get('BMGL', 'https://telegram.me/+QAdjuRtIXf0xMDk1')
ACL = environ.get('ACL', 'https://telegram.me/addlist/YtriDZhDyVViZjY9')
BACL = environ.get('BACL', 'https://telegram.me/MrAK_AnimeZz')
AGL = environ.get('AGL', 'https://telegram.me/MrAK_AnimeZz_Tamil')
WCL = environ.get('WCL', 'https://whatsapp.com/channel/0029VaZbVwQGU3BJt3IfFr2Q')
TSCL = environ.get('TSCL', 'https://telegram.me/+4_Uq4L95R00yODll')
BMB = environ.get('BMB', 'https://telegram.me/MrAK_Movie_bot')
MRAKBOTS = environ.get('MRAKBOTS', 'https://telegram.me/MrAK_BOTS')
MYBOT = environ.get('MYBOT', 'https://telegram.me/MrAKLinkZbot')
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://niyoyoh251:XwoLRWgZL6NFWFLM@cluster0.ea1ka.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "zgsvhsu")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002158259855'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002158259855'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002158259855'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002158259855'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002036256358'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002158259855')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002158259855'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://telegram.me/MrAK_BOTS_Support_Group') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', False)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://telegram.me/HowToDownload_Tutorial_MrAK/3")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "5f14184b5d330486d0ebcb32127fdca5b03c8b42")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'publicearn.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "5f14184b5d330486d0ebcb32127fdca5b03c8b42")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'publicearn.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "5f14184b5d330486d0ebcb32127fdca5b03c8b42")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'publicearn.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "600"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["Tamil", "Tam", "Telugu", "Tel", "Kannada", "kan", "Malayalam", "Mal", "Hindi", "Hin", "English", "Eng", "Korean", "Kor", "Japanese", "Jap", "Chinese", "Chi", "Dual", "Multi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://envs.sh/TWL.jpg https://envs.sh/TWG.jpg https://envs.sh/TWK.jpg https://envs.sh/TWz.jpg https://envs.sh/TW3.jpg https://envs.sh/TWY.jpg https://envs.sh/TWC.jpg https://envs.sh/TWR.jpg https://envs.sh/TW1.jpg https://envs.sh/TW4.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://graph.org/file/f96562518138b9132abf8.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/54339913c153df35e5a54.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '3600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '10'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
