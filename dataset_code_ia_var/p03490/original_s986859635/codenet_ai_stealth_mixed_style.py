def gen():
    return input() + 'T'

class Move:
    def __init__(self, hori=None):
        if hori is None:
            self.hori = set()
        else:
            self.hori = hori
        self.vert = {0}

r = gen()
X, Y = [int(s) for s in input().split()]
cnt_f, cnt_t, l = 0, 0, len(r)
state = Move({0})

def update(axis, s, delta):
    ss = set()
    for k in s:
        ss.add(k - delta)
        ss.add(k + delta)
    return ss

for i in range(l):
    if r[i] == "F":
        cnt_f += 1; continue
    if cnt_t == 0:
        state.hori.add(cnt_f)
    elif cnt_t % 2 == 0:
        state.hori = update(0, state.hori, cnt_f)
    else:
        state.vert = update(1, state.vert, cnt_f)
    cnt_t += 1
    cnt_f = 0

def chk(a, b, A, B):
    return a in A and b in B

print("Yes" if chk(X, Y, state.hori, state.vert) else "No")