a = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5]

#Give the length of the list by removing the duplicates

#Two approaches

# 1. By using a counter for unique number
def new_list(a):
    initial_length = len(a)
    counter = 0
    new_dict = dict()
    for i in range(len(a)):
        if a[i] not in new_dict:
            new_dict[a[i]] = 1
        else:
            new_dict[a[i]] += 1

    for value in new_dict.values():
        if value > 2:
            counter += value - 2

    return initial_length - counter



    return new_dict




# 2. By creating a new list with unique keys and get the length of that new_list
# def new_list(a):
#     counter = 0
#     sub_list = []
#     new_dict = dict()
#     for i in a:
#         if i not in new_dict:
#             new_dict[i] = 1
#             sub_list.append(i)
#
#     return len(sub_list)



print(new_list(a))

