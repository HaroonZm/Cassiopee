N = input()
a = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
R = [w for a, w in zip(a, w) if a == 0]
L = [w for a, w in zip(a, w) if a == 1]
if R and L:
    print(min(R) + min(L))
else:
    print(0)