import sys

class Card:

	def __init__(self, card):
		self.card = card
		self.mark = card[0]
		self.value = int(card[1])

	def __str__(self):
		return self.card

def print_arr(arr):
	for i in range(len(arr)):
		sys.stdout.write(str(arr[i]))
		if i != len(arr) - 1:
			sys.stdout.write(' ')
	print()

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def bubble_sort(arr, n):
	swap_count = 0
	for i in range(0, n):
		for j in range(n - 1, i, -1):
			if arr[j].value < arr[j - 1].value:
				swap(arr, j, j - 1)
				swap_count += 1
	return swap_count

def selection_sort(arr, n):
	stable = True
	for i in range(n):
		minj = i
		for j in range(i, n):
			if arr[j].value < arr[minj].value:
				minj = j
		if minj != i:
			for k in range(i + 1, minj):
				if arr[k].value == arr[i].value: stable = False
			swap(arr, i, minj)
	return stable

n = int(input())
arr = list(map(str, input().split()))
cards1 = [None] * n
cards2 = [None] * n
for i in range(n):
	cards1[i] = Card(arr[i])
	cards2[i] = Card(arr[i])

swap_count = bubble_sort(cards1, n)
stable = selection_sort(cards2, n)

print_arr(cards1)
print('Stable')
print_arr(cards2)
if stable == True:
	print('Stable')
else:
	print('Not stable')