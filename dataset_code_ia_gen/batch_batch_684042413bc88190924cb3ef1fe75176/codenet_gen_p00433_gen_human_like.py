a_scores = list(map(int, input().split()))
b_scores = list(map(int, input().split()))

sum_a = sum(a_scores)
sum_b = sum(b_scores)

print(sum_a if sum_a >= sum_b else sum_b)