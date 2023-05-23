import time

def time_func(func):
    start = time.time()
    result = func(1000000)
    end = time.time()
    print(f" Function time {func.__name__}: {end - start}")
    return result

@time_func
def append(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

@time_func
def comprehension(n):
    even_list = [i for i in range(n + 1) if i % 2 == 0]
    return even_list