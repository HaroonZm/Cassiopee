D = {}
q = int(input())
for i in range(q):
    L = input().split()
    if L[0] == '0':
        key, x = L[1], L[2]
        D[key] = x
    else:
        key = L[1]
        print(D[key])