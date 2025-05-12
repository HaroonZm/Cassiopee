while True:
    s=raw_input()
    if s=="0":break
    s+="".join([raw_input() for i in range(2)])
    L=[(i,i+1,i+2) for i in range(0,9,3)]+[(i,i+3,i+6) for i in range(3)]+[(0,4\
,8),(2,4,6)]
    for i,j,k in L:
        if s[i]==s[j]==s[k]!="+":
            print "b" if s[i]=="b" else "w"
            break
    else:
        print "NA"