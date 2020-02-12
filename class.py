
# def tag(string):
#     def inner(func):
#         def decorator(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return f'<{string}>{result}</{string}>'
#         return decorator
#     return inner
#
#
#
# @tag("div")
# def foo(a):
#     return a
#
# print(foo(1))
# def is_latin(sym):
#     if ord("a") <= ord(sym) <= ord("z"):
#         return True
#
#
# print(is_latin("d"))
# def foo(val):
#     a = [1, 1]
#     b = 0
#     first_num = 1
#     second_num = 1
#     third_num = first_num + second_num
#     while a[] <= val:
#         a.append(third_num)
#         print(a)
#     return a
# print(foo(10))

# import time
#
#
# def sleeping(func):
#     def decorator(*args, **kwargs):
#
#         return func(*args, **kwargs)
#     return decorator
#
#
# @sleeping
# def func_sleeping(seconds):
#     time.sleep(seconds)
#
#     return str(seconds)
import re

def find_word(string):
    pattern = re.compile(r'\d*[0,2,4,6,8]\b')
    return pattern.findall(string)
s = '''123 12312
c12 12312412312312
ddasd'''
print(find_word(s))
