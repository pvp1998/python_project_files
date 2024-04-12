def sum(n):
    if n <= 0:
        return 0
    new_sum =  n + sum(n-1)
    return new_sum

# print(sum(3))

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
        return total

def pair_sum(a, b):
    return a + b

print(pair_sum_sequence(3))