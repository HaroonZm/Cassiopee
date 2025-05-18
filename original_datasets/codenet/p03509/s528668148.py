n, p = map(int, input().split())
w, b = [], []
for _ in range(n):
    ww, bb = map(int, input().split())
    w.append(ww)
    b.append(bb)

s = []
for ww, bb in zip(w, b):
    s.append((100 - p) * ww + p * bb)
s.sort(reverse=True)

score = -sum(b) * p

cnt = 0
while score < 0:
    score += s[cnt]
    cnt += 1
print(cnt)

# (100-p)*w-p*b>=0