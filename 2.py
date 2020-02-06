def accum(random_str):
    b = list(map(lambda x: x.capitalize(), list(map(lambda x: x * (list(random_str).index(x) + 1), list(random_str)))))
    c = "-".join(b)
    return c
