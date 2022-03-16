import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By



class WebCrawlear():


    def __init__(self, url='https://www.spacemoney.com.br/ultimas-noticias') -> None:
        self.url = url
        self.driver = None
        self.data_frame_news = None

    def make_driver(self):
        option = Options()
        option.headless = True
        self.driver = webdriver.Firefox(options=option)
        self.driver.get(self.url)

    def get_elements_by_class_name(self, class_name = 'titulos'):
        list_with_xpaths = self.driver.find_elements(By.CLASS_NAME, value=class_name)
        return list_with_xpaths

    def extract_title(self,xpath):
        html_content_title = xpath.get_attribute('title')
        soup_title = BeautifulSoup(html_content_title, 'html.parser')
        return soup_title
    
    def make_data_frame_news(self):
        list_with_xpaths = self.get_elements_by_class_name('titulos')
        lista_news = []
        for xpath in list_with_xpaths:
            news = self.extract_title(xpath)
            lista_news.append(news)
        # return lista_news
        self.data_frame_news = pd.DataFrame(lista_news, columns = ['News'])
        self.driver.quit()
        return self.data_frame_news

    def make_html(self):
        table_html = self.data_frame_news.to_html()

        with open("templates/news.html") as inf:
            txt = inf.read()
            soup = BeautifulSoup(txt, 'html.parser')

        soup.table.extend(table_html)

        # soup.table.append(table_html)

        with open("templates/news.html", "w") as outf:
            outf.write(str(soup))

    def main(self):
        self.make_driver()
        dataframe_news = self.make_data_frame_news()
        # print(dataframe.values.tolist())
        return dataframe_news.values.tolist()
        # print(self.data_frame_news.to_html())
        # self.make_html()

if __name__ == "__main__":
    webscralear = WebCrawlear(url='https://www.spacemoney.com.br/ultimas-noticias')
    teste = webscralear.main()
    print(teste)