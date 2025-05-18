def main():
  n = int(input()) + 1
  a = [int(x) for x in input().split()]
  q = [0] * n
  for i in range(n):
    q[i] = (q[i - 1] - a[i - 1]) * 2 if i != 0 else 1
    # print(q[i])
    if q[i] <= 0:
      print(-1)
      return
  
  if q[n - 1] < a[n - 1]:
    print(-1)
    return
  q[n - 1] = a[n - 1]
  s = q[n - 1]
  # print('--')
  # print(q[n - 1])
  for i in range(n - 2, -1, -1):
    q[i] = min(q[i], q[i + 1] + a[i])
    if q[i] == 0:
      print(-1)
      return
    # print(q[i])
    s += q[i]
  print(s)

main()