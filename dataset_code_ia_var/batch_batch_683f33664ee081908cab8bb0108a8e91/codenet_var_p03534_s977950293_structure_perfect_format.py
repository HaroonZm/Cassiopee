from collections import Counter

def solve():
    S = raw_input()
    C = Counter(S)
    if len(S) == 1:
        return True
    A = sorted(C.items(), key=lambda x: -x[1])
    if len(A) == 2:
        return len(S) == 2
    if len(A) == 1:
        return False
    top1 = A[0][1]
    others = sum(a[1] for a in A[1:])
    return others >= (top1 - 1) * 2

print 'YES' if solve() else 'NO'