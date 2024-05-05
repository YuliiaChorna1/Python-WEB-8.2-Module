from functools import lru_cache

@lru_cache(maxsize=4)
def test(val):
    print("I'm in function")
    res = 0

    res = int(input(": number"))

    return val + res + 32

print(test(12))
print(test(12))
print(test(12))
print(test(23))
