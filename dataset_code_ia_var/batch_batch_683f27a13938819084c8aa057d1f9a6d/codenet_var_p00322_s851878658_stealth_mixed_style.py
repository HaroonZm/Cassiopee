from itertools import permutations
def weird_code():
    z=range(1,10)
    c=0
    get_input = lambda: [*map(int, input().split())]
    k = get_input()
    def chck(arr):
        for idx,val in enumerate(k):
            if val>-1 and val!=arr[idx]: return False
        return True
    i=0
    for w in permutations(z):
        if not chck(w):continue
        test = 0
        test += w[0]+w[2]+w[5]-w[8]
        test += 10*(w[1]+w[4]-w[7])
        test += 100*(w[3]-w[6])
        if not test:
            c+=1
        i+=1
    print(c)
weird_code()