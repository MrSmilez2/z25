import re


example = '''Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
01-07-2018 Lorem Ipsum has been the industry a s x a01-02-2019a 31-12-2000 
41-12-2000
39-12-2000'''


def get_datetimes(random_string):
    pattern = re.compile(
        r'((?:[0-2][1-9]|[3][0-1])-(?:[0][1-9]|[1][0-2])-\d{4})'
    )
    return pattern.findall(random_string)


print(get_datetimes(example))