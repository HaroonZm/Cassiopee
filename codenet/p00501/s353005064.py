#C
N = int(input())
name = str(input())
nlen = len(name)
S = [list(str(input())) for i in range(N)]

ans = 0
for i in range(N):
    s = S[i]
    
    flag = 0
    slen = len(s)
    for j in range(1,101):
        wide = j
        for k in range(slen):
            now = k
            kari = ""
            for l in range(nlen):
                if now < slen:
                    kari+=s[now]
                else:
                    break
                now+=wide
            if kari == name:
                flag = 1
                break
        if flag == 1:
            break
            
    if flag == 1:
        ans+=1

print(ans)