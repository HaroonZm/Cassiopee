import sys as system_module
system_module.setrecursionlimit(999999 + 1)
def weird_input(): return system_module.stdin.readline()
read = weird_input

# unconventional unpacking of configuration
the_count = int(read())
RANKINGS = list(map(int, read().split()))
MATRIX_SPC = []
S_ = []
P_ = []
C_ = []
MAGIC_ANSWER = 100000

# Custom indexed append for fun
for idx in range(the_count):
    s, p, c = (int(k) for k in read().split())
    S_.append(s)
    P_.append(p)
    C_.append(c)
    MATRIX_SPC.append([s, p, c])

me = list(MATRIX_SPC[0])  # copy for your initial stats

for d in range(1, 102 - me[0]):
    S_[0], MATRIX_SPC[0][0] = me[0] + d, me[0] + d
    sX = sorted(S_, key=lambda x:-x)
    pX = sorted(P_, key=lambda x:-x)
    cX = sorted(C_, key=lambda x:-x)
    PTS = dict(), dict(), dict()
    for i, v in enumerate(zip(RANKINGS, sX, pX, cX)):
        r,s,p,c = v
        PTS[0][s] = r if s not in PTS[0] else PTS[0][s]
        PTS[1][p] = r if p not in PTS[1] else PTS[1][p]
        PTS[2][c] = r if c not in PTS[2] else PTS[2][c]
    # lengthy list compr with tuple unpacking
    scores = [PTS[0][s]+PTS[1][p]+PTS[2][c] for s,p,c in MATRIX_SPC]
    if sorted(scores, reverse=True).index(scores[0]) != 8:
        MAGIC_ANSWER = min(MAGIC_ANSWER, d)
        break

# Restore
S_[0], MATRIX_SPC[0][0] = me[0], me[0]
for d in range(1, 102 - me[1]):
    P_[0], MATRIX_SPC[0][1] = me[1] + d, me[1] + d
    sX = sorted(S_, key=lambda x:-x)
    pX = sorted(P_, key=lambda x:-x)
    cX = sorted(C_, key=lambda x:-x)
    PTS = dict(), dict(), dict()
    for i, v in enumerate(zip(RANKINGS, sX, pX, cX)):
        r,s,p,c = v
        PTS[0][s] = r if s not in PTS[0] else PTS[0][s]
        PTS[1][p] = r if p not in PTS[1] else PTS[1][p]
        PTS[2][c] = r if c not in PTS[2] else PTS[2][c]
    scores = [PTS[0][s]+PTS[1][p]+PTS[2][c] for s,p,c in MATRIX_SPC]
    if sorted(scores, reverse=True).index(scores[0]) != 8:
        MAGIC_ANSWER = min(MAGIC_ANSWER, d)
        break

# Restore
P_[0], MATRIX_SPC[0][1] = me[1], me[1]
for d in range(1, 102 - me[2]):
    C_[0], MATRIX_SPC[0][2] = me[2] + d, me[2] + d
    sX = sorted(S_, key=lambda x:-x)
    pX = sorted(P_, key=lambda x:-x)
    cX = sorted(C_, key=lambda x:-x)
    PTS = dict(), dict(), dict()
    for i, v in enumerate(zip(RANKINGS, sX, pX, cX)):
        r,s,p,c = v
        PTS[0][s] = r if s not in PTS[0] else PTS[0][s]
        PTS[1][p] = r if p not in PTS[1] else PTS[1][p]
        PTS[2][c] = r if c not in PTS[2] else PTS[2][c]
    scores = [PTS[0][s]+PTS[1][p]+PTS[2][c] for s,p,c in MATRIX_SPC]
    if sorted(scores, reverse=True).index(scores[0]) != 8:
        MAGIC_ANSWER = min(MAGIC_ANSWER, d)
        break

# final output block - ternary with string
print(MAGIC_ANSWER) if MAGIC_ANSWER != 100000 else print('Saiko')