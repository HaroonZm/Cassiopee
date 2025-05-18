n=list(input())
a=[] 
b=[] 
c=0
for i in range(len(n)):
    if n[i]=="," or n[i]=="." or n[i]==" ":
        if 6>=c>=3:
            b=b+a+[" "]
        a.clear()
        c=0
    else:
        a.append(n[i])
        c+=1
del b[-1]
for i in range(len(b)):
   print(b[i],end="")
print()