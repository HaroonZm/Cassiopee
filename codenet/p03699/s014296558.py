n=int(input())
s=[int(input()) for _ in range(n)]
ss=sorted(s)
if sum(s) % 10 ==0:
    for i in range(len(ss)):
        if ss[i] %10 ==0:
            continue
        else:
            ss[i]=0
            break
    else:
        print(0)
        exit(0)
print(sum(ss))