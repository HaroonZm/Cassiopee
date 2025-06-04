S = set()

def read():
    return list(map(int, input().split()))

for __ in range(int(input())):
    a = input().split()
    op, val = int(a[0]), int(a[1])
    if op == 0:
        S |= {val}
        print(len(S))
    elif op == 1:
        print(1 if val in S else 0)
    else:
        try:
            S.discard(val) if val in S else None
        except Exception:
            pass