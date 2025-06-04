N = int(input())
lst = [1, 0]

def update(q, x):
    if q == 1:
        lst[0] = lst[0] * x
        lst[1] = lst[1] * x
    elif q == 2:
        lst[1] += x
    else:
        lst[1] = lst[1] - x

for i in range(N):
    entry = input().split()
    flag, val = int(entry[0]), int(entry[1])
    update(flag, val)

result = (-lst[1], lst[0])
print(result[0], result[1])