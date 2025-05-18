n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
al, bo = 0, 0
for i in a[0::2]:
    al += i
for i in a[1::2]:
    bo += i
print(al - bo)