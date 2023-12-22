# Воспользуемся MongoDB TTL индексом для удаления документа после определеннго времени 
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

collection.create_index("expireAt", expireAfterSeconds=0)

expire_time = datetime.utcnow() + timedelta(hours=24)
document = {
    "field1": "value1",
    "field2": "value2",
    "expireAt": expire_time
}
collection.insert_one(document)

