s=input()
cnt=len(s)//2
i=0
if len(s)%2:
    while cnt+i<len(s) and s[cnt-i]==s[cnt+i]==s[cnt]:
        i+=1
else:
    while cnt+i<len(s) and s[cnt-i-1]==s[cnt+i]==s[cnt]:
        i+=1
print(cnt+i)