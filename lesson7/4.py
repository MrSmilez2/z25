import re


example = '''Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
01-07-2018 Lorem Ipsum has been the industry a s x 01-02-2019a 31-12-2000 
41-12-2000
39-12-2000'''


def get_words(random_string, sym):
    get_words_dict = {
        ('consonants', 'vowels'): r'[^\d\W]\w+',
    ('consonants',):  r'\b[^eyuioaEYUIOA\d\W ]\w+',
    ('vowels',): r'\b[eyuioaEYUIOA]\w+'
    }
    pattern = re.compile(get_words_dict[sym])
    return pattern.findall(random_string)


print(list(get_words(example, ('consonants',))))
print(list(get_words(example, ('vowels',))))
print(list(get_words(example, ('consonants', 'vowels'))))

