D = {}
q = int(input())
for i in range(q):
    L = input().split()
    if L[0] == '0':
        key = L[1]
        value = L[2]
        D[key] = value
    else:
        key = L[1]
        print(D[key])