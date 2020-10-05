import requests
from bs4 import BeautifulSoup
import time
import json

url = 'https://www.tripadvisor.fr/Restaurant_Review-g187079-d2211150-Reviews-Perditempo-Bordeaux_Gironde_Nouvelle_Aquitaine.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


with open('urls.txt', 'r') as inf:
    with open ('restaurant.json', 'w') as outf:    
        for row in inf:
            url = row.strip()
            res = requests.get(url)
            if res.ok:
                soup = BeautifulSoup(res.text,'html.parser')
                name = soup.find('h1', class_='_3a1XQ88S').text
                adress = soup.find('a', class_='_15QfMZ2L', href='#MAPVIEW').text
                elements = soup.find_all('div', class_='_1XLfiSsv')
                speciality_list = []
                for element in elements:
                    speciality = (element.text).replace(',', '').split()
                    speciality_list.append(speciality)
                print(speciality_list[1][0])
                prix_moyen = soup.find(class_='_1XLfiSsv').text
                notes = soup.find(class_='r2Cf69qf').text
                nbre_avis = soup.find('a', class_='_10Iv7dOs', href='#REVIEWS').text
                headers = soup.find_all(class_='header_nondesktop')
                top_avis = []
                for header in headers:
                    element = header.text
                    top_avis.append(element)
                print(str(top_avis))
                print('Enseigne : ' + name,
                    'Adresse : ' + adress,
                    'Specialite : ' + str(speciality_list),
                    'Fouchette de prix : ' + prix_moyen,
                    'Note globale : ' + notes,
                    'Nombre d\'avis : ' + nbre_avis,
                    'Top avis : ' + str(top_avis))
                data = {
                    "Enseigne": name,
                    "Adresse": adress,
                    "Specialite": str(speciality_list),
                    "Fourchette de prix": prix_moyen,
                    "Note globale": notes,
                    "Nombre d'avis": nbre_avis,
                    "Top avis": str(top_avis)
                }
                json.dump(data, outf)
    time.sleep(3)                   