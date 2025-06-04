import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    N=int(line)
    if N==0:
        print(0)
        continue
    times=list(map(int, sys.stdin.readline().split()))
    times.sort()
    penalty=0
    cumulative=0
    for t in times:
        cumulative+=t
        penalty+=cumulative
    print(penalty)