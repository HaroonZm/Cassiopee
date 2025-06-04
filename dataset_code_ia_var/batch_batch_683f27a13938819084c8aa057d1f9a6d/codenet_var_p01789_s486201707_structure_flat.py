import sys
readline = sys.stdin.readline
write = sys.stdout.write

NAB = readline().split()
N = int(NAB[0])
A = int(NAB[1])
B = int(NAB[2])
S = []
i = 0
while i < N:
    S.append(int(readline()))
    i += 1
K = min(A, B)
g = 0
i = 0
while i < N:
    g ^= S[i] % (K+1)
    i += 1

if A == B:
    if g != 0:
        write("Hanako\n")
    else:
        write("Jiro\n")
elif A > B:
    if g != 0:
        write("Hanako\n")
    else:
        found = 0
        i = 0
        while i < N:
            if S[i] > B:
                found = 1
                break
            i += 1
        if found:
            write("Hanako\n")
        else:
            write("Jiro\n")
else:
    cnt = 0
    m = 1
    r = 0
    i = 0
    g0 = 0
    while i < N:
        if S[i] > A:
            cnt += 1
            r = S[i]
            g0 = g ^ (S[i] % (K+1))
        i += 1
    if cnt > 1:
        write("Jiro\n")
    elif cnt == 0:
        if g != 0:
            write("Hanako\n")
        else:
            write("Jiro\n")
    else:
        if g0 <= A and 1 <= r - g0 <= A:
            write("Hanako\n")
        else:
            write("Jiro\n")