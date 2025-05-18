n = int(input())

s = m = int(input())

for i in range(n):
  in_car, out_car = map(int, input().split())
  
  m += in_car - out_car
  
  if m < 0:
    s = 0
    break
  else:
    s = max(s, m)

print(s)