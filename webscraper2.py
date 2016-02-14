import requests
import re
import mongodbconn
from bs4 import BeautifulSoup


url ="http://www.theatlantic.com/most-popular/"; 
r = requests.get(url)

#Pulls all HTML Content From Page
soup = BeautifulSoup(r.content, "html.parser")
sections = soup.find_all("li", {"class": "article blog-article"})

for articles in sections: 

	#Gets Article Title 
	title = articles.find("h2", {"class": "hed"})
	title =  title.text

	#Gets Subheader 
	subheader = articles.find("p")
	subheader =  subheader.text

	#Clean Data 
	subheader = re.sub(u'[,\u2019\u2122\u201d\u201c]', '', subheader)


	#Gets Article Link
	link = articles.find('a')
	url =  "http://theatlantic.com" + link.get('href')

	#Spacing 
	print " " 
	print " " 

	#Insert Into Database
	mongodbconn.Insert(title, subheader, url)














	

