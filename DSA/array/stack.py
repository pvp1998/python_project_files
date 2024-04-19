arr = [1, 2, 3, 4, 6, 7, 9]


def missing_number(arr):
    for i in range(len(arr) + 1):
        if arr[i] + 1 != arr[i+1]:
            return arr[i] + 1


print(missing_number(arr))


def missing(arr, n):
    for i in range(n):
        if arr[i] + 1 != arr[i+1]:
            return arr[i] + 1




def missing_natural(arr, n):
    sum_n = (n * (n + 1))/2
    sum_arr = sum(arr)
    miss = sum_n - sum_arr
    return miss

print(missing_natural(arr, 6))







