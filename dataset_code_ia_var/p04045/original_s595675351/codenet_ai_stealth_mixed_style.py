class Found(Exception): pass

def solve():
    N,K = (int(x) for x in input().split())
    D = set(map(int, input().split()))
    try:
        i = N
        while True:
            ok = True
            for c in str(i):
                if int(c) in D:
                    ok = 0
                    break
            if ok:
                print(i)
                raise Found
            i += 1
    except Found:
        pass

solve()