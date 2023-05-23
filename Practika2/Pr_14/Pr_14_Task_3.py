import time

def Time_func(func):
    def wrapper(*args):
        t = time.time()
        func(*args)
        dt = time.time() - t
        print(f"Time: {dt}")

    return wrapper

def fibo_cache(fn):
    cache = {}

    def wrapper(n):

        if n in cache:
            return cache[n]

        if not cache:
            for i in range(min(2, n + 1)):
                cache[i] = i

        for i in range(len(cache), n + 1):
            cache[i] = cache[i-1] + cache[i-2]

        print(f"last number is {cache[n]}")
        return cache[n]

    return wrapper

@Time_func
@fibo_cache
def fibCache(n):
    return n if n == 0 or n == 1 else fibCache(n - 1) + fibCache(n - 2)

n = int(input("Write the number: "))
old_n = int(input("Write the same number: "))
new_n = int(input("Write more number: "))

print(fibCache(n))
print(fibCache(old_n))
print(fibCache(new_n))