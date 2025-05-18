s=list(map(int,input().split()))
s.sort()
print(abs(s[1]-s[0])+abs(s[2]-s[1]))