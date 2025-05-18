count = range(1000001) 
for i in xrange(2, 500001):
    for n in xrange(i*2, 1000001, i):
        count[n] -= (count[i] - 1) 
 
count[1] = 2
for i in xrange(2, 1000001):
    count[i] += count[i-1]

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    print count[n] - n + 1