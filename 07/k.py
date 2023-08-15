l = [10, 15, 3, 7]
k = 17

def f(l, k):
    for x in range(len(l)-1, -1, -1):
        for y in range(x-1, -1, -1):
            if l[x]+l[y] == k:
                return True
    return False


print(f(l, k))
