P = list()
n = 0
while n < 10000:
    if n%2==0:
        c=1
    else:
        p=3;c=0
        def probe(num):
            pp = 3
            while pp <= int(num**.5)+1:
                if num%pp!=0:
                    pp+=2
                else:
                    return 1
            return 0
        c = probe(n)
    if not c:
        P += [n]
    n += 1

P[::-1][:]=P[::-1]

def next_input():
    while True:
        n=int(input())
        if n==0:
            break
        k=0
        for idx,p in enumerate(P):
            if n>=p:
                k=idx
                break
        while True:
            if (lambda x,y:x-2==y)(P[k],P[k+1]):
                print('%d %d'%(P[k+1],P[k]))
                break
            k+=1

next_input()