s=input()
a=[]
d=[]
sum=0
for i,line in enumerate(s):
    if line == "\\":
        d.append(i)
    elif line == "/" and d:
        j=d.pop()
        a_tmp=i-j
        sum+=a_tmp
        while a and a[-1][0] > j:
            a_tmp += a.pop()[1]
        a.append([j,a_tmp])
 
print(sum)
print(len(a),*[s for i,s in a])