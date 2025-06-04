k_n = input().split()
k = int(k_n[0])
n = int(k_n[1])
if k % 2 == 0:
    print(k // 2, end=" ")
    i = 0
    while i < n - 1:
        print(k, end=" ")
        i += 1
else:
    l = []
    i = 0
    while i < n:
        l.append((k + 1) // 2)
        i += 1
    i = 0
    count = n // 2
    while i < count:
        if l[-1] == 1:
            l.pop()
        else:
            l[-1] -= 1
            j = 0
            while j < (n - len(l)):
                l.append(k)
                j += 1
        i += 1
    idx = 0
    while idx < len(l):
        print(l[idx], end=" " if idx < len(l)-1 else "\n")
        idx += 1