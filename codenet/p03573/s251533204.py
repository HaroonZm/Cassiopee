num = [int(x) for x in input().split()]
for i in num:
    if num.count(i) == 1:
        print(i)