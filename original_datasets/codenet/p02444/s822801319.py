import copy

n = int(input())
num = list(map(int, input().split()))

tmp = copy.deepcopy(num)
q = int(input())
for _ in range(q):
    b, m, e = map(int, input().split())
    for i in range(e - b):
        pos = b + (i + e - m) % (e - b)
        tmp[pos] = num[i + b]
    num = copy.deepcopy(tmp)

print(' '.join(str(n) for n in num))