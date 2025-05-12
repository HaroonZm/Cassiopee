while True:
    n=input()
    if n==0:break
    L=[map(int,raw_input().split()) for i in range(n)]
    S=set([min(i) for i in L])
    for t in [[i[j] for i in L] for j in range(n)]:
	maxInt=max(t)
        if maxInt in S:
            print maxInt
            break
    else:
	print 0