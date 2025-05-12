from statistics import mean

scores = [int(input()) for i in range(5)]
scores = list(map(lambda x: max(40, x), scores))
print(mean(scores))