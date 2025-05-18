import sys
from collections import defaultdict, deque
n = int(sys.stdin.readline().split()[0])
A = defaultdict(deque)
ans = []
for query in sys.stdin:
    if query[0] == '0':
        t, x = query[2:].split()
        A[t].append(x)
    elif query[0] == '1':
        if A[query[2:-1]]:
            ans.append(A[query[2:-1]][0] + '\n')
    else:
        if A[query[2:-1]]:
            A[query[2:-1]].popleft()
sys.stdout.writelines(ans)