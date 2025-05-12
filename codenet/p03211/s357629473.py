s=input()
n=len(s)
minnum=100000
for i in range(n-2):
    check=s[i:i+3]
    check=abs(753-int(check))
    minnum=min(minnum,check)
print(minnum)