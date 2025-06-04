n = int(input())
d, x = map(int, input().split())
count = 0
for i in range(n):
    a = int(input())
    if d % a == 0:
        num = d // a
    else:
        num = d // a + 1
    count = count + num
count = count + x
print(count)