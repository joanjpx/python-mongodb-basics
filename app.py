from pymongo import MongoClient

MONGO_URI="mongodb://localhost:27017";

client = MongoClient(MONGO_URI);

db = client['teststore'];

ProductsCollection = db['products'];
UserCollection = db['users'];

product = [{
	"name" : "iMac Pro I5",
	"price" : 2300.00
},{
	"name" : "Apple KeyBoard",
	"price" : 300.00
}];

user = {
	"user": "root",
	"pass": "123456",
	"name": "developer",
	"role": "admin"
}
## INSERT DATA
ProductsCollection.insert_many(product);
UserCollection.insert_one(user);

## RETRIEVING DATA
results = ProductsCollection.find();
filteredResults = ProductsCollection.find({"price":2300})
result = UserCollection.find_one({});

print(result);

ProductsCollection.delete_many({"price":1900})

for r in results:
	print(r['name']);


