import pymongo
"""
1. Install Mongo: python -m pip install pymongo
2. import pymongo



3. Install MongoDB: brew tap mongodb/brew
brew install mongodb-community@7.0
-Start MongoDB: brew services start mongodb/brew/mongodb-community@7.0
-Check if MongoDB is running: brew services list

4. Create a database called "Demo_Mongo":
"""
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Demo_Mongo"]

"5. Create a collection called 'customers':"

mycol = mydb["customers"]


"NOTE: If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document."

"6.Insert Multiple Documents, with Specified IDs:"

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

"7.Insert the list of documents (mylist) into the customers collection"
x3 = mycol.insert_many(mylist)

"8. Run the Migration Script: python lib/demo_mongoDB.py"

"9. You can check if a database exist by listing all databases:"
print(myclient.list_database_names())

"10. Connect and Use MongoDB: mongosh"

mylist1 = { "_id": 15, "name": "Andrea O'Brien", "address": "39 Green Street"}

x = mycol.insert_one(mylist1)





