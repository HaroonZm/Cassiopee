lst = [1]*50021
for i in range(50021):
    if i == 0:
        lst[i] = 0
    else:
        if lst[i] == 1:
            j = i + 1
            k = i
            while True:
                k = k + j
                if k >= 50021:
                    break
                lst[k] = 0

while True:
    try:
        n = int(input())
        a = lst[0:n-1]
        b = lst[n:]
        print((n - 1 - a[::-1].index(1)), (n + 1 + b.index(1)))
    except EOFError:
        break