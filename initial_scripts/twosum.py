one = [2,7,11,15]

def twosum(a: list[int], b: int) -> list[int]:
    for i in range(len(one)):
        for j in range(i+1, len(one)):
            if one[i] != one[j] and one[i] + one[j] == b:
                return [one[i], one[j]]



print(twosum(one, 9))