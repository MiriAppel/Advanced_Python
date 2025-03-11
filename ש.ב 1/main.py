import time

def running_time(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"זמן הריצה של הפונקציה {execution_time} שניות")
        return result
    return wrapper

def cache(func):
    cache_dict = {}
    def wrapper(*args):
        start_time = time.time()
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"זמן הריצה של הפונקציה {execution_time} שניות")
        return result
    return wrapper

# @running_time
@cache
def fibunachi(num):
    if num <= 1:
        return num+1
    return fibunachi(num - 1) + fibunachi(num - 2)

print(fibunachi(10))
