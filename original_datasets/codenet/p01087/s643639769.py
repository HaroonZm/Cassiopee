def solve(x,a,ind):
#    print(x,a,ind)
    if "0" <= a[0][ind] <="9":
        return int(a[0][ind])

    if a[0][ind] =="+":
        i = j= 1
        su = 0
        while(i < x):
            if a[i][ind+1] == "+" or a[i][ind+1]=="*":
                j+=1
                while j < x and a[j][ind +1]==".":
                    j += 1
                su += solve(j-i,a[i:j],ind+1)
                i = j
                j = j
            else:
                su += int(a[j][ind+1])
                i += 1
                j += 1

#        print(x,a,ind,su)
        return su

    if a[0][ind] =="*":
        i = j= 1
        su = 1
        while(i < x):
            if a[i][ind+1] == "+" or a[i][ind+1]=="*":
                j+=1
                while j<x and a[j][ind +1]==".":
                    j += 1
                su *= solve(j-i,a[i:j],ind+1)
                i = j
                j = j
            else:
                su *= int(a[j][ind+1])
                i += 1
                j += 1
 #       print(x,a,ind,su)
        return su

while(1):
    n  = int(input())
    if n >0:
        a = [input() for i in range(n)]
        print(solve(n,a,0))
    else:
        break