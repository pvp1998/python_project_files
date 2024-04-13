num = int(input("enter a number: "))


def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)

    return divisors

print(divisors(num))
