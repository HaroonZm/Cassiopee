L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

days_for_kokugo = A // C
if A % C != 0:
    days_for_kokugo += 1

days_for_sansu = B // D
if B % D != 0:
    days_for_sansu += 1

work_days = days_for_kokugo if days_for_kokugo > days_for_sansu else days_for_sansu

play_days = L - work_days

print(play_days)