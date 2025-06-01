A=range(14)
B=range(3,11)
M=["0"*14 for i in A]
z="000"
N=range(input())
for i in N:
    s=raw_input()
    for j in B:
        M[j]=z+raw_input()+z
    x=input()+2
    y=input()+2
    s=M[y]
    if s[x]!="0":
        M[y]=s[:x]+"0"+s[x+1:]
        R=[-3,-2,-1,1,2,3]
        for e in R:
            s=M[y]
            if 0<=x+e<14 and s[x+e]!="0":
                M[y]=s[:x+e]+"0"+s[x+e+1:]
                for ee in R:
                    if 0<=x+e+ee<14:
                        s2=M[y]
                        if s2[x+e+ee]!="0":
                            M[y]=s2[:x+e+ee]+"0"+s2[x+e+ee+1:]
            s2=M[y+e] if 0<=y+e<14 else None
            if s2 != None and 0<=x<14 and s2[x]!="0":
                M[y+e]=s2[:x]+"0"+s2[x+1:]
                for ee in R:
                    if 0<=x+ee<14 and 0<=y+e<14:
                        s3=M[y+e]
                        if s3[x+ee]!="0":
                            M[y+e]=s3[:x+ee]+"0"+s3[x+ee+1:]
    print "Data %d:" %(i+1)
    for j in B:
        print M[j][3:-3]