a,b = map(int,input().split())
ans = min(a+b,10)
if ans == 10:
    print("error")
else:
    print(ans)