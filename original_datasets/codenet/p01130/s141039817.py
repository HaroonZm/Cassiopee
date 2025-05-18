import sys

def warshall(n, matrix):
  for i in xrange(n):
    matrix[i][i] = 0
  for i in xrange(n):
    for j in xrange(n):
      for k in xrange(n):
        matrix[j][k] = min(matrix[j][k], matrix[j][i]+matrix[i][k])
  return matrix

while True:
  n,m,s,g1,g2 = map(int, raw_input().split())
  if n==m==s==g1==g2==0:
    break
  matrix = [[10**10] * n for i in xrange(n)]
  for i in xrange(m):
    b1,b2,c = map(int, raw_input().split())
    matrix[b1-1][b2-1] = c
  costs = warshall(n, matrix)
  mincost = 10**10
  for i in xrange(n):
    mincost = min(mincost, costs[s-1][i]+costs[i][g1-1]+costs[i][g2-1])
  print mincost