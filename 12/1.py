from random import randint

def rand5():
    return randint(1, 5)

def rand7():
    nums = [0, 0, 0, 0, 0, 0, 0]
    while len(set(nums)) != 7:
        for i in range(7):
            nums[i] += rand5()
    return nums.index(max(nums))+1


print(rand7())