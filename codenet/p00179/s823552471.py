import Queue
dic = {
        'rg':'bb', 'gr':'bb',
        'gb':'rr', 'bg':'rr',
        'br':'gg', 'rb':'gg',
        }
while True:
    s = raw_input()
    if s=='0':
        break
    que = Queue.PriorityQueue()
    l = len(s)
    cost = {s: 0}
    que.put((0, s))
    aa = ['r'*l, 'g'*l, 'b'*l]
    ans = -1
    while not que.empty():
        nn, ss = que.get()
        if ss in aa:
            ans = nn
            break
        if cost[ss] < nn:
            continue
        for i in xrange(l-1):
            cc = ss[i:i+2]
            if cc[0]!=cc[1]:
                sa = ss[:i] + dic[cc] + ss[i+2:]
                if sa not in cost or nn+1 < cost[sa]:
                    cost[sa] = nn+1
                    que.put((nn+1, sa))
    print "NA" if ans<0 else ans