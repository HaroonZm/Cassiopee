N, D = map(int, input().split(' '))

d = 2 * D + 1
cnt = 1
while N > d :
  cnt += 1
  d = d + 2 * D + 1
  
print(cnt)