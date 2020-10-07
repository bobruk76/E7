import json
import os
import redis
from bson import ObjectId
from pymongo import MongoClient


host = str(os.environ.get("REDIS_HOST", "localhost"))
port = int(os.environ.get("REDIS_PORT", 6379))
# r = redis.StrictRedis(host=host, port=port, db=1)

db_name = 'e7'

class Message():
    def __init__(self):
        mongo_client = MongoClient()
        collection = mongo_client[db_name]
        self.db = collection.messages
        self.result = False
        
    def set(self, message):
        try:
            self.db.insert({'message': message})
            self.result = True
        except:
            self.result = False

    def get_all(self):
        cursor = self.db.find()
        messages = list(cursor)
        return [item for item in messages]

    def get(self, _id):
        cursor = self.db.find({'_id': ObjectId(_id)})
        return list(cursor)[0]

    def update_tags(self, _id, new_tag):

        self.db.update({'_id': ObjectId(_id)}, {'$push': {'tags': new_tag}})
    
    # fib_memory = json.loads(r.get('fib_memory'))
    #
    # fib_max = json.loads(r.get('fib_max'))
    # if num <= fib_max:
    #     return fib_memory[str(num)]
    # for item in range(fib_max+1, num+1):
    #     fib_memory[str(item)] = fib_memory[str(item-2)] + fib_memory[str(item-1)]
    # r.set('fib_max', json.dumps(num))
    # r.set('fib_memory', json.dumps(fib_memory))
    # return fib_memory[str(num)]
