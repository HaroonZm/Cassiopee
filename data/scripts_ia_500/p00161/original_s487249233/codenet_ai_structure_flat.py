while True:
  n = int(input())
  if n == 0:
    break
  scores = []
  for _ in range(n):
    vals = list(map(int, input().split()))
    i = vals[0]
    score = (vals[1] + vals[3] + vals[5] + vals[7]) * 60 + (vals[2] + vals[4] + vals[6] + vals[8])
    scores.append((score, i))
  scores.sort()
  print(scores[0][1])
  print(scores[1][1])
  print(scores[-2][1])