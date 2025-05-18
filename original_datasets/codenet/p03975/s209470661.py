n, a, b = map(int, input().split())
i = 0
j = 0
while i < n:
    t = int(input())
    if (t < a or t >= b):
        j += 1
    i += 1
print(str(j))