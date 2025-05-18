H, W, A, B = map(int, input().split())

for _ in range(B):
  print(''.join(['0'] * A + ['1'] * (W-A)))
for _ in range(H-B):
  print(''.join(['1'] * A + ['0'] * (W-A)))