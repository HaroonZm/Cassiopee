a = int(input())
count = 0
for x in range(a//2+1):
    y = a - x
    s = int(str(x)+str(y)) - int(str(y)+str(x))
    if s == a:
        count += 1
print(count)