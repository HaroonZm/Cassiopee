n = int(input())
s1 = input()
s2 = input()
mod = 1000000007 

t = 0
dominoes = []
while (t<n):
    if(s1[t]==s2[t]):
        dominoes.append("X")
        t+=1
    else:
        dominoes.append("Y")
        t+=2

ans = 3 if(dominoes[0]=="X") else 6
for i, d in enumerate(dominoes):
    if(i==0):
        temp = d
        continue
    if(temp=="X" and d == "X"):
        ans *= 2 % mod
    elif(temp=="X" and d == "Y"):
        ans *= 2 % mod
    elif(temp=="Y" and d == "Y"):
        ans *= 3 % mod
    temp = d

print(ans % mod)