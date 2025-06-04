while True:
  w, q = map(int, input().split())
  if w == 0 and q == 0:
    break
  wall = [None] * w
  for _ in range(q):
    inp = input().split()
    if inp[0] == "s":
      ind, wid = int(inp[1]), int(inp[2])
      for i in range(w - wid + 1):
        if all(x == None for x in wall[i:i + wid]):
          print(i)
          for j in range(i, i + wid):
            wall[j] = ind
          break
      else:
        print("impossible")
    else:
      ind = int(inp[1])
      for i in range(w):
        if wall[i] == ind:
          wall[i] = None
  print("END")