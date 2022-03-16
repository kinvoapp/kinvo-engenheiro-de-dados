from  selenium import webdriver
from flask import Flask, render_template
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

app = Flask(__name__)
@app.route('/')
def getNews(lnk, processed, links):

    #Define website
    #url = "https://www.spacemoney.com.br/tags/b3/"

    # Define Webdriver
    ser = Service("C:\chromedrive\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=op, service=ser)
    #Loop to browse pages
    i = 1
    lnk = []
    processed = []
    while i < 10:
        url1 = "https://www.spacemoney.com.br/ultimas-noticias/p/"
        url = url1 + str(i)
        driver.get(url)
        #Getting news links about B3 on the website
        links = driver.find_elements(By.CSS_SELECTOR, ".noticiaTexto [href*='b3']")
        for link in links:
            if link not in processed:
                link = link.get_attribute('href')
                lnk.append(link)
                processed.append(link)
            else:
                continue
        i+= 1
    return lnk

@app.route('/news')
def postNews(lnk):
    ser = Service("C:\chromedrive\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=op, service=ser)
    for url in lnk[1:]:
        driver.execute_script('window.open("{}", "_blank");'.format(url))

    return render_template("news.html", url = url)

if __name__ == '__main__':
    app.run()

