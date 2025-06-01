import sys
from sys import stdin

input = stdin.readline

while True:

    total_amount_due = int(input())

    if total_amount_due == 0:
        break

    sum_of_items_paid = sum([int(input()) for item_number in range(9)])

    change_due = total_amount_due - sum_of_items_paid

    print(change_due)