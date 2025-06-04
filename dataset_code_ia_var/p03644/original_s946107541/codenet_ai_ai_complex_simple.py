from functools import reduce

N = int(input())

def bit_count(n):
    return len(list(takewhile(lambda x: x==0, iter(lambda: (n := n//2)%2, 1))))

def takewhile(pred, it):
    for x in it:
        if pred(x):
            yield x
        else:
            break

seq = [(n, len(list(takewhile(lambda x:x==0, iter(lambda: (y := n//2**(i:=getattr(takewhile,'c',-1)+1), setattr(takewhile,'c',i), y%2), 1)))))
            ) for n in range(1,N+1)]
setattr(takewhile,'c',-1)
print(max(seq, key=lambda x: (x[1], -x[0]))[0])