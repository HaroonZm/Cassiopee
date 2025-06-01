from statistics import mean

def apply_min_score(score):
    return max(40, score)

scores = []
for i in range(5):
    val = int(input())
    scores.append(val)

scores = list(map(apply_min_score, scores))

avg = mean(scores)
print(avg)