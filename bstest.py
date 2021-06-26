from bs4 import BeautifulSoup
import requests


url = '/Users/leonkulo/Desktop/sublime/bstest.html'
htmlfile = open(url, encoding='utf-8')
bsObj = BeautifulSoup(htmlfile, 'lxml')

Mycity = []
CityObj = bsObj.find('dl')
Cities = CityObj.find_all('dt')
for City in Cities:
	Mycity.append(City.text)

Mycountry = []
CountryObj = bsObj.find('dl')
Countries = bsObj.find_all('dd')
for Country in Countries:
    Mycountry.append(Country.text)

print("國家:", Mycountry)
print("都市:", Mycity)    	

