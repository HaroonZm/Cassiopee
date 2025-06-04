import sys
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N_K_line = sys.stdin.readline().strip()
while N_K_line == '':
    N_K_line = sys.stdin.readline().strip()
N_K = list(map(int, N_K_line.split()))
N = N_K[0]
K = N_K[1]
AB = []
count = 0
while count < N:
    ab_line = sys.stdin.readline().strip()
    if ab_line == '':
        continue
    ab = list(map(int, ab_line.split()))
    AB.append(ab)
    count += 1

ans = 0
i = 0
while i < N:
    if (K | AB[i][0]) == K:
        ans += AB[i][1]
    i += 1

Kb = format(K, 'b')
length = len(Kb)
i = 0
while i < length:
    b = Kb[i]
    if b == '1':
        Kb2 = Kb[:i] + '0' + '1' * (length - i - 1)
        k = int(Kb2, 2)
        sm = 0
        j = 0
        while j < N:
            if (k | AB[j][0]) == k:
                sm += AB[j][1]
            j += 1
        if sm > ans:
            ans = sm
    i += 1

print(ans)