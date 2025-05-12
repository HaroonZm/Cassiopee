n = int(input())
cards = [input().split() for i in range(n)]

taroScore = 0
hanakoScore = 0

for i in range(n):
    sortedCards = sorted(cards[i])
    if cards[i][0] == cards[i][1]:
        taroScore += 1
        hanakoScore += 1
    elif cards[i][0] == sortedCards[0]:
      hanakoScore += 3
    else:
        taroScore += 3

print(taroScore, hanakoScore)