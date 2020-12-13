#============================================
# Title: Exercise 9.2 - Querying and Creating Documents
# Author: Professor Krasso
# Date: 12 December 2020
# Modified By: Arlix Sorto
# Description: Querying and creating documents in a MongoDB
#              database instance through Python and pymongo
#===========================================

#Imported modules
import pymongo 
import pprint
import datetime

#Connects to local MongoDB instance
client = pymongo.MongoClient('localhost', 27017)
db = client.web335

#Creating a user document.
user = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "jwick@email.com",
    "employee_id": "0000001",
    "date_created": datetime.datetime.utcnow()
}

#Inserting the new document to local instance.
user_id = db.users.insert_one(user).inserted_id

#Output user id.
print(user_id)

#Output the new inserted document.
employee_id = "0000001"

pprint.pprint(db.users.find_one({"employee_id": employee_id}))