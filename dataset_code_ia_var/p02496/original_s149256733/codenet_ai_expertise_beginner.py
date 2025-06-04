n = int(input())
cards = []
for i in range(4):
    cards.append([False]*13)

for i in range(n):
    s = input().split()
    mark = s[0]
    num = int(s[1]) - 1

    if mark == "S":
        cards[0][num] = True
    elif mark == "H":
        cards[1][num] = True
    elif mark == "C":
        cards[2][num] = True
    elif mark == "D":
        cards[3][num] = True

suits = ["S", "H", "C", "D"]

for i in range(4):
    for j in range(13):
        if not cards[i][j]:
            print(suits[i], j+1)