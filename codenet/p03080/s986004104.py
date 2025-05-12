N=int(input())
s=input()
num=0
for i in range(N):
    if s[i]=="R": num+=1

if num>N-num: print("Yes")
else: print("No")