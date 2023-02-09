import math

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print("!!!TASK 7!!!")
def my_funct(nums):
    isTrue = False
    for i in range(1, len(nums)):
        num = nums[i] * 10 + nums[i-1]
        if num == 33:
            isTrue = True
            break
    return isTrue

nums = list(map(int, input().split()))
print((nums))
