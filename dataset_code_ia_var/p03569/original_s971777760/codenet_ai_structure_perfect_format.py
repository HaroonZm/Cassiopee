s = list(input())
X = []
hoge = 0
for i in range(len(s)):
    if s[i] == 'x':
        hoge += 1
    else:
        X.append(hoge)
        X.append(s[i])
        hoge = 0
X.append(hoge)
ans = 0
for i in range(len(X)//2):
    if i % 2 == 0:
        ans += abs(X[i] - X[-i-1])
    elif X[i] != X[-i-1]:
        print(-1)
        exit()
print(ans)