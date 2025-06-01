a = input().split()
b = input().split()

for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])

sum_a = 0
sum_b = 0

for num in a:
    sum_a = sum_a + num
for num in b:
    sum_b = sum_b + num

if sum_a >= sum_b:
    print(sum_a)
else:
    print(sum_b)