def introduce_on_debug(debug):
    def inner(func):
        def decorator(*args, **kwargs):
            if debug:
                return f'''identity
                    {func(*args, **kwargs)}'''
            else:
                return func(*args, **kwargs)
        return decorator
    return inner


@introduce_on_debug(debug=False)
def identity(x):
    return x
