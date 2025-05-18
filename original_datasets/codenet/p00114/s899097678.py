from math import gcd

def get_loop(a, m):
  count = 1
  acc = a
  while acc != 1:
    count += 1
    acc *= a
    acc %= m
  return count

while True:
  a1, m1, a2, m2, a3, m3 = map(int, input().split())
  if not a1:
    break
  loop_a = get_loop(a1, m1)
  loop_b = get_loop(a2, m2)
  loop_c = get_loop(a3, m3)
  loop_ab = loop_a * loop_b // gcd(loop_a, loop_b)
  loop_abc = loop_ab * loop_c // gcd(loop_ab, loop_c)
  print(loop_abc)