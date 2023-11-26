"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

numbers = [1, 2, 3, 4, 5]
k = 9
result = []

if k in numbers:
    result.append(k)
    print(result)
else:
    flag = False
    for i in range(len(numbers)):
        result.append(numbers[i])
        sum = numbers[i]
        for j in numbers[i+1:]:
            result.append(j)
            sum += j
            if sum > k:
                break
            elif sum == k:
                flag = True
                break
        if flag:
            break
        else:
            result = []
print(result)
