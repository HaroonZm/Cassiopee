r="abcdefghijklmnopqrstuvwxyz"
import sys
def process():
 while True:
  try:
   n = int(input())
  except:
   break
  if not n:break
  def get_s(): return list(sys.stdin.readline().strip())
  s = get_s()
  ab=[]
  for _ in range(n):
   a,b=[int(x) for x in sys.stdin.readline().split()]
   ab.append((a,b))
  l=len(ab)
  i=0
  while l>i:
   (a,b)=ab[-(i+1)]
   d=abs(a-b)
   idx_a,idx_b=a-1,b-1
   temp=s[idx_b]
   s[idx_b]=r[(r.index(s[idx_a])+d)%26]
   s[idx_a]=r[(r.index(temp)+d)%26]
   i+=1
  print("".join(s))
process()