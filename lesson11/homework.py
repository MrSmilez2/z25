class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        res = self.first
        if res > self.n:
            raise StopIteration
        self.first, self.second = self.second, self.first + self.second
        return res


class Even:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.start
        if res > self.n:
            raise StopIteration
        self.start += 2
        return res


class Factorials:
    def __init__(self, n):
        self.n = n
        self. start = 1
        self.res = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.n:
            self.res *= self.start
            self.start += 1
            return self.res
        raise StopIteration

