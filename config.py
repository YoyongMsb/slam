# REQUIRED CONFIG
BOT_TOKEN = "2006307738:AAFCuN2GkNDm3SVcWpuOXWSPRYay3iq0Ubs"
GDRIVE_FOLDER_ID = "0AAgKxbLSKET1Uk9PVA"
OWNER_ID = 1600128107
DOWNLOAD_DIR = "/usr/src/app/downloads"
DOWNLOAD_STATUS_UPDATE_INTERVAL = 5
AUTO_DELETE_MESSAGE_DURATION = 20
IS_TEAM_DRIVE = "true"
TELEGRAM_API = 4583787
TELEGRAM_HASH = "b87ff75eb54f6669d4d15ed40836c581"
# OPTIONAL CONFIG
DATABASE_URL = ""
AUTHORIZED_CHATS = ""  # Split by space
SUDO_USERS = ""  # Split by space
IGNORE_PENDING_REQUESTS = ""
USE_SERVICE_ACCOUNTS = ""
INDEX_URL = ""
STATUS_LIMIT = ""  # Recommend limit status to 4 tasks
UPTOBOX_TOKEN = ""
MEGA_API_KEY = ""
MEGA_EMAIL_ID = ""
MEGA_PASSWORD = ""
BLOCK_MEGA_FOLDER = "" 
BLOCK_MEGA_LINKS = ""
STOP_DUPLICATE = ""
SHORTENER = ""
SHORTENER_API = ""
# qBittorrent
IS_VPS = ""  # Don't set this to True even if VPS, unless facing error with web server
SERVER_PORT = "80"  # Only For VPS even if is_vps is false
BASE_URL_OF_BOT = ""  # Web Link, Required for Heroku to avoid sleep or use worker if you don't want to use web (selection)
# If you want to use Credentials externally from Index Links, fill these vars with the direct links
# These are optional, if you don't know, simply leave them, don't fill anything in them.
ACCOUNTS_ZIP_URL = ""
TOKEN_PICKLE_URL = ""
MULTI_SEARCH_URL = ""  # You can use gist raw link (remove commit id from the link, like config raw link check Heroku guide)
# To use limit leave space between number and unit. Available units is (gb or GB, tb or TB)
TORRENT_DIRECT_LIMIT = ""
TAR_UNZIP_LIMIT = ""
CLONE_LIMIT = ""  
MEGA_LIMIT = ""
# View Link button to open file Index Link in browser instead of direct download link
# You can figure out if it's compatible with your Index code or not, open any video from you Index and check if the END of link from browser link bar is ?a=view, if yes make it "True" it will work (Compatible with Bhadoo Index Code)
VIEW_LINK = ""
# Add more buttons (Three buttons are already added of Drive Link, Index Link, and View Link, you can add extra buttons too, these are optional)
# If you don't know what are below entries, simply leave them, Don't fill anything in them.
BUTTON_FOUR_NAME = ""
BUTTON_FOUR_URL = ""
BUTTON_FIVE_NAME = ""
BUTTON_FIVE_URL = ""
BUTTON_SIX_NAME = ""
BUTTON_SIX_URL = ""
