import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/2021_debug/")
print(lapa)
#print(lapa.content)

soup = BeautifulSoup(lapa.content, 'html.parser')
print(soup.prettify())