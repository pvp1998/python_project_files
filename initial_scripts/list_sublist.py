ask = int(input("Please enter a number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def sublist(a, b):
    new_list = []
    for i in range(len(a)):
        if a[i] < b:
            new_list.append(a[i])
    return new_list


print(sublist(a, ask))