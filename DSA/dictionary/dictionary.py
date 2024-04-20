# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
#
# def merge_dicts(dict1, dict2):
#     for i in dict2:
#         if i in dict1:
#             dict1[i] = dict1.get(i, 0) + dict2[i]
#         else:
#             dict1[i] = dict2[i]
#     return dict1
#
# #print(merge_dicts(dict1, dict2))
#
# def merge_dicts_two(dict1, dict2):
#     new_dict = dict1.copy()
#     for key, value in dict2.items():
#         new_dict[key] = new_dict.get(key, 0) + value
#     return new_dict
#
# print(merge_dicts_two(dict1, dict2))

#Key with highest value

my_dict = {'a': 5, 'b': 9, 'c': 2}

# def max_value_key(my_dict):
#     max = 0
#     max_key = None
#     for key, value in my_dict.items():
#         if value > max:
#             max = value
#             max_key = key
#     return max_key


# def max_value_key(my_dict):
#     return max(my_dict, key=my_dict.get)
#
# print(max_value_key(my_dict))

def reverse_keys(my_dict):
    new_dict = {}
    for keys, values in my_dict.items():
        new_dict[my_dict[keys]] = keys

    return new_dict

print(reverse_keys(my_dict))




s = """Big data engineering is a booming field Working with data is interesting and fun"""

def count_words(s):
    tracker = {}
    l_string = s.split(' ')
    for l in l_string:
        if l.lower() not in tracker.keys():
            tracker[l.lower()] = 1
        else:
            tracker[l.lower()] = tracker.get(l) + 1
    return tracker

new_dict = count_words(s)



