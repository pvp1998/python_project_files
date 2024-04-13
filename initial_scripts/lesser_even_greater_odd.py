first = 4
second = 3
def lesser_even(a, b):
    if a % 2 != 0 or b % 2 != 0:
        if a > b:
            return a
        else:
            return b
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b

print(lesser_even(first, second))