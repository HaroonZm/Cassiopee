def i1():
    return int(input())

def i2():
    return [int(i) for i in input().split()]

s = ["KIH", "B", "R", ""]
n = []
for i in range(1 << 5):
    c = ""
    for j in range(4):
        if (i >> j) & 1 == 1:
            c += "A"
        c += s[j]
    n.append(c)

ss = input()
if ss in n:
    print("YES")
else:
    print("NO")