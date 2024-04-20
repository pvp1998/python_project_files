l1 = [1,1,1,2,2,3]
l2 = [0,0,1,1,1,1,2,3,3]


def max_two_list(l1):
    new_dict = {}
    threshold = 2
    breaching_count = 0
    for i in l1:
        if i not in new_dict.keys():
            new_dict[i] = 1
        else:
            new_dict[i] = new_dict.get(i,0) + 1

    for value in new_dict.values():
        if value > threshold:
            diff = value - threshold
            breaching_count += diff

    print(len(l1) - breaching_count)


print(max_two_list(l2))









