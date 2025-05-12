while 1:
    N = int(raw_input())
    if N == 0: break
    a = raw_input().split()
    mn,mx = -10**10,10**10
    for i in range(1,N):
        if a[i-1] == a[i] == "x":
            print "none"
            break
        elif a[i-1] == "x":
            if (i+1)%2 == 0: mx = min(mx,int(a[i])-1)
            else           : mn = max(mn,int(a[i])+1)
        elif a[i] == "x":
            if (i+1)%2 == 0: mn = max(mn,int(a[i-1])+1)
            else           : mx = min(mx,int(a[i-1])-1)
        else:
            if   (i+1)%2 == 0 and int(a[i]) <= int(a[i-1]):
                print "none"
                break
            elif (i+1)%2 == 1 and int(a[i]) >= int(a[i-1]): 
                print "none"
                break
    else:
        if "x" not in a: 
            print "ambiguous"
        else:
            print mx if mn == mx else "ambiguous" if mn < mx else "none"