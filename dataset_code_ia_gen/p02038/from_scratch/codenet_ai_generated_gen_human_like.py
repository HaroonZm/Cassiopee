n = int(input())
p = input().split()

def M(x, y):
    if x == 'T' and y == 'T':
        return 'T'
    elif x == 'T' and y == 'F':
        return 'F'
    elif x == 'F' and y == 'T':
        return 'T'
    else:  # x == 'F' and y == 'F'
        return 'T'

res = p[0]
for i in range(1, n):
    res = M(res, p[i])

print(res)