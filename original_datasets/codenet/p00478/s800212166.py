x = input()
n = int(input())
ans = 0
for i in range(n) :
    y = list(input())
    for j in range(len(x)-1) :
        y.append(y[j])
    y = "".join(y)
    if x in y :
        ans += 1
print(ans)