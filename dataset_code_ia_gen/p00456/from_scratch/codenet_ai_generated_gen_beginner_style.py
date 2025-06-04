w_scores = []
k_scores = []

for i in range(10):
    w_scores.append(int(input()))
for i in range(10):
    k_scores.append(int(input()))

w_scores.sort(reverse=True)
k_scores.sort(reverse=True)

w_sum = w_scores[0] + w_scores[1] + w_scores[2]
k_sum = k_scores[0] + k_scores[1] + k_scores[2]

print(w_sum, k_sum)