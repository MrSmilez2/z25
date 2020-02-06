def custom_range(*random_list):
    filled_list = []
    if len(random_list) == 1:
        n = random_list[0]
        first_num = 0
        while first_num < n:
            filled_list.append(first_num)
            first_num += 1
        return filled_list
    elif len(random_list) == 2:
        n = random_list[1]
        first_num = random_list[0]
        while first_num < n:
            filled_list.append(first_num)
            first_num += 1
        return filled_list
    elif len(random_list) == 3:
        n = random_list[1]
        first_num = random_list[0]
        while first_num < n:
            filled_list.append(first_num)
            first_num += random_list[2]
        return filled_list
