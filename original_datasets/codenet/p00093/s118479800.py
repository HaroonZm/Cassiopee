flag=False
while True:
    a,b=map(int,raw_input().split())
    if (a,b)==(0,0):
        break
    if not flag:
        flag=True
    else:
        print
    ans=[y for y in xrange(a,b+1) if (y%4==0 and not y%100==0) or y%400==0]
    if not ans:
        print "NA"
    else:
        print "\n".join(map(str,ans))