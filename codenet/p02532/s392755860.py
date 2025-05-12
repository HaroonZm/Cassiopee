p = [[] for i in range(input())]
while True:
  v = raw_input().split()
  if v[0] == 'quit':
    break
  elif v[0] == 'push':
    p[int(v[1]) - 1].append(v[2])
  elif v[0] == 'move':
    p[int(v[2]) - 1].append(p[int(v[1]) - 1].pop())
  elif v[0] == 'pop':
    print(p[int(v[1]) - 1].pop())