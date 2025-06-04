L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

from math import ceil

days_for_A = ceil(A / C)
days_for_B = ceil(B / D)

work_days = max(days_for_A, days_for_B)
play_days = L - work_days

print(play_days)