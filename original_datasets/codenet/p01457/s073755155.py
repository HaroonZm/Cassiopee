cnt = 0
for loop in xrange(int(raw_input())):
    a,c,n = raw_input().split()
    n = int(n)
    cnt += n if c == "(" else -n
    print "Yes" if cnt == 0 else "No"