s=input()
t=input()
sm=0
for i in range(len(s)):
    if s[i]!=t[i]:
        sm+=1
print(sm)