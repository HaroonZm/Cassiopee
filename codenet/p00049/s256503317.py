a = [0, 0, 0, 0]
aa = ["A", "B", "AB", "O"]
while True:
  try:
    s = input()
  except:
    break
  b, c = s.split(",")
  a[aa.index(c)] += 1
for i in range(4):
  print(a[i])