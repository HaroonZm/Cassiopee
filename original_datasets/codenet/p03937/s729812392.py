h,w = (int(i) for i in input().split())
a = []
ct = 0
for i in range(h):
  s = input()
  a.append(s)
  ct += s.count('#')
queue = [(0,0)]
check = []
if a[0][0] == '.':
 print('Impossible')
 exit()
while queue != []:
 i,j = queue[0]
 queue.pop(0)
 if not (i,j) in check:
  if i+1 < h:
   if a[i+1][j] =='#':
    queue.append((i+1,j))
  if j+1 < w: 
   if a[i][j+1] =='#':
    queue.append((i,j+1))
  check.append((i,j))
  if i+1 < h and j+1 < w: 
    if a[i+1][j] =='#' and  a[i][j+1] =='#':
      break
  if queue != []:
   if queue[0] == (h-1,w-1) and a[h-1][w-1] == '#':
     if h+w-1 == ct:
      print('Possible')
      exit()
print('Impossible')