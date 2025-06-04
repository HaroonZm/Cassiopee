C = [0] * 6
n = int(raw_input())
i = 0
while i < n:
  s = raw_input()
  j = 0
  a = 0
  while s[j] != '.':
    a = a*10 + int(s[j])
    j += 1
  # skip the dot and parse b, but it's unused
  j += 1
  while j < len(s) and s[j].isdigit():
    j += 1
  idx = (a-160)//5
  if idx < 0:
    idx = 0
  if idx > 5:
    idx = 5
  C[idx] += 1
  i += 1
k = 0
while k < 6:
  print '%d:%s' % (k+1, '*'*C[k])
  k += 1