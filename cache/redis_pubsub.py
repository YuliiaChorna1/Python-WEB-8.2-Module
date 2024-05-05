import redis

r = redis.Redis(host="localhost", port=6379, password=None)

redis_connection = r.pubsub()
r.publish("work's done", "hello")

redis_connection.subscribe("work's done")

for message in redis_connection.listen():
    print(message)
