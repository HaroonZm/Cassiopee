n = int(input())
a = list(map(int, input().split()))
if n < 3:
    print(1)
    exit(0)
cnt = 1

increase = a[1] - a[0];
for i in range(2, len(a)):
    new_inc = a[i] - a[i-1];
    if increase * new_inc < 0:
        cnt += 1
        increase = 0
    elif increase == 0:
        increase = new_inc
print(cnt)