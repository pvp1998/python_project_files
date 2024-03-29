a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_list(a, b):
    new_dict = dict()
    new_list = []
    for i in a:
        if i in b:
            if i not in new_dict.keys():
                new_dict[i] = 1
                new_list.append(i)
    return new_list

print(common_list(a, b))
