while 1:
	n=input()
	if n==0:break
	t=map(int,raw_input().split())
	if max(t)<2:
		print "NA"
		continue
	print 1+len([i for i in t if i>0])