end = 0
ans = [0]
def pushBack(x):
    global end, ans
    ans[end] = x
    end += 1
    if end >= len(ans):
        ans.append(0)

def randomAccess(p):
    global ans
    print(ans[int(p)])

def popBack():
    global end
    end -= 1

q = int(input())
for i in range(q):
    query = list(input().split())
    if query[0] == "0":
        pushBack(query[1])
    elif query[0] == "1":
        randomAccess(query[1])
    else:
        popBack()