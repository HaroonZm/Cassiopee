A,B,C = map(int,input().split())
money = B
utility = 0
if A > B:
    print(utility)
else:
    while (utility < C) and (money-A >= 0):
        utility += 1
        money -= A
    print(utility)