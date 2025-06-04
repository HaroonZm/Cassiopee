scores = []
for i in range(5):
    point = int(input())
    if point < 40:
        point = 40
    scores.append(point)
average = sum(scores) // 5
print(average)