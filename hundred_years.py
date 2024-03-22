from datetime import datetime

name = str(input("What is your name? "))
age = int(input("How old are you? "))
random_num = int(input("Enter random number: "))

current_year = 2024
future_year = datetime.now().year + (100-age)

print(f"{name}, you will be 100 years old in the year {future_year}!\n"* random_num)
