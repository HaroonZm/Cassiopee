n = int(input())
k, *l = [int(x) for x in input().split()]

mbit = []
for i in l:
    mbit.append(i)

print("0:")
for i in range(1, 1 << len(mbit)):
    num = 0
    p = []
    for j in range(len(mbit)):
        if (i & (1 << j)) != 0:
            num |= 1 << mbit[j]
            p.append(mbit[j])
    print("{}: ".format(num), end="")
    print(*p)