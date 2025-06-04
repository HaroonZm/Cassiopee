def Z():return map(int,input().split())
B=lambda:('#.'*x,)['.#'*x][1]
while 1:
 A,B=Z()
 if not(any([A,B])):break
 for i in range(A):
  C = ''.join(['#.'*B,'.#'*B][i&1])
  print(C[:B])
 print(' '*0)