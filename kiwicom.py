from bs4 import BeautifulSoup
import requests
import time
quote_page = ('https://www.kiwi.com/us/search/budapest-bud/-/anytime/2-10?passengers=2&priceMax=150&priceMin=0&sortBy=price')
page = requests.get(quote_page)
print(page)
soup = BeautifulSoup(page.text,"lxml")
print(soup.prettify()[0:10])
cities = soup.find_all('span', attrs={'class': 'city'})
prices = soup.find_all('span', attrs={'class': 'price-content'})
if len(cities)>0:
	for i in range(1, len(cities)):
		print (cities[i].string.strip(), " ", prices[i].findNext('span').findNext('span').findNext('span').string.strip())
else:
	print('Sikertelen! :(')
