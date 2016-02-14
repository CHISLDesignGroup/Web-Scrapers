from pymongo import MongoClient 

client = MongoClient()
print client.database_names()

db = client.scraperDB

cursor = db.scraperTable.find()

for document in cursor:
    print(document)
    print " " 
    print " " 


db.scraperTable.remove({})