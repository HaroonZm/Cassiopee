n=int(input())
tf=list(map(str,input().split()))
tf_r=tf[::-1]
while n!=1:
    if tf_r[-1]=="T" and tf_r[-2]=="F":
        del tf_r[-2:]
        tf_r.append("F")
        n-=1
    else:
        del tf_r[-2:]
        tf_r.append("T")
        n-=1
print(tf_r[0])