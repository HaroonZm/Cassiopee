from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

A = input()
B = input()

A_root = [[-1] * 3 for i in range(1000)]
B_root = [[-1] * 3 for i in range(1000)]

class Source():
  def __init__(self, S):
    self.S = S
    self.pos = 0
   
  
def peek(S):
  return S.S[S.pos] if S.pos < len(S.S) else -1

def next(S):
  S.pos += 1

def tree(S, A, i):
  next(S)
  if peek(S) == ')':
    next(S)
    return -1
  c = i[0]
  i[0] += 1
  l = i[0] 
  left = tree(S, A, i)
  center = root(S, A)
  i[0] += 1
  r = i[0]
  right = tree(S, A, i)
  
  A[c] = [center, l, r]
  next(S)
  
def root(S, A):
  res = 0
  next(S)
  while peek(S) != ']':
    res = res * 10 + int(peek(S))
    next(S)
  next(S)
  
  return res
  
tree(Source('(' + A + ')'), A_root, [0])
tree(Source('(' + B + ')'), B_root, [0])

def f(i, j):
  if A_root[i][0] == -1 or B_root[j][0] == -1:
    return '()'
  center = '[' + str(A_root[i][0] + B_root[j][0]) + ']'
  return '(' + f(A_root[i][1], B_root[j][1]) + center + f(A_root[i][2], B_root[j][2]) + ')'

print(f(0, 0)[1:-1])