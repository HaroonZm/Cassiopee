import sys
while 1:
    s=raw_input().rstrip().split(" ")
    h=int(s[0])
    w=int(s[1])
    if h==0 and w==0:
	break;
    for i in range(0,h):
	for j in range (0,w):
            if (i==0 or i%2==0) and (j==0 or j%2==0):
		sys.stdout.write('#')
            elif (i==0 or i%2==0) and j%2!=0:
                sys.stdout.write('.')
            elif i%2!=0 and (j==0 or j%2==0):
		sys.stdout.write('.')
            elif i%2!=0 and j%2!=0:
                sys.stdout.write('#')
        print ''
    print ''