a = [1, 2, 3, 4, 5]
b = []

for i in range(len(a)):
    temp_list = a[:]
    temp_sum = 0
    temp_list.pop(i)
    for j in range(len(a)-1):
        if j == 0:
            temp_sum = temp_list[j]
        else:
            temp_sum *= temp_list[j]
    b.append(temp_sum)


print("A:", a)
print("B:", b)