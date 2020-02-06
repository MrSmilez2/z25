def max_number_count(random_list):
    random_dict = {}
    for i in random_list:
        try:
            random_dict[i] += 1
        except KeyError:
            random_dict[i] = 1
    val = max(random_dict, key=lambda x: random_dict[x])
    print(f'({val},{random_dict[val]})')
