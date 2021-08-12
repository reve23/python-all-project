from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "E:\Download"
url = "https://reve23.github.io/covid-tracker/"


driver = webdriver.Firefox(path)
driver.get(url)
time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")
# print(soup)