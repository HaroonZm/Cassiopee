scores = [int(input()) for _ in range(5)]
total = sum(score if score >= 40 else 40 for score in scores)
print(total // 5)