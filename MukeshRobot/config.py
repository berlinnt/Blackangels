
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "25965139" # integer value, dont use ""
    API_HASH = "ff199ecfed11f6c4a75feb165d62c9ab"
    TOKEN = "6958783493:AAGWOGrXKkI1kGhW69e7o9t0mdkMbc3Me7M"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 484576504 # If you dont know, run the bot and do /id in your private chat with it, also an integer

    MUST_JOIN = "blackangelsmusic"
    SUPPORT_CHAT = "blackangelsmusic"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph//file/0356d9684c032d44c0607.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://kansya:1234@cluster0.pz6wrfk.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = [484576504]  # List of groups that you want blacklisted.
    DRAGONS = [484576504]  # User id of sudo users
    DEV_USERS = [484576504]  # User id of dev users
    DEMONS = [484576504]  # User id of support users
    TIGERS = [484576504]  # User id of tiger users
    WOLVES = [484576504]  # User id of whitelist users

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
