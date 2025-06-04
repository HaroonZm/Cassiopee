a = int(input())
a_li = input().split()
for i in range(a):
    a_li[i] = int(a_li[i])

b = int(input())
b_li = input().split()
for i in range(b):
    b_li[i] = int(b_li[i])

merged = a_li + b_li
unique = []
for num in merged:
    if num not in unique:
        unique.append(num)

unique.sort()

for num in unique:
    print(num)