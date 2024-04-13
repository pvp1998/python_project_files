lines = 'Write a python function that accepts a string and calculates the number of upper case letters and lower case letters'

def upper_lower(a):
    upper = 0
    lower = 0
    for i in lines:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1

    return (f'Upper case count is {upper} and lower case count is {lower}')


print(upper_lower(lines))