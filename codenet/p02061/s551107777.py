#!/usr/bin/python3

Fact = [False for _ in range(10**5+1)]

def get_fact(m):
  global Fact
  ans = 1
  for i in range(2,int(m**0.5)+1):
    if m%i==0:
      ans *= i
      if i != m//i:
        ans *= m//i
      if ans >= m*2 or Fact[m//i]:
        return True
  return False

Fact_n = [0 for _ in range(10**5+1)]
for i in range(2,10**5+1):
  Fact[i] = get_fact(i)
  if Fact[i]:
    Fact_n[i] = Fact_n[i-1]+1
  else:
    Fact_n[i] = Fact_n[i-1]

Q = int(input())
ret = [0 for _ in range(Q)]
for q in range(Q):
  ret[q] = Fact_n[int(input())]

for q in ret:
  print(q)