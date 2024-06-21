# If n= 200703, return: 1/2 + 2/7 + 7/3

def my_func(n: int):
    withoutzero = str(n).replace('0', '')
    temp = "1"
    result = 0
    for i in range(len(withoutzero)):
        if i == len(withoutzero)-1:
            temp += withoutzero[i]
        else:
            temp += withoutzero[i]*2
    for j in range(0, len(temp)-1, 2):
        result += int(temp[j])/int(temp[j+1])
    return result

print(my_func(200703))