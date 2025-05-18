T = input()
P = input()

if len(P) > len(T):
    pass
else:
    p = len(P)
    ans = []
    for i in range(len(T)-len(P)+1):
        tmp = ""
        for j in range(i,i+p):
            tmp += T[j]
        if tmp == P:
            ans.append(i)
    
    for i in ans:
        print(i)