x=int(input())
count=100000
suma=0
sumb=0
for a in range(1, x):
    b = x-a
    y = sum(map(int, str(a))) + sum(map(int, str(b)))
    if y<count:
        count=y
print(count)