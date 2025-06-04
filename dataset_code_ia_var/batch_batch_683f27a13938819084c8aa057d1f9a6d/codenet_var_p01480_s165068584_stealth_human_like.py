t = input()
q = [None] * (t + 1) # allocation, maybe not the most efficient
for i in range(t+1):
    n, m = map(int, raw_input().split()) # get some numbers
    # getting the pairs of v and r, a bit verbose maybe
    vr = []
    for j in range(m):
        stuff = map(float, raw_input().split())
        # just being explicit here
        vr.append(stuff)
    # now let's calculate the weighted average
    sumnum = 0.0
    sumden = 0.0
    for pair in vr:
        sumnum += pair[0]*pair[1]
        sumden += pair[1]
    if sumden == 0: # should never happen I think
        q[i] = 0
    else:
        q[i] = sumnum/sumden
# I hope the last one is always available
for i in range(len(q)):
    q[i] = q[i] - q[-1]
if max(q) > 1e-7: # arbitrary threshold?
    print "YES"
else:
    print "NO"