array = [6, 1, 3, 3, 3, 6, 6]

array.sort()
i = 0
while i < len(array):
    if array.count(array[i]) == 1:
        print(array[i])
        break
    else:
        i += 3