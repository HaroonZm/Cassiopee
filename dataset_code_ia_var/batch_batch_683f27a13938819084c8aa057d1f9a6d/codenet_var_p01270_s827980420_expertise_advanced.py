import sys
import bisect

sys.setrecursionlimit(1 << 25)
inf = float('inf')
eps = 1e-10
mod = 10**9 + 7

DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI0(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(x): print(x, flush=True)

from typing import List

def process_instructions(n: int) -> List[int]:
    records = [[(c if i == 0 else int(c)) for i, c in enumerate(LS())] for _ in range(n)]
    result, allocated, deleted = [], [(0, -1)], set()
    for rec in records:
        op = rec[0]
        if op == 'R':
            idx = bisect.bisect_left(allocated, (rec[1], inf))
            last_id = allocated[idx-1][1]
            result.append(-1 if last_id in deleted else last_id)
        elif op == 'W':
            i, c = rec[1], rec[2]
            ai = 0
            while c > 0:
                pos, curr_id = allocated[ai]
                next_pos = allocated[ai + 1][0] if ai + 1 < len(allocated) else inf
                length = next_pos - pos
                if curr_id >= 0 and curr_id not in deleted:
                    ai += 1
                    continue
                take = min(c, length)
                if take < length:
                    allocated[ai:ai+1] = [(pos, i), (pos + take, curr_id)]
                    c = 0
                else:
                    allocated[ai] = (pos, i)
                    c -= take
                    if take == length:
                        ai += 1
                    else:
                        allocated.insert(ai + 1, (pos + take, curr_id))
                        c = 0
            # Merge intervals for efficiency (optional)
            merged = [allocated[0]]
            for p, id_ in allocated[1:]:
                if merged[-1][1] == id_:
                    merged[-1] = (merged[-1][0], id_)
                else:
                    merged.append((p, id_))
            allocated = merged
        else:  # 'D'
            deleted.add(rec[1])
    return result

def main():
    output = []
    readint = I
    while True:
        n = readint()
        if n == 0:
            break
        output.extend(process_instructions(n))
        output.append('')
    return '\n'.join(map(str, output))

print(main())