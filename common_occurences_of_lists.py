first = [1, 2, 4, 5, 6]
second = [4, 2, 3, 9]

def common_occurences(a, b):
    counter = 0
    for i in range(len(first)):
        if first[i] in second:
            counter += 1

    return counter


print(common_occurences(first, second))