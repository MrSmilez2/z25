def flip(func):
    def decorator(*args, **kwargs):
        result = func(*args[::-1])
        return result
    return decorator


@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res
