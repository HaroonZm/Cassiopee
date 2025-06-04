def func(args):
    s,a,b,c = args
    return s,int(a)*3+int(c)

n = input()
while True:
    a = map(func,[raw_input().split() for _ in xrange(n)])
    a.sort(key=lambda x:-x[1])
    print "\n".join(map(lambda (s,p):"{},{}".format(s,p),a))
    n = input()
    if n == 0:
        break
    print