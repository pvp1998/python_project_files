# Adjacent pairs are swapped repeatedly until all the elements are in order

list = [1,4,5,8,2]

def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j+1], list[j] = list[j], list[j+1]
    return list



print(bubble_sort(list))