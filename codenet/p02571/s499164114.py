s=input()
t=input()

l=[False]*len(s)
c=0
m=0
for x in range(len(s)-len(t)+1):
     c=0
     for y in range(len(t)):
          w=s[x:x+len(t)]
          if w[y]==t[y]:c+=1
     m=max(m,c)
print(len(t)-m)