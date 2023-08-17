a = [1, 2, 3, 4, 5]
b = []

for i in range(len(a)):
    temp = 1
    for j in range(len(a)):
        if j != i:
            temp *= a[j]
    b.append(temp)

print("A:", a)
print("B:", b)