import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from src.crawler.util import make_dict


drive_path = os.path.join(os.getcwd(), 'src\crawler\chromedriver.exe')

def scrapping() -> dict:
    option = Options()
    print(drive_path)
    option.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=drive_path, 
        options=option
        )
    driver.get("https://www.spacemoney.com.br/ultimas-noticias/feed/")
    time.sleep(2)
    folder_number = 2
    soup_infos = []
    for i in range(0, 5):
        item = driver.find_element(by=By.ID, value=f"folder{folder_number}").text
        soup_infos.append(BeautifulSoup(item, features="xml"))
        folder_number += 3
    driver.close()
    infos = [make_dict(info) for info in soup_infos]
    return {"news": infos}
