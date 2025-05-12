input()
L = [int(x) for x in input().split()]
input()
Q = [int(x) for x in input().split()]

for i in sorted(set(L)|set(Q)):
    print(i)