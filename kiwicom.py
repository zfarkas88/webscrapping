from bs4 import BeautifulSoup
import requests
import time
quote_page = ['https://www.kiwi.com/us/search/budapest-bud/-/anytime/2-10?passengers=2&priceMax=50&priceMin=0&sortBy=price','https://www.kiwi.com/us/search/budapest-bud/-/2017-01-01_2017-04-30/2-10?passengers=2&priceMax=50&priceMin=0&sortBy=price']
for pg in quote_page:
	page = requests.get(pg)
	soup = BeautifulSoup(page, 'html.parser')
	print(page)
	cities = soup.find_all('span', attrs={'class': 'city'})
	prices = soup.find_all('span', attrs={'class': 'price-content'})

	if len(cities)>0:
		for i in range(1, len(cities)):
			print (cities[i].string.strip(), " ", prices[i].findNext('span').findNext('span').findNext('span').string.strip())
	else:
		print('Sikertelen! :(')
	time.sleep(5)
