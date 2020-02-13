import time


def cache(num):
    def inner(func):
        def decorator(*args, **kwargs):
            time_passed = round(time.time())
            print(f'time_passed{time_passed}')
            result = func(*args, **kwargs)
            cache_key = func.__name__
            if not hasattr(cache, 'contain_time'):
                cache.contain_time = {cache_key: round(time.time())}
                return result
            else:
                if cache_key not in cache.contain_time:
                    cache.contain_time[cache_key] = round(time.time())
            print(cache.contain_time.items())
            if (time_passed - cache.contain_time[cache_key]) < num:
                print(f"ok {time_passed - cache.contain_time[cache_key]}, {num}")

                return result
            else:
                print(
                    f"not ok {time_passed - cache.contain_time[cache_key]}, {num}")
                del cache.contain_time[cache_key]
                print(cache.contain_time.items())

        return decorator
    return inner


@cache(5)
def random_func(a):
    time.sleep(a)
    return 1


# @cache(20)
# def another_func():
#     return 2
#
#
# @cache(20)
# def anotherone_func():
#     return 3

start = time.time()
print(random_func(2))
# print(another_func())
# print(anotherone_func())
print(random_func(3))
end = time.time()
print(random_func(3))

print(random_func(2))
print(random_func(2))
print(end - start)