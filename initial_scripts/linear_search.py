list = [1,2,4,5,8]
num = 5

def linear_search(list: list, num: int) -> bool:
    for i in range(len(list)):
        if list[i] == num:
            return True

if linear_search(list, num):
    print("Found")
else:
    print("Not Found")