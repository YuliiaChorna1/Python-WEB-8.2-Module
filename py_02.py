# Функція f обгортається декоратором @cache, який і зберігає значення функції протягом 
# 15 хвилин всередині кеша. Ми бачимо, що виклик функції відбувся один раз, 
# при повторному зверненні значення було взято з кеша.

import redis
from redis_lru import RedisLRU


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client) # default_ttl = 15min, max_size - cache size


@cache
def f(x):
    print(f"Function call f({x})")
    return x

if __name__ == '__main__':
    print(f"Result f(3): {f(3)}")
    print(f"Result f(3): {f(3)}")
