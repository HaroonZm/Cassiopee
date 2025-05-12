n, W, H = [int(i) for i in input().split()]
X = [[int(i) for i in input().split()] for j in range(n)]

imos_h = [0] * (H + 2)
imos_w = [0] * (W + 2)

for x, y, w in X:
  imos_h[max(0, y - w)] += 1
  imos_h[min(H + 1, y + w)] -= 1
  imos_w[max(0, x - w)] += 1
  imos_w[min(W + 1, x + w)] -= 1
  
for h in range(H):
  imos_h[h + 1] += imos_h[h]
  
for w in range(W):
  imos_w[w + 1] += imos_w[w]

is_w = all(imos_w[w] >= 1 for w in range(W))
is_h = all(imos_h[h] >= 1 for h in range(H))

if is_h or is_w:
  print('Yes')
else:
  print('No')