from pymongo import MongoClient 

#Connect to Local Hosted MongoDB Database 

try:
    client = MongoClient()
    client.server_info() # force connection on a request as the
                         # connect=True parameter of MongoClient seems
                         # to be useless here 
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 


def Insert(title, subheader, url): 

	#Create a table
	database = client.scraperDB

	#Create a collection, AKA a Table, in the database 
	table = database.scraperTable

	tableID = table.insert_one(
		{
			"title": title, 
			"subheader": subheader, 
			"url": url
		}
	)
	print "It works!"




