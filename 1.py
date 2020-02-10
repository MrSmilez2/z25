def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for z in kwargs:
        print(z, kwargs.get(z), type(kwargs.get(z)))
