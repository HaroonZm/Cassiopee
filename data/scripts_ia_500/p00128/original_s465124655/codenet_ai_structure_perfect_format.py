def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break


table = [
    "* = ****",
    " * =* ***",
    " * =** **",
    " * =*** *",
    " * =**** ",
    " *= ****",
    " *=* ***",
    " *=** **",
    " *=*** *",
    " *=**** "
]

N = list(get_input())
for l in range(len(N)):
    if l > 0:
        print("")
    num = int(N[l])
    ans = []
    for i in range(5):
        ans.append(table[num // 10**(4 - i)])
        num = num % 10**(4 - i)
    for i in range(8):
        for j in range(5):
            print(ans[j][i], end="")
        print("")