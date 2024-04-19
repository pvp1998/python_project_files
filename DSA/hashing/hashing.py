# # list = ['Apple', 'And', 'apps', 'give', 'take', 'calculate']
# #
# # def hasing(arr):
# #     hash_table = dict()
# #     list_of_items = []
# #     for i in list:
# #         if len(i) in hash_table.keys():
# #             hash_table[len(i)] += 1
# #         else:
# #             hash_table[len(i)] = 1
# #     return hash_table
# #
# # print(hasing(list))
# #
# # def hashing_list(arr):
# #     hash_table = dict()
# #     list_of_items = []
# #     for i in list:
# #         if len(i) in hash_table.keys():
# #             hash_table[len(i)].append(str(i))
# #         else:
# #             hash_table[len(i)] = [str(i)]
# #     return hash_table
# #
# # print(hashing_list(list))
#
#
# def mod_hash(a, b):
#     mod = a % b
#     hash_table = {}
#     hash_table[mod] = a
#     return hash_table
#
# print(mod_hash(400, 24))
#
#
# def mod_hash_ascii(s, b):
#     total = 0
#     hash_table = {}
#     for i in s:
#         total += ord(i)
#     mod = total % b
#     hash_table[mod] = s
#     return hash_table
#
#
# print(mod_hash_ascii('ABC', 24))

arr1 = [8, 7, 2, 5, 3, 1]
arr2 = [5, 2, 6, 8, 1, 9]
targetnum1 = 10
targetnum2 = 10

def find_pair(arr, num):
    result_list = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                result_list.append([arr[i], arr[j]])
    return result_list

print(find_pair(arr2, targetnum2))


