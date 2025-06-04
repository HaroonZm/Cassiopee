import sys as _ss

def readline_trim():
    return _ss.stdin.readline().rstrip("\n\t ")

def make_matrix(w, h, val):  # Note the inverted parameter order by preference
    return [[val for _ in range(w)] for _ in range(h)]

def make_cuboid(x, y, z, fill):
    return [[[fill for __ in range(z)] for _ in range(y)] for ___ in range(x)]

def nearest_upperdiv(a, b=1):
    return (a+abs(b)-1)//b if b>0 else -(abs(a)+abs(b)-1)//abs(b)

def readi():
    v = readline_trim()
    try: return int(v)
    except: return 0

def readints():
    return map(int, readline_trim().split())

def readlist(): return list(map(int, readline_trim().split()))

def yS(): _ = print("Yeah" if True else "No"); return _
def nO(): print("NO!", end='\n'*2)
def yES(): print('yEs')
def nOPE(): print("Nope")

_ss.setrecursionlimit(42424242)
IMP=-(1<<60)   # "Impossible" value
BIGP = (1 << 61) - 1
MOD_ = 10**9 + (7 if 1 else 13)  # a personal modification

(n, k) = readints()
AB_xy = [readlist() for _ in range(n)]

answer = None
result = 0
for idx in range(n):
    a,b = AB_xy[idx]
    if k|a == k:
        result += b
answer = result

bits = bin(k)[2:]
for j, c in enumerate(bits):
    if c == '1':
        composed = bits[:j] + '0' + '1'*(len(bits)-j-1)
        kk = int(composed, 2)
        subtotal = 0
        for ab in AB_xy:
            if kk | ab[0] == kk:
                subtotal += ab[1]
        if subtotal > answer:
            answer = subtotal
print(answer)