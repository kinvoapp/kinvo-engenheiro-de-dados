import logging
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


class WebCrawlear():


    def __init__(self, url=None) -> None:
        spacemoney_url = 'https://www.spacemoney.com.br/ultimas-noticias'
        self.url = url or spacemoney_url
        self.driver = None
        self.data_frame_news = None
        self._make_driver(url=self.url)

    def _make_driver(self, url=None):
        """ Make firefox webdriver to be used by other methods
        """
        logging.debug("--> _make_driver")
        option = Options()
        option.headless = True
        self.driver = webdriver.Firefox(options=option)
        self.driver.get(url or self.url)
        logging.debug("<-- _make_driver")


    def _get_elements_by_class_name(self, class_name):
        """ Takes elements of a specified class
        input: str class_name
        """
        logging.debug("--> _get_elements_by_class_name")
        self.list_with_xpaths = self.driver.find_elements(
            By.CLASS_NAME, value=class_name
            )
        logging.debug("<-- _get_elements_by_class_name")

    def _extract_title(self,xpath):
        """ Extracts tag elements with a specific title tag from xpath
        """
        logging.debug("--> _extract_title")
        html_content_title = xpath.get_attribute('title')
        soup_title = BeautifulSoup(html_content_title, 'html.parser')
        logging.debug("<-- _extract_title")
        return soup_title
    
    def make_data_frame_news(self, class_name='titulos'):
        """ Create dataframe from all elements [elements list] with same class_name
        input: str class_name
        output: dataframe (save in self argument)"""
        logging.debug("--> make_data_frame_news")
        self._get_elements_by_class_name(class_name)
        lista_news = []
        for xpath in self.list_with_xpaths :
            news = self._extract_title(xpath)
            lista_news.append(news)
        self.data_frame_news = pd.DataFrame(lista_news, columns = ['News'])
        logging.info(f'dataframe maked: {self.data_frame_news}')
        self.driver.quit()
        logging.debug("<-- make_data_frame_news")
        return self.data_frame_news

    def get_list_news(self):
        """ Create news list from dataframe.   
        """
        logging.debug("--> make_data_frame_news")
        dataframe_news = self.make_data_frame_news()
        self.dataframe_list_news = dataframe_news.values.tolist()
        logging.info(f'list_news maked: {self.dataframe_list_news}')
        logging.debug("--> make_data_frame_news")
        return self.dataframe_list_news

if __name__ == "__main__":
    from load_parameter_util import AppParameterLoadUtil
    # Esta classe cria a possibilidade de setar nivel de log facilitando debug dos recursos utilizados
    # As bibliotecas utilizadadas possuem debug automatico desde que se utilize a biblioteca logging no modo debug
    app_parameter_load_util = AppParameterLoadUtil()
    CONFIG_PARAMS = app_parameter_load_util.get_dictinary(
        file_name='config_webcrawlear.cfg',
    )
    url='https://www.spacemoney.com.br/ultimas-noticias'
    webcrawlear_config = CONFIG_PARAMS.get('webcrawlear') or None
    if webcrawlear_config:
        url = webcrawlear_config['url']
    logging.info(f'url: {url}')
    try:
        webscralear = WebCrawlear(url)
        teste = webscralear.get_list_news()
    except Exception as e:
        logging.error(e)