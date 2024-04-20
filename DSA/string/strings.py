#Length of longest substring without characters repeating

s = 'abcabcbb'
s1 = 'bbbbb'
s2 = 'pwwkew'
def max_len_substring(s):
    subs_list = []
    prev_values = []
    for i in s:
        if i not in subs_list:
            subs_list.append(i)
        elif i in subs_list:
            prev_values.append(len(subs_list))
            subs_list.clear()
            subs_list.append(i)

    return max(prev_values)

print(max_len_substring(s2))