def introduce_on_debug(debug):
    def inner(func):
        def decorator(*args, **kwargs):
            if debug:
                print(f'{func.__name__}')
                return func(*args, **kwargs)
            else:
                return func(*args, **kwargs)
        return decorator
    return inner


@introduce_on_debug(debug=True)
def identity(x):
    return x
