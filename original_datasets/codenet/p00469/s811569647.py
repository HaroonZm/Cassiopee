import itertools
while True:
    n=raw_input()
    if n=="0 0":break
    else:
        k=input()
    if k==0:break
    L=[raw_input() for i in range(int(n))]
    S=set()
    for t in itertools.permutations(L,k):
        S.add("".join(t))
    print len(S)