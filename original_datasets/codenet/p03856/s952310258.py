S=input().strip()
ws=['dream','dreamer','erase','eraser']
while True:
  change = False
  for w in ws:
    if len(w) <= len(S) and S[-len(w):] == w:
      S = S[:-len(w)]
      change = True
  if not change:
    break
print("YES" if len(S) == 0 else "NO")