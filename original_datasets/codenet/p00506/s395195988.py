input()
s=list(map(int,input().split()))
a,b=s[:2]
while b:a,b=b,a%b
if len(s)-2:
 b=s[2]
 while b:a,b=b,a%b
[print(x)for x in range(1,a+1)if a%x==0]