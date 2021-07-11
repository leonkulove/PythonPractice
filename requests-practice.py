import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.youtube.com/playlist?list=PLcCTPbs8iOoEO4UNN7hj0UX-ByMh7f6BS")
#print(html.text)
sp = BeautifulSoup(html.text, 'lxml')
print(type(sp.title))
print(sp.title)
print(sp.title.text)
#ist1 = sp.find_all("a")
#list1 = sp.find_all("a", "pl-video-title-link")
#print(ist1)