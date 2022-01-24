# import requests
# from bs4 import BeautifulSoup

# # lapa = requests.get("https://vvsprogramm.github.io/2021_debug/")

# lapa = requests.get("http://vilanuvidusskola.blogspot.com/")


# soup = BeautifulSoup(lapa.content, 'html.parser')

# #Metode .find_all var tikt izmantota, lai atrastu konkrētu tagu jeb elementu visā lapā
# #print(soup.find_all('li'))
# print(soup.find('li'))

# #print(soup.find_all('p')[0].get_text())


import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/A/")



soup = BeautifulSoup(lapa.content, 'html.parser')

#print(soup.find_all('li'))
print(soup.find_all('p'))

print(soup.find_all('p')[0].get_text())
print(soup.find_all('p')[1].get_text())
print(soup.find_all('p')[2].get_text())
print(soup.find_all('p')[3].get_text())