a=[]
try:
  while True:
    a.append(int(input()))
except EOFError:
  pass
counts = [0]*101
for n in a:
  counts[n] += 1
max_count = max(counts)
for n in range(len(a)):
  if counts[n] == max_count:
    print(n)