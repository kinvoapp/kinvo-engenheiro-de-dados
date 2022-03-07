from typing import Type
from src.repository.repository import save_jsons, read_jsons
from src.crawler.crawler import scrapping

class News():
    def obtain_news(self) -> None:
        self.new_infos = scrapping()
        self.create_news()

    def read_news(self) -> list:
        try:
            self.news = read_jsons()
        except ValueError:
            print("Decoding json has failed.")
        except TypeError:
            print("File must be a json.")
        else:
            return self.news['news']
    
    def create_news(self) -> None:
        try:
            save_jsons(self.new_infos)
        except Exception as e:
            print("Error: ", e)

news = News()