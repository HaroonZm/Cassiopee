class Card:
    def __init__(self, card):
        self.card = card
        self.mark = card[0]
        self.value = int(card[1])

    def __str__(self):
        return self.card

def print_arr(arr):
    for i in range(len(arr)):
        if i != 0:
            print(' ', end='')
        print(arr[i], end='')
    print()

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j].value < arr[j-1].value:
                swap(arr, j, j-1)

def selection_sort(arr, n):
    stable = True
    for i in range(n):
        minj = i
        for j in range(i, n):
            if arr[j].value < arr[minj].value:
                minj = j
        if minj != i:
            # Check if not stable before swapping
            if arr[minj].value == arr[i].value:
                stable = False
            swap(arr, i, minj)
    return stable

n = int(input())
arr = input().split()
cards1 = []
cards2 = []
for i in range(n):
    cards1.append(Card(arr[i]))
    cards2.append(Card(arr[i]))

bubble_sort(cards1, n)
stable = selection_sort(cards2, n)

print_arr(cards1)
print('Stable')
print_arr(cards2)
if stable:
    print('Stable')
else:
    print('Not stable')