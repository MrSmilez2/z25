number_names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen",  18: "eighteen", 19: "nineteen"}
number_list = ['four', 'one', 'three', 'two']


def sort_by_abc(random_list):

    return list(sorted(random_list, key=lambda number: number_names[number]))
