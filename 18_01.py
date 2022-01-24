import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://data.gov.lv./lv")

soup = BeautifulSoup(lapa.content, 'html.parser')

#print(soup.find_all('li'))
print(soup.find_all(class_ = "datacat"))

print(soup.find_all(class_ = "datacat")[4].get_text())
# print(soup.find_all('p')[1].get_text())
# print(soup.find_all('p')[2].get_text())
# print(soup.find_all('p')[3].get_text())