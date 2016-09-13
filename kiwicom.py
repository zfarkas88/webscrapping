from bs4 import BeautifulSoup
import requests
import time

counter=0

while counter<10:
	quote_page = ('https://www.kiwi.com/us/search/budapest-bud/-/anytime/2-10?passengers=2&priceMax=50&priceMin=0&sortBy=price')
	page = requests.get(quote_page)
	#print ("Status code: ",page.status_code)
	soup = BeautifulSoup(page.text,"lxml")

	#file = open("out.log", "w")
	#file.write(page.text)
	#file.close()

	cities = soup.find_all('span', attrs={'class': 'city'})
	prices = soup.find_all('span', attrs={'class': 'price-content'})
	if len(cities)>0:
		break	
	else:
		counter=+1
		time.sleep(5)	
if len(cities)>0:
	for i in range(1, len(cities)):
                        print (cities[i].string.strip(), " ", prices[i].findNext('span').findNext('span').findNext('span').string.strip())
else:
	print("Sikertelen!")
