n = int(input())
cards = []
i = 0
while i < n:
    cards.append(input().split())
    i += 1
taroScore = 0
hanakoScore = 0
i = 0
while i < n:
    a = cards[i][0]
    b = cards[i][1]
    if a == b:
        taroScore += 1
        hanakoScore += 1
    else:
        if a < b:
            hanakoScore += 3
        else:
            taroScore += 3
    i += 1
print(taroScore, hanakoScore)