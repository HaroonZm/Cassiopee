num = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(num):
    minj = i
    for j in range(i, num):
        if a[j] < a[minj]:
            minj = j
    a[i], a[minj] = a[minj], a[i]
    if i != minj:
        cnt += 1

print(" ".join(str(i) for i in a))
print(cnt)