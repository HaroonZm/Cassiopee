import math

EPS = 1e-10

def eq(a, b):
  return (abs(a-b) < EPS)

def eqv(a, b):
  return (eq(a.real, b.real) and eq(a.imag, b.imag))

def cross(a, b):
  return a.real * b.imag - a.imag * b.real

def is_intersected_ls(a1, a2, b1, b2):
  return (cross(a2-a1, b1-a1) * cross(a2-a1, b2-a1) < EPS) and \
         (cross(b2-b1, a1-b1) * cross(b2-b1, a2-b1) < EPS)

def intersection_l(a1, a2, b1, b2):
  a = a2 - a1
  b = b2 - b1
  return a1 + a * cross(b, b1-a1) / cross(b, a)

while True:
  n = int(input())
  if n==0:
    break
  lines = []
  for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((complex(x1, y1), complex(x2, y2)))

  ans = 2
  for i in range(1, n):
    cross_point = []
    for j in range(0, i):
      l1, l2 = lines[i], lines[j]
      if is_intersected_ls(l1[0], l1[1], l2[0], l2[1]):
        p = intersection_l(l1[0], l1[1], l2[0], l2[1])
        if -100+EPS<=p.real<=100-EPS and -100+EPS<=p.imag<=100-EPS:
          cross_point.append(p)
    cnt = min(len(cross_point), 1)
    for i in range(1, len(cross_point)):
      flag = 0
      for j in range(0, i):
        if eqv(cross_point[i], cross_point[j]):
          flag = 1
      if not flag:
        cnt+=1
    ans += 1+cnt
  
  print(ans)