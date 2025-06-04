table = [
    "* = ****",
    "* =* ***",
    "* =** **",
    "* =*** *",
    "* =**** ",
    " *= ****",
    " *=* ***",
    " *=** **",
    " *=*** *",
    " *=**** "
]

N = []
while True:
    try:
        N.append(''.join(input()))
    except EOFError:
        break

for l in range(len(N)):
    if l > 0:
        print("")

    num = int(N[l])
    ans = []
    v = num
    t = [10000, 1000, 100, 10, 1]
    for i in range(5):
        d = v // t[i]
        ans.append(table[d])
        v = v % t[i]
    for i in range(8):
        for j in range(5):
            print(ans[j][i], end="")
        print("")