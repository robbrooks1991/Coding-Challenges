import pymongo


def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is connected!"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e


conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
coll.drop()  # remove the collection
docs = [{"name": "Code", "surname": "Institute", "twitter": "@codersinstitute"},
        {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"},
        {"name": "Code", "surname": "Institute", "twitter": "@codersinstitute"}]
coll.insert_many( docs )
results = coll.find()
for doc in results:
    print doc