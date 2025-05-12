# solution
data = str(input())
n = len(data)

c = [1] * n
for i in range(n):
  if data[i] == 'R' and data[i+1] == 'R':
    c[i+2] += c[i]
    c[i] = 0

for i in range(n-1, -1, -1):
  if data[i] == 'L' and data[i-1] == 'L':
    c[i-2] += c[i]
    c[i] = 0

print(' '.join(map(str, c)))