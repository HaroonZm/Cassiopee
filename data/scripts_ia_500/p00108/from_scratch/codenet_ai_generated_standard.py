from collections import Counter
import sys

for line in sys.stdin:
    n=line.strip()
    if n=='0':
        break
    n=int(n)
    S=list(map(int,sys.stdin.readline().split()))
    count=0
    while True:
        freq=Counter(S)
        C=[freq[x] for x in S]
        count+=1
        if C==S:
            print(count-1)
            print(*C)
            break
        S=C[:]