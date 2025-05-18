import copy

def can_empty(A):
    while 1:
        # Fall processing
        for w in xrange(W):
            seq = ("".join(A[h][w] for h in xrange(H))).replace(".","")
            seq += "."*(H-len(seq))
            for h in xrange(H):
                A[h][w] = seq[h]

        # Banish processing
        B = [[0]*W for _ in xrange(H)]
        for h in xrange(H):
            cnt = 1
            c = A[h][0]
            for w in xrange(1,W):
                if A[h][w] == c: cnt += 1
                else:
                    if cnt >= n and c != ".":
                        for wi in xrange(w-cnt,w):
                            B[h][wi] = 1
                    c,cnt = A[h][w],1
            if cnt >= n and c != ".":
                for wi in xrange(W-cnt,W):
                    B[h][wi] = 1
                c,cnt = A[h][w],1
        for w in xrange(W):
            cnt = 1
            c = A[0][w]
            for h in xrange(1,H):
                if A[h][w] == c: cnt += 1
                else:
                    if cnt >= n and c != ".":
                        for hi in xrange(h-cnt,h):
                            B[hi][w] = 1
                    c,cnt = A[h][w],1
            if cnt >= n and c != ".":
                for hi in xrange(H-cnt,H):
                    B[hi][w] = 1
                c,cnt = A[hi][w],1

        banish = False
        for h in xrange(H):
            for w in xrange(W):
                if B[h][w]:
                    A[h][w] = "."
                    banish = True
        if not banish: return False
        if A == goal: return True
        

# Entry point
H,W,n = map(int,raw_input().split())
_A = [list(raw_input()) for _ in xrange(H)][::-1]
goal = [["."]*W for _ in xrange(H)]
ans = False
for h in xrange(H):
    A = copy.deepcopy(_A)
    for w in xrange(W):
        if w < W-1:
            if A[h][w] == A[h][w+1]: continue
            A[h][w],A[h][w+1] = A[h][w+1],A[h][w]
            if can_empty(copy.deepcopy(A)):
                ans = True
                break
            A[h][w],A[h][w+1] = A[h][w+1],A[h][w]
    if ans: break
print "YES" if ans else "NO"