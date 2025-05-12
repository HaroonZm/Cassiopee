import sys
range = xrange
input = raw_input
 
def main():
  n = int(input())
  A = [int(x) for x in input().split()]
  B = [int(x) for x in input().split()]
 
  DP = [0]*(n+1)
  DP[n] = n
  for j in range(3):
      sell = A[j]
      extra = B[j] - sell
      if extra > 0:
          for i in reversed(range(len(DP) - sell)):
              DP[i] = max(DP[i], DP[i + sell] + extra)
  n = max(DP)
  A,B = B,A
 
  DP = [0]*(n+1)
  DP[n] = n
  for j in range(3):
      sell = A[j]
      extra = B[j] - sell
      if extra > 0:
          for i in reversed(range(len(DP) - sell)):
              DP[i] = max(DP[i], DP[i + sell] + extra) 
  print(max(DP))
 
main()