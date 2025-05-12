while True:
  n = int(input())
  if n == 0:break
  mes = list(input())
  mes = [ord(c) - ord("a") for c in mes]
  ablst = [tuple(map(int, input().split())) for _ in range(n)]
  ablst.reverse()
  for a, b in ablst:
    a -= 1
    b -= 1
    mes[b], mes[a] = (mes[a] + (b - a)) % 26, (mes[b] + (b - a)) % 26
  mes = [chr(i + ord("a")) for i in mes]
  print("".join(mes))