def inpl(): return list(map(int, input().split()))

Sd = input()
T = input()

def match(L):
    for l, t in zip(L, T):
        if l == "?":
            continue
        else:
            if l != t:
                return False
            else:
                pass
    return True

res = []

for i in range(len(Sd)-len(T)+1)[::-1]:
    if match(Sd[i:i+len(T)]):
        res.append((Sd[:i] + T + Sd[i+len(T):]).replace("?", "a"))

if len(res):
    print(sorted(res)[0])
else:
    print("UNRESTORABLE")