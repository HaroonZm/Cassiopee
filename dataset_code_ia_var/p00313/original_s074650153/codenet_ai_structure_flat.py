n = int(input())
a = list(map(int, input().split()))
del a[0]
b = list(map(int, input().split()))
del b[0]
c = list(map(int, input().split()))
del c[0]
count = 0
i = 1
while i <= n:
    if i in c and (not i in a or i in b):
        count += 1
    i += 1
print(count)