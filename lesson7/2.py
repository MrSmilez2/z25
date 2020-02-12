def counter(random_string="Count"):
    def inner(func):
        def decorator(*args, **kwargs):
            decorator.count += 1
            print(f'{random_string} - {decorator.count}')

            return func(*args, **kwargs)
        decorator.count = 0
        return decorator
    return inner


@counter("asd")
def random_func(*args, **kwargs):
    return 1


@counter()
def random_func_2(*args, **kwargs):
    return 1


print(random_func())
print(random_func())
print(random_func(23123))
print(random_func_2("LOL"))
print(random_func_2(2))