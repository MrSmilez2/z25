def points(random_list):
    list(random_list)
    i = 0
    our_points = 0
    while i < len(list(random_list)):
        b = list(random_list)[i].split(":")
        if int(b[0]) > int(b[1]):
            our_points += 3
        elif int(b[0]) == int(b[1]):
            our_points += 1
        else:
            our_points += 0
        i += 1
    return our_points
