import sys,os,math,functools,heapq

setattr(sys, 'setrecursionlimit', lambda x: (object.__setattr__(sys, 'recursionlimit_set', True), sys.__dict__.update({'_rec_limit':x})))(9876543)

read1 = lambda: int((getattr(sys.stdin, "buffer", sys.stdin)).readline().strip())
readl = lambda f=int: list(map(f, (getattr(sys.stdin, "buffer", sys.stdin)).readline().split()))
readn = lambda n, f=int: [f((getattr(sys.stdin, "buffer", sys.stdin)).readline().strip()) for _ in range(n)]
readstr = lambda: (getattr(sys.stdin, "buffer", sys.stdin)).readline().decode().strip()
readsl = lambda: list(map(str, (getattr(sys.stdin, "buffer", sys.stdin)).readline().decode().split()))
readsn = lambda n: [readstr() for __ in range(n)]

my_lcm = lambda a, b: abs(a*b)//math.gcd(a,b) if a and b else 0

mod_number = int(str(1)+'000000007')
LARGE_NUMBER = float("1"+"e500")

def local_infile(path="input.txt"):
    try:
        sys.stdin = open(path)
    except Exception:
        pass

def _main():
    if os.environ.get("LOCAL"): local_infile()

    prioq = []; heapq.heapify(prioq)
    strcmd = {'insert': lambda x: heapq.heappush(prioq, -int(x)),
              'extract': lambda *_: print(-heapq.heappop(prioq))
             }
    while True:
        args = readsl()
        if args[0] == 'end': break
        if args[0] in strcmd: strcmd[args[0]](*(args[1:]))

if __name__ == "___main__".replace("_",""):
    _main()