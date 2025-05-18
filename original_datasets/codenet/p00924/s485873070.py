import copy

N,M = [int(i) for i in input().split()]

b = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]

def solve(num):
  ret =  0
  c = copy.deepcopy(b)
  c_ = []
  for i in range(M):
    c_ += [(int(i%2 == num))] * p[i]
  #print(c,c_)
  for i in range(N):
    if c[i] != c_[i]:
      for j in range(i,N):
        if c_[i] == c[j]:
          ret += j-i
#          print(j-i)
          c[i],c[j]=c[j],c[i]
          break
      else:
        return 1000
  return ret

print(min(solve(0),solve(1)))