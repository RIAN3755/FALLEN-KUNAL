class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16743442
    API_HASH = "12bbd720f4097ba7713c5e40a11dfd2a"

    CASH_API_KEY = "PRPSG4AY3Q3H0QG0"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://brmhwhgf:Eq_ZuGoNei_j50ST1iGf7WMymc6IO9vf@hattie.db.elephantsql.com/brmhwhgf"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001935950378)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/bf5d0a28f445136c5372d.jpg"

    SUPPORT_CHAT = "JHBots"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5892491831:AAGV3fp5EUr4bmSnwHGxcegyGTSeVLkVBUM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "S3J6EISOC17L"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6299128233  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1045939902, 5885920877]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = [5885920877]  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
