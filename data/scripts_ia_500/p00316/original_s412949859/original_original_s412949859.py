n, m, k = map(int, input().split())
parent = [i for i in range(n)]
club = [-1 for _ in range(n)]

def find(x):
  if x == parent[x]:
    return x
  ret =  find(parent[x])
  parent[x] = ret
  return ret

for count in range(1, k + 1):
  t, a, b = map(int, input().split())
  a -= 1
  b -= 1
  if t == 1:
    p_a = find(a)
    p_b = find(b)
    c_a = club[p_a]
    c_b = club[p_b]
    if c_a >= 0 and c_b >= 0 and c_a != c_b:
      print(count)
      break
    if c_a < 0 and c_b >= 0:
      club[p_a] = c_b
    parent[p_b] = p_a

  else:
    p_a = find(a)
    if club[p_a] < 0:
      club[p_a] = b
    if club[p_a] >= 0 and club[p_a] != b:
      print(count)
      break
else:
  print(0)