N = int(input())
b = list(map(int, input().split()))
op = []
mylist = []
for x in b:
    mylist.append(x)
f = True
while len(mylist) > 0:
    found = False
    i = len(mylist) - 1
    while i >= 0:
        if mylist[i] == i + 1:
            op.append(mylist[i])
            del mylist[i]
            found = True
            break
        i -= 1
    if not found:
        f = False
        break
if f:
    ans = []
    i = len(op) - 1
    while i >= 0:
        ans.append(op[i])
        i -= 1
    i = 0
    while i < len(ans):
        print(ans[i])
        i += 1
else:
    print(-1)