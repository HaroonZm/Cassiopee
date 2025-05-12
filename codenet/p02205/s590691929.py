N = int(input())
A, B = map(int, input().split())

ret = [(A, B)]
for i in range(1, 12) :
  if i % 2 == 0 :
    B = A + B
  else :
    A = A - B
  ret.append((A, B))
  
print(*ret[N % 12])