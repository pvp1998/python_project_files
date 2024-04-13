list = [1, 2, 3, 4, 5, 6]
num = 4


# Even the below approach will lead to looping of atleast half of the elements of a list leading O[n/2] which is almost as equal as 0[n]
# def binary_search(list, num):
#     if len(list)%2 != 0:
#         mid_point_index = (len(list) + 1) // 2 - 1
#     else:
#         mid_point_index = len(list)//2
#
#     # return mid_point_index
#
#     if num > list[mid_point_index]:
#         i = mid_point_index
#         while i <= len(list):
#             if list[i] == num:
#                 return i
#             i = i + 1
#     elif num == list[mid_point_index]:
#         return mid_point_index
#     elif num < list[mid_point_index]:
#         i = mid_point_index
#         while i >= 0:
#             if list[i] == num:
#                 return i
#             i = i - 1
#     else:
#         return -1
#
#
#
# print(binary_search(list, num))

def bs(list, num):
    l = 0
    r = len(list) - 1

    while l <= r:
        mid_point_index = l + (r - l) // 2
        if num == list[mid_point_index]:
            return mid_point_index
        elif num > list[mid_point_index]:
            l = mid_point_index + 1
        else:
            r = mid_point_index - 1

    return mid_point_index






print(bs(list, num))