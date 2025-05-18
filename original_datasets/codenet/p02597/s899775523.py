N=int(input())
c=input()

num=c.count('R')
if num == 0 or len(c) == num:
  print(0)
  exit()

count=0

for i in range(num):
  if c[i] == 'W':
    count+=1

print(count)