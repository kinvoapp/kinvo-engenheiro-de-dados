import os
import secrets


API_PREFIX = "/api/v1"

BOT_NAME = 'kinvo'

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

DEPTH_LIMIT = 10
DOWNLOAD_TIMEOUT = 540
DOWNLOAD_DELAY = 5

EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
    'scrapy.extensions.closespider.CloseSpider': 1
}

FEED_EXPORT_ENCODING = 'utf-8'
NEWSPIDER_MODULE = 'kinvo.services'
ROBOTSTXT_OBEY = True
SPIDER_MODULES = ['kinvo.services']

SECRET_KEY = secrets.token_urlsafe(16)
