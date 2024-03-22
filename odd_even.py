take_number = int(input("Enter the number: "))
num = take_number
check = int(input("Enter another number: "))

def odd_even(n):
    if n%2 == 0:
        print('Entered number', n, 'is an even number')
        if n%4 == 0:
            print("You number is divisible by 4 as well")
    else:
        print("Entered number", n, 'is an odd number')

odd_even(take_number)

def divisible(n, c):
    if n%c == 0:
        print(f"given {n} is divisible by {c}")
    else:
        print(f'given {n} is not divisible by {c}')

divisible(num, check)