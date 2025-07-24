from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri="mongodb+srv://narayanammrudula6:zTeTYoy1AtiWl5cD@cluster0.jxqyreg.mongodb.net/"
client=MongoClient(uri,server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("🎉🎉Pinged Your Deployment. You Successfully connected to MongoDB 🎉🎉")
except Exception as e:
    print(e)
db=MongoClient("mydb")
collection=db['users']
collection.insert_one({
    'name': "Alice",
    'email': "alice@gmail.com",
    'age': 20
})
User.insert_many([
    {'name': "Bob",'email': "bob@gmail.com",'age': 30},
    {'name': "Charlie",'email': "charlie@gmail.com",'age': 35}
])
user=collection.find_one({'name':"Alice"})
