import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "EAABwzLixnjYBO8DXCi8ccaV0f0ZAA4AaHpga9LNUKCIM1Wh6ELzUHGbgbNqgZAwPo3u2hZBl9W7ZBgoKc1Sb65avr5lfqR54zzQz1QKc4SWtpXCrgg7SV3Pb3REZCTeTBkdjds2rIddT5PJA3psver970QXod7ksxwZBXaihZCxP9sC6SeTkp41l46RWglgTr9KF5qZATU7GlErO")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH","")
    # Get these values from my. Facebook Messenger.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Facebook Messenger
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "https://www.facebook.com/profile.php?id=61554593814364&mibextid=kFxxJD"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER")
