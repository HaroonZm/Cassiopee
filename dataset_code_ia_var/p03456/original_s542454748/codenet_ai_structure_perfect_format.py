a, b = map(int, input().split())
n = int(str(a) + str(b))
m = 'No'
for i in range(1, 1000):
    if i ** 2 == n:
        m = 'Yes'
print(m)