import os
import time
import json
import redis
import pymongo
import dotenv

dotenv.load_dotenv()
client = pymongo.MongoClient(os.environ['DB_LOCAL_URI'])

r = redis.Redis(host="localhost", port=6379, password=None)

def timer_wrapper(func):
    def timer(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()

        print(f"Getting worker took: {end - start} seconds")

        return res

    return timer


@timer_wrapper
def get_worker(collection, worker_name):
    r.incr('counter1')

    result = r.get(worker_name)

    if result is None:
        print("Getting value from DB")
        result = collection.find_one({"name": worker_name}, {"_id": 0})
        r.set(worker_name, json.dumps(result))
    else:
        result = json.loads(result)

    return result


if __name__ == "__main__":
    collection = client.office.workers

    collection.delete_many({})
    r.delete("Den")

    collection.insert_one({
        "name": "Den", "age": 22, "position": "Trainee Engineer"
    })

    print(get_worker(collection, "Den"))
    print("---------------------------")
    print(get_worker(collection, "Den"))


    print(f"You tried to get worker: {r.get('counter1')} times")
