import requests
from bs4 import BeautifulSoup
import time
import json

url = 'https://www.tripadvisor.fr/Restaurant_Review-g187079-d2211150-Reviews-Perditempo-Bordeaux_Gironde_Nouvelle_Aquitaine.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Récupération de l'intégralité du html de la page
# print(res.text)

# Récupération des noms des restaurants

name = soup.find('h1', class_='_3a1XQ88S').text
#print(name)

# Récupération des adresses des restaurants
adress = soup.find('a', class_='_15QfMZ2L', href='#MAPVIEW').text
#print(adress)

# Récupération de la spécialité des restaurants
elements = soup.find_all('div', class_='_1XLfiSsv')
speciality_list = []
for element in elements:
    speciality = (element.text).replace(',', '').split()
    speciality_list.append(speciality[0:])
print(speciality_list)

# Récupération de la fourchette moyenne des prix des restaurants
prix_moyen = soup.find(class_='_1XLfiSsv').text
#print(prix_moyen)

# Récupération des notes des restaurants
notes = soup.find(class_='r2Cf69qf').text
#print(notes)

# Récupération du nombre d'avis des restaurants
nbre_avis = soup.find('a', class_='_10Iv7dOs', href='#REVIEWS').text
#print(nbre_avis)

# Récupération des tops avis des restaurants 
headers = soup.find_all(class_='header_nondesktop')
top_avis = []
for header in headers:
    element = header.text
    top_avis.append(element)
#print(top_avis)


# Tentative ratée pour récup' les notes sous forme de bulles

# tests = soup.find_all(class_='ui_bubble_rating bubble_45')
# for test in tests:
#     a = test.select('alt')
#     # print(a)

# for test in tests:
#     toto = test.select('alt')
#     print(toto)

# for test in tests:
#     bulle=tests[0]['alt']
#     print(bulle)

# toto=soup.find_all(class_='ui_bubble_rating bubble_35')
# print(toto)

# for test in tests:
#     bulle=test.text
#     print(bulle)

