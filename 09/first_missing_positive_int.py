def first_missing_positive_int(l):
    if 1 not in l:
        return 1
    sorted_list = sorted(list(set(l)))
    one_index = sorted_list.index(1)
    counter = 2
    for i in range(one_index + 1, len(sorted_list)):
        if sorted_list[i] == counter:
            counter += 1
        else:
            break
    return counter


print(first_missing_positive_int([3, 4, -1, 1]))
print(first_missing_positive_int([1, 2, 0]))