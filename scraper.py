from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/")
soup = BeautifulSoup(page.content,'html.parser')
title = soup.title
print(title.text)
div = soup.div
print(div.text)
