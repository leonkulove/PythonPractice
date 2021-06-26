import bs4 
import requests

url = '/Users/leonkulo/Desktop/sublime/PythonPractice/bstest2.html'
htmlfile = open(url, encoding='utf-8')
bsjob = bs4.BeautifulSoup(htmlfile, 'lxml')

myriver = []
tableobj = bsjob.find('table').find('tbody')
tables = tableobj.find_all('tr')
for table in tables:
	river = table.find('td')
	myriver.append(river.text)

mycountry = []
for table in tables:
    countries = table.find_all('td')
    country = countries[1]
    mycountry.append(country.text)

print(myriver)
print(mycountry)    	
data = dict(zip(mycountry, myriver))
print(data)