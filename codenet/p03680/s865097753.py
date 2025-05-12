def solve(an,n):
  ret = 0
  nxt = 1
  while ret <= n+1:
    nxt = an[nxt-1]
    ret += 1
    if nxt == 2:
      return ret
  return -1

if __name__ == "__main__":
  n = int(input())
  An = [0 for i in range(n)]
  for i in range(n):
    An[i] = int(input())
  print(solve(An,n))