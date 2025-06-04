import sys
import heapq
from collections import defaultdict

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    L = N + 20000
    E = []  # Employee list by position (may be None if removed)
    Q = []  # Waiting queue: max-heap (negated key)
    P = []  # Working group: min-heap
    R = {}  # Name -> (index, score)
    for i in range(N):
        s, a = readline().split()
        key = int(a) * L + i
        E.append(s)
        heapq.heappush(Q, (-key, i))
        R[s] = (i, key)
    P = [(-b, idx) for (b, idx) in heapq.nsmallest(N // 5, Q)]
    heapq.heapify(P)
    used = set(idx for _, idx in P)
    Q = [item for item in Q if item[1] not in used]
    heapq.heapify(Q)
    pn, qn, ln = len(P), len(Q), N
    cur = N

    def promote():
        nonlocal pn, qn
        while Q:
            c, k = heapq.heappop(Q)
            if E[k] is not None:
                heapq.heappush(P, (-c, k))
                pn += 1; qn -= 1
                return k
        return None

    def demote():
        nonlocal pn, qn
        while P:
            c, k = heapq.heappop(P)
            if E[k] is not None:
                heapq.heappush(Q, (-c, k))
                pn -= 1; qn += 1
                return k
        return None

    M = int(readline())
    for _ in range(M):
        tmp = readline().split()
        op = tmp[0]
        da = db = dk = None
        if op == "+":
            t, b = tmp[1], int(tmp[2]) * L + cur
            E.append(t)
            R[t] = (cur, b)
            ln += 1
            target_pn = ln // 5
            if pn < target_pn:
                heapq.heappush(P, (b, cur))
                pn += 1
                da = True
            elif -Q[0][0] < b:
                heapq.heappush(P, (b, cur))
                pn += 1
                # Demote worst in P
                k = demote()
                if k == cur:
                    da = False
                else:
                    db, dk = False, k
                pn += 1  # demote reduces pn, so this corrects it
                pn -= 1
            else:
                heapq.heappush(Q, (-b, cur))
                qn += 1
                da = False
            if da is not None:
                msg = f"{t} is {'working hard' if da else 'not working'} now.\n"
                write(msg)
            if db is not None:
                msg = f"{E[dk]} is {'working hard' if db else 'not working'} now.\n"
                write(msg)
            cur += 1
        else:  # remove
            t = tmp[1]
            j, b = R.get(t, (None, None))
            if j is None:
                continue
            E[j] = None
            ln -= 1
            target_pn = ln // 5
            if P and P[0][0] <= b and pn > 0:
                pn -= 1
                if pn < target_pn:
                    k = promote()
                    if k is not None:
                        db, dk = True, k
            else:
                qn -= 1
                if pn > target_pn:
                    k = demote()
                    if k is not None:
                        db, dk = False, k
            if db is not None:
                msg = f"{E[dk]} is {'working hard' if db else 'not working'} now.\n"
                write(msg)

solve()