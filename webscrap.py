#Se importan librerias
import requests
from bs4 import BeautifulSoup

#Acceder a ebay: crime books
ebay_url = 'https://www.ebay.com/sch/crime+books'
response = requests.get(ebay_url)
print(response)

#Encontrar los titulos
soup = BeautifulSoup(response.text, 'html.parser')
tags = soup.findAll('h3', class_ = 's-item__title')

#Prueba: obtener el texto del primer titulo
tags[1].text
print(tags[1].text)

#Obtener todos
crime_listings = []
for i in range(1,len(tags)):
    crime_listings.append(tags[i].text)
print(crime_listings)
