ls = sorted(list(map(int, input().split())),reverse=True)
if ls[0] == sum(ls[1:]):
    print("Yes")
else:
    print("No")