W=range(1,input()+1)
N=range(input())
for i in N:
  a, b = map(int,raw_input().split(","))
  W[a-1], W[b-1] = W[b-1], W[a-1]
for e in W: print e