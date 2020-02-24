import time


"""
0. (*) Написать функцию, которая из списка чисел составляет
максимальное число
[98, 9, 34] -> 99834
"""


def max_number(_list):
    pass


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


class MultiOpenFile:

    def __init__(self, *args):
        self.list_of_files = args
        self.open_file_list = []

    def __enter__(self):
        for item in self.list_of_files:
            self.open_file_list.append(open(*item))
        return self.open_file_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        for item in self.open_file_list:
            item.close


"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время
выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""


class Timer:
    def __init__(self, _str):
        self._str = _str
        self.start = 0
        self.duration = 0

    def now(self):
        self.duration = time.time() - self.start
        self._str = f'Time: {self.duration} sec'
        return self._str

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time


if __name__ == '__main__':
    # assert max_number([234, 123, 98]) == 98234123
    # assert max_number([1, 2, 3, 4]) == 4321
    # assert max_number([]) is None
    # assert max_number([98, 9, 34]) == 99834
    # print('max_number - OK')
    with MultiOpenFile(
            ('file1.txt', 'w'), ('file2.txt', 'w'), ('fileN.txt', 'w')
    ) as file_list:
        print("hello")
        for item in file_list:
            item.write("ghfh")

    with Timer("Time: {}") as timer:
        time.sleep(2)
        print(timer.now())
        time.sleep(3)
        print(timer.now())
