from bs4 import BeautifulSoup
import requests
import time

def title(url):
  if url == "":
    url = input("Enter URL: ")
    time.sleep(5)
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    title = doc.select_one('meta[itemprop="name"][content]')['content']
    return title
  else:
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    title = doc.select_one('meta[itemprop="name"][content]')['content']
    return title
