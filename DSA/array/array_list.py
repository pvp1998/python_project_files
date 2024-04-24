
#Identify missing number in a naturally ordered sorted list
# miss = [1, 2, 3, 4, 6]
# num = 6
#
# def missing_nums(arr, n):
#     sum_natural_n = (n * (n + 1))// 2
#     sum_arr = sum(arr)
#     missing = sum_natural_n - sum_arr
#     return missing

#print(missing_nums(miss, num))


# Two sum pairs with dictionary
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
#
# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i

#print(two_sum(nums, target))

# Find out the max of two products
# arr = [1, 7, 3, 4, 9, 5]
#
# def max_two_products(arr):
#     products_list = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             product = arr[i] * arr[j]
#             products_list.append(product)
#     return max(products_list)
#
# def max_two_product_two(arr):
#     arr.sort(reverse=True)
#     return arr[0] * arr[1]


# new_arr = [1, 7, 3, 4, 9, 5]
# def max_two_product_three(arr):
#     max1 = 0
#     max2 = 0
#
#     for i in arr:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2 and i < max2:
#             max2 = i
#     return max1 * max2
#
# print(max_two_product_three(new_arr))



# l1 = [1,1,1,2,2,3]
# l2 = [0,0,1,1,1,1,2,3,3]
#
# def max_twotimes_list(l1):
#     new_dict = {}
#     threshold = 2
#     breaching_count = 0
#     for i in l1:
#         if i not in new_dict.keys():
#             new_dict[i] = 1
#         else:
#             new_dict[i] = new_dict.get(i,0) + 1
#
#     for value in new_dict.values():
#         if value > threshold:
#             diff = value - threshold
#             breaching_count += diff
#
#     print(len(l1) - breaching_count)


#print(max_twotimes_list(l2))

# Diagonal sum of two-dimensional list

# myList2D= [[1,2,3],
#            [4,5,6],
#            [7,8,9]]
#
# def two_dim_sum(l):
#     adds = 0
#     for i in range(len(l)):
#         adds = adds + (l[i][i])
#     return adds
#
# print(two_dim_sum(myList2D))


# mylist = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# def two_best_scores(mylist):
#     max1 = 0
#     max2 = 0
#     for i in mylist:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2 and i < max1:
#             max2 = i
#     return max1, max2
#
# print(two_best_scores(mylist))

arr1 = [1,2,2,1,1,3]
arr3 = [-3,0,1,-3,1,1,1,-3,10,0]

# def uniqueOccurrences(arr):
#     new_dict = {}
#     for i in arr:
#         if i not in new_dict.keys():
#             new_dict[i] = 1
#         if i in new_dict.keys():
#             new_dict[i] = new_dict.get(i, 0) + 1
#     seen = []
#     for i in new_dict.values():
#         if i not in seen:
#             seen.append(i)
#         else:
#             return False
#     return True
#
#
# print(uniqueOccurrences(arr1))

nums1 = [1,2,3]
nums2 = [2,4,6]

def find_difference(num1, num2):
    for i in num1:
        if i in num2:
            num1.











