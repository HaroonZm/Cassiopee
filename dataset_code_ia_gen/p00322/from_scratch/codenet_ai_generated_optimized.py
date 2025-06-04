from sys import setrecursionlimit
setrecursionlimit(10**7)

A,B,C,D,E,F,G,H,I = map(int, input().split())

digits = [A,B,C,D,E,F,G,H,I]
used = [False]*10
for d in digits:
    if d != -1:
        used[d] = True

missing_indices = [i for i,d in enumerate(digits) if d == -1]
missing_digits = [i for i in range(1,10) if not used[i]]

count = 0
def dfs(pos):
    global count
    if pos == len(missing_indices):
        a,b,c,d,e,f,g,h,i = digits
        if a*100 + b*10 + c + d*100 + e*10 + f == g*100 + h*10 + i:
            count += 1
        return
    idx = missing_indices[pos]
    for md in missing_digits:
        if used[md]:
            continue
        digits[idx] = md
        used[md] = True
        dfs(pos+1)
        used[md] = False
        digits[idx] = -1

dfs(0)
print(count)