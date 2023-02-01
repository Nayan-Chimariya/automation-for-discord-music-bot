from bs4 import BeautifulSoup
import requests

def title():
  url = input("Enter URL: ")
  page = requests.get(url)
  doc = BeautifulSoup(page.text, "html.parser")
  title = doc.select_one('meta[itemprop="name"][content]')['content']
  return title
