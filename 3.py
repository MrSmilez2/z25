def composition(f, g):
    def h(*args, **kwargs):
        return f(g(*args, **kwargs))
    return h