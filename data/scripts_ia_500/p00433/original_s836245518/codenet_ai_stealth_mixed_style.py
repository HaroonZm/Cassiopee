a = []
for i in input().split():
    a.append(int(i))

b = [int(x) for x in input().split()]

sum_a = 0
for num in a:
    sum_a += num

sum_b = sum(b)

if sum_a >= sum_b:
    print(sum_a)
else: print(sum_b)