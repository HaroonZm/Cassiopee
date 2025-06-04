# Variables camelCase et "while" à la place du "for", avec traitement itératif inhabituel

n = int(input())
xValues = [int(v) for v in input().split()]
meanGuess = int((sum(xValues)/n) + 0.5)
weirdAccumulator = 0
i = 0
while i < n:
    diff = xValues[i] - meanGuess
    weirdAccumulator = weirdAccumulator + (diff * diff)
    i += 1
print(weirdAccumulator)