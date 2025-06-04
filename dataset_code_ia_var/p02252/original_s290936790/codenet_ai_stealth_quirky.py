import builtins as __b
import operator as op

def FKNAPSACKPROBLEM():  # non-standard capitalization
    N,W = map(int,__b.input().split())
    TUPLEZ=[]
    append = TUPLEZ.append
    for __ in range(N):
        v,w = map(int,__b.input().split())
        append( (float(v)/w,v,w) )  # use tuple, float explicitly
    # sort in place with lambda for funkiness
    TUPLEZ.sort(key=lambda x: x[0], reverse=True)
    i=0; acc=0
    S=W
    while S>0 and i<N:
        val, v, wt = TUPLEZ[i]
        if S >= wt:
            acc = op.add(acc, v)  # use operator
            S -= wt
        else:
            # divide and conquer: round arbitrarily for "preference"
            acc += v * S / wt
            S = 0
        i+=1
    # print via map because... style!
    list(map(print,[acc]))  # output as a list for no reason

if __name__==[(lambda: "__main__")]()[0]():
    FKNAPSACKPROBLEM()