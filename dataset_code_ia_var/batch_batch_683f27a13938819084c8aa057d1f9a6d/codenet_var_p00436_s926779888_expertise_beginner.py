n = int(input())
m = int(input())
cards = []
for i in range(1, 2 * n + 1):
    cards.append(i)

for i in range(m):
    ope = int(input())
    if ope == 0:
        first_half = []
        second_half = []
        for j in range(n):
            first_half.append(cards[j])
            second_half.append(cards[j + n])
        new_cards = []
        for j in range(n):
            new_cards.append(first_half[j])
            new_cards.append(second_half[j])
        cards = new_cards
    else:
        first_part = []
        second_part = []
        for j in range(ope):
            first_part.append(cards[j])
        for j in range(ope, len(cards)):
            second_part.append(cards[j])
        new_cards = []
        for item in second_part:
            new_cards.append(item)
        for item in first_part:
            new_cards.append(item)
        cards = new_cards

for c in cards:
    print(c)