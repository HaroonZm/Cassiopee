n=input()
if n==2:print-1;exit(0)
r=range(n-1)
A=[[`1+(i+j+2)%n`for j in r]for i in[-1]+r]
i=n/2-1
if i:
 for j in range(i+1):A[j][i]=`j+i+1`;A[j][i-n]=`j+i+2`
print"\n".join(" ".join(e)for e in A)