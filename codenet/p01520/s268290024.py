n, t, e = map(int, input().split())
watch = list(map(int, input().split()))

ans = False
for w in range(n) :
    for i in range(e+1) :
        if (t+i) % watch[w] == 0 :
            ans = True
            break
        if (t-i) % watch[w] == 0 :
            ans = True
            break
    if ans == True :
        break

if ans == True :
    print(w+1)
else :
    print(-1)