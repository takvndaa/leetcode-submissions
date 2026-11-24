def add_two_numbers() -> int:
    lst = input().split(",")
    nums = []
    for num in lst:
        nums.append(int(num))

    return sum(nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
