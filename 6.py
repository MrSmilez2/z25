import time


def timer(func):
    def decorator(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return f'''Результат: {result}. 
               Время выполнения функции: {start_time - end_time}'''
    return decorator


@timer
def mult(val):
    count = 1
    x = 1
    while count < val:
        x *= count
        count += 1
    return x
