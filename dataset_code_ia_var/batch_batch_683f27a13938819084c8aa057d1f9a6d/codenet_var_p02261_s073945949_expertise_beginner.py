def bubble_sort(cards, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(cards[j][1]) < int(cards[j-1][1]):
                temp = cards[j]
                cards[j] = cards[j-1]
                cards[j-1] = temp

def selection_sort(cards, n):
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if int(cards[j][1]) < int(cards[min_index][1]):
                min_index = j
        temp = cards[i]
        cards[i] = cards[min_index]
        cards[min_index] = temp

n = int(input())
cards = input().split()
original_cards = cards[:]
bubble_sort(cards, n)
print(" ".join(cards))
print("Stable")
selection_cards = original_cards[:]
selection_sort(selection_cards, n)
print(" ".join(selection_cards))
if cards == selection_cards:
    print("Stable")
else:
    print("Not stable")