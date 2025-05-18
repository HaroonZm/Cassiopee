c=input()
num=map(int,raw_input().split())
num.sort()
s=""
for i in num:
    s+=" "+str(i)
print s[1:]