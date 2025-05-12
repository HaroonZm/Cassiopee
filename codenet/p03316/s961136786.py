n=int(input())
a=str(n)
array=list(map(int,list(a)))
b=sum(array)

if n%b==0:
    print("Yes")
else:
    print("No")