dic = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
while True:
  sa = list(map(int, input().split()))
  if sa == [0, 0]:
    break
  lst = [sum(sa)]
  for _ in range(4):
    lst.append(sum(map(int, input().split())))
  print(dic[lst.index(max(lst))], max(lst))