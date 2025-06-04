w = int(input())
n = int(input())

lines = list(range(1, w+1))

for _ in range(n):
    a,b = input().split(',')
    a = int(a)
    b = int(b)
    # echanger les elements aux positions a-1 et b-1
    temp = lines[a-1]
    lines[a-1] = lines[b-1]
    lines[b-1] = temp

for num in lines:
    print(num)