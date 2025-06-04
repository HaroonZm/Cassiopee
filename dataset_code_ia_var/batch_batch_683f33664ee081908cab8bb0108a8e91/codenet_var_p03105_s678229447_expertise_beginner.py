a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

money = b
utility = 0

if a > b:
    print(utility)
else:
    while utility < c and money - a >= 0:
        utility = utility + 1
        money = money - a
    print(utility)