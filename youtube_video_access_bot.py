from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
path = "E:\Download\chromedriver.exe"
URL = "https://youtu.be/QEdhToP0bq4"

driver = webdriver.Chrome(executable_path="E:\Download\chromedriver.exe")
def youtube_bot():
    driver.get("http://reve23.github.io")

#abondend because of webdriver