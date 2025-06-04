n = int(input())
lst = [0] * 100002
for i in range(n):
    a, b = map(int, input().split())
    lst[a - 1] += 1
    lst[b] -= 1

for i in range(1, len(lst)):
    lst[i] = lst[i] + lst[i-1]

i = n
while i >= 0:
    if i <= lst[i]:
        print(i)
        break
    i -= 1