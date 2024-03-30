from collections import Counter

a = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5]

s = 'collections'
new = 'mom'
new2 = 'wow'

def palindrome(a):
    a_list = list(a)
    reverse_list = a_list[::-1]
    print(reverse_list)
    if a_list == reverse_list:
        print("Palindrome")
    else:
        print("Not palindrome")


palindrome(new2)