n = int(input())
a_l = input().split()
for i in range(n):
    a_l[i] = int(a_l[i])

max_num = a_l[0]
min_num = a_l[0]

for num in a_l:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

ans = max_num - min_num
print(ans)