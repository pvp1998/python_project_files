list = [9, 2, 5, 7, 8, 1, 6]

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]

    return list

print(selection_sort(list))
