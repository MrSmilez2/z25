def accum(_str):
    b = list(
        map(
            lambda x: x.capitalize(), list(
                map(
                    lambda x: x * (list(_str).index(x) + 1), list(_str)
                    )
                )
            )
    )
    c = "-".join(b)
    return c
