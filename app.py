import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time
import json

# with open('urls.txt', 'r') as inf:
#     with open ('restaurant.json', 'w') as outf:    
#         for row in inf:
#             url = row.strip()
#             res = requests.get(url)
#             if res.ok:
#                 soup=BeautifulSoup(res.text,'html.parser')
#                 titles=soup.find_all(class_='_1hkogt_o')
#                 for title in titles:
#                     name=title.find('h1').text
#                     adress=soup.find('a', class_='_15QfMZ2L', href='#MAPVIEW').text
#                     prix_moyen=soup.find(class_='_1XLfiSsv').text
#                     print('Nom : ' + name, 'Adresse : ' + adress, 'Fouchette : ' + prix_moyen)
#                     data={'\n'
#                     "Enseigne" : name,'\n'
#                     "Adresse" : adress, '\n'
#                     "Fourchette de prix" : prix_moyen'\n'
#                     }
#                     json.dump(data, outf)
#             time.sleep(3)



url='https://www.tripadvisor.fr/Restaurant_Review-g187079-d2211150-Reviews-Perditempo-Bordeaux_Gironde_Nouvelle_Aquitaine.html'
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')

#Récupération de l'intégralité du html de la page
#print(res.text)


#########################TABLE RESTO##############################

#Récupération des noms des restaurants
titles=soup.find_all(class_='_1hkogt_o')
for title in titles:
    name=title.find('h1').text
    #print(name)

#Récupération des adresses des restaurants
adress=soup.find('a', class_='_15QfMZ2L', href='#MAPVIEW').text
#print(adress)

#Récupération de la spécialité des restaurants
totos=soup.find_all(class_='_13OzAOXO _34GKdBMV')
for toto in totos:
    speciality=toto.find().text
#print(speciality)
totos=soup.find_all('a', class_='_2mn01bsa')
for toto in totos:
    speciality=toto.find('')

#Récupération de la fourchette moyenne des prix des restaurants
prix_moyen=soup.find(class_='_1XLfiSsv').text
#print(prix_moyen)

#########################TABLE AVIS##############################

#Récupération des notes des restaurants
notes=soup.find(class_='r2Cf69qf').text
#print(notes)

#Récupération du nombre d'avis des restaurants
nbre_avis=soup.find('a', class_='_10Iv7dOs', href='#REVIEWS').text
#print(nbre_avis)

#Tentative ratée pour récup' les notes sous forme de bulles
tests=soup.find_all(alt='4,5 sur 5 bulles')
for test in tests:
    bulle=test.find('alt')
    #print(bulle)

#Récupération 
headers=soup.find_all(class_='reason ui_column is-4')
for header in headers:
    avis_first=header.find(class_='header_desktop').text
    #print(avis_first)


dic={
"Enseigne" : name,
"Adresse" : adress, 
"Spécialités" : speciality,
"Fourchette de prix" : prix_moyen
}
#print(dic)

df = pd.DataFrame({
"Enseigne" : name,
"Adresse" : adress,
"Spécialités" : speciality,
"Fourchette de prix" : prix_moyen
},
index=[0])

#print(df)

