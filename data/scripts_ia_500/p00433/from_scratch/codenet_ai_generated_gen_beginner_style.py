a = input().split()
b = input().split()
a_scores = [int(x) for x in a]
b_scores = [int(x) for x in b]
sum_a = 0
sum_b = 0
for i in range(4):
    sum_a += a_scores[i]
    sum_b += b_scores[i]
if sum_a >= sum_b:
    print(sum_a)
else:
    print(sum_b)