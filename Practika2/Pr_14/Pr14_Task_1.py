import time

def Time_func(func):
    def wrapper(*args):
        t = time.time()
        func(*args)
        dt = time.time() - t
        print(f"Time: {dt}")

    return wrapper

@Time_func
def append(n):
    num_list: list = []
    for i in range(n):
        if i % 2 == 0:
            num_list.append(i)
    return num_list

@Time_func
def comprehension(n):
    comprehension = [i for i in range(n + 1) if i % 2 == 0]
    return comprehension


n = int(input("Write the number: "))

print("For append():")
append(n)

print("For comprehension():")
comprehension(n)