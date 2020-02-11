import time


def timer(func):
    def decorator(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции - {end_time - start_time}')
        return result
    return decorator


@timer
def mult(val):
    count = 1
    x = 1
    while count < val:
        x *= count
        count += 1
    return x
