# ============================================
# Title: Exercise 9.3 - Updating and Deleting Documents
# Author: Professor Krasso
# Date: 12 December 2020
# Modified By: Arlix Sorto
# Description: Updating and deleting documents in a MongoDB
#              database instance through Python and pymongo
# ===========================================

import pymongo
import pprint
import datetime

# Connects to local MongoDB instance
client = pymongo.MongoClient('localhost', 27017)
db = client.web335

# Update  the user document
db.users.update_one(
    {"employee_id": "0000001"},
    {
        "$set": {
            "email": "asorto@my365.bellevue.edu"
        }
    }
)
#Output the updated document.
employee_id = "0000001"
pprint.pprint(db.users.find_one({"employee_id": employee_id},{ 
    "_id":0,
    "date_created":0
}))
