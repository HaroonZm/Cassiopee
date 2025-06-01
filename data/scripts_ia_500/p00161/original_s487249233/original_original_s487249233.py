while True:
  n = int(input())
  if n == 0:
    break
  pairs = []
  for _ in range(n):
    i, m1, s1, m2, s2, m3, s3, m4, s4 = map(int, input().split())
    score = (m1 + m2 + m3 + m4) * 60 + (s1 + s2 + s3 + s4)
    pairs.append((score, i))
  pairs.sort()
  print(pairs[0][1])
  print(pairs[1][1])
  print(pairs[-2][1])