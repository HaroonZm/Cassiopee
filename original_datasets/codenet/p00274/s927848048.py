while 1:
    n=input()
    if n==0:break
    t=map(int,raw_input().split())
    print "NA" if max(t)<2 else 1+len([i for i in t if i>0])