import sys
N = int(sys.stdin.readline())
sys.stdout.write("0:\n")
i = 1
while i < (1 << N):
    s = []
    j = 0
    while j < N:
        if i & (1 << j):
            s.append(str(j))
        j += 1
    sys.stdout.write(str(i) + ": " + " ".join(s) + "\n")
    i += 1