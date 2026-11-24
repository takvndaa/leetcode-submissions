from typing import List

def read_integers() -> List[int]:
    lst = input()
    lst = lst.split(",")
    nums = []
    for num in lst:
        nums.append(int(num))
    return nums



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
