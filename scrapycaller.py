from os import path
from subprocess import check_output

class ScrapyCaller(object):

    scrapy_folder = 'news_scraper'
    call_string = 'scrapy crawl finance-news --nolog --output -:json'

    def __init__(self):
        self.working_dir = path.join(path.dirname(__file__), self.scrapy_folder, '')
        print(self.working_dir)

    def get_scrapy_output(self):
        return check_output(self.call_string.split(), cwd=self.working_dir).decode('unicode_escape')