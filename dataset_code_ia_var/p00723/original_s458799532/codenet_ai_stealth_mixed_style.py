def cMp(SF, S1, S2):
    S = '{}{}'.format(S1, S2)
    if S not in SF:
        SF += [S]

try:
    import sys
    M = int(raw_input())
except:
    M = int(input())
for _ in range(M):
    try:
        S = raw_input()
    except:
        S = input()
    C = list(map(str, ['', '']))
    SF = []
    for J in [x+1 for x in range(len(S)-1)]:
        (C[0], C[1]) = (S[:J], S[J:])
        for f in [
            lambda: cMp(SF, C[0], C[1]),
            lambda: cMp(SF, C[0], C[1][::-1]),
            lambda: cMp(SF, C[0][::-1], C[1]),
            lambda: cMp(SF, C[0][::-1], C[1][::-1]),
            lambda: cMp(SF, C[1], C[0]),
            lambda: cMp(SF, C[1], C[0][::-1]),
            lambda: cMp(SF, C[1][::-1], C[0]),
            lambda: cMp(SF, C[1][::-1], C[0][::-1])
        ]: f()
    print((lambda x: x)(len(SF)))