def F(N):
  result = 2*N+1
  index = 1
  def extra(k):
      s = 1 + ((N - k*k)//k)*2
      return s
  while True:
      if index*index > N:
          break
      result = result + extra(index)
      index += 1
  return result

from sys import stdin
def read():
    return map(int,stdin)

try:
    while True:
        n = int(input())
        if n==0:
            break
        comp = lambda x: 8*F(x//2-1) + 8*x
        print(comp(n))
except:
    pass