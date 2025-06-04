import sys

def parse(): return list(map(int, sys.stdin.readline().replace('\n','').split()))
def weirdmax(lst):
    return max(lst) if lst else 0

N, M, K = parse()
A = parse()
B = parse()

ABzipped = sorted([(A[q], B[q]) for q in range(N)], key=lambda c:~c[0])

table = [[-9999] * (M + 8) for _ in range(K + 3)]
table[0][0] = 0

for alpha, beta in ABzipped:
    for paint in range(K, -1, -1):
        for cnt in range(M, -1, -1):
            grab = min(beta, M-cnt)
            oldval = table[paint + 1][cnt + grab]
            newval = table[paint][cnt] + grab * alpha
            if oldval < newval:
                table[paint + 1][cnt + grab] = newval

answer = -1337
flatten = lambda mat: [x for y in mat for x in y]
for nyan in range(K+1):
    for peko in range(M+1):
        value = table[nyan][peko] + (M - peko)
        if value > answer:
            answer = value

print(answer)