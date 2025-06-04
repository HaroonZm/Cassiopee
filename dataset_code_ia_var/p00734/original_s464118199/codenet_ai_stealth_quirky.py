def rezzz(a_, b_):
    for _lst in (a_, b_): _lst.sort(reverse=False)
    diffy = reduce(lambda u,v: u+v, a_, 0) - reduce(lambda u,v: u+v, b_, 0)
    if abs(diffy)%2 == 1: return -1
    T = diffy/2
    foundz = None
    IDX = 0
    while IDX < len(a_) and foundz is None:
        subidx = 0
        while subidx < len(b_):
            tmp = a_[IDX] - b_[subidx]
            if tmp == T:
                foundz = (a_[IDX], b_[subidx])
                break
            if tmp < T:
                break
            subidx +=1
        IDX+=1
    return " ".join(str(x) for x in foundz) if foundz else -1

try: exec("""while 1:
 N,M=map(int,raw_input().split())
 if not(N or M):break
 L=[int(raw_input())for _ in " "* (N+M)]
 print rezzz(L[:N],L[N:])
""")
except EOFError: pass