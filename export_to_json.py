from pymongo import MongoClient
from configs import MONGO_URL, DB_NAME, ORIGIN_FOLDER, PROCESSED_FOLDER, TIME_OUT
import datetime
from datetime import timezone
from datetime import datetime
import sys
import json

# mongodb_client = MongoClient(MONGO_URL)
# database = mongodb_client[DB_NAME]

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

start_str = sys.argv[1]
end_str = sys.argv[2]

start_date = datetime.strptime(start_str, '%Y-%m-%dT%H:%M:%S')
end_date = datetime.strptime(end_str, '%Y-%m-%dT%H:%M:%S')

client = MongoClient(MONGO_URL)
filter={
    'last_update': {
        '$gte': start_date
    }, 
    'last_update': {
        '$lte': end_date
    }
}
sort=list({
    'last_update': 1
}.items())

result = client['prounciation']['tasks'].find(
  filter=filter,
  sort=sort
)
tmp = []
for task in result:
    tmp.append(task)
json.dump(tmp, open('data/'+'tasks'+ start_str + '_' + end_str+'.json', 'w'), default=str)