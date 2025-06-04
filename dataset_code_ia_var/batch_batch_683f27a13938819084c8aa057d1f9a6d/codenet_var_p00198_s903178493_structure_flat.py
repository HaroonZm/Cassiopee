while True:
  n = int(input())
  if n == 0:
    break

  cube_dic = {}
  ans = 0

  for _ in range(n):
    cube = input().split()
    c1, c2, c3, c4, c5, c6 = cube[0], cube[1], cube[2], cube[3], cube[4], cube[5]
    if c2 == "Red":
      tmp = c2
      c2 = c6
      c6 = c5
      c5 = c1
      c1 = tmp
    elif c3 == "Red":
      tmp = c3
      c3 = c6
      c6 = c4
      c4 = c1
      c1 = tmp
    elif c4 == "Red":
      tmp = c4
      c4 = c6
      c6 = c3
      c3 = c1
      c1 = tmp
    elif c5 == "Red":
      tmp = c5
      c5 = c6
      c6 = c2
      c2 = c1
      c1 = tmp
    elif c6 == "Red":
      tmp = c6
      c6 = c5
      c5 = c1
      c1 = tmp
    cube_tuple = (c1, c2, c3, c4, c5, c6)
    if cube_tuple in cube_dic:
      ans += 1
    else:
      cube_dic[(c1, c2, c3, c4, c5, c6)] = True
      cube_dic[(c1, c4, c2, c5, c3, c6)] = True
      cube_dic[(c1, c3, c5, c2, c4, c6)] = True
      cube_dic[(c1, c5, c4, c3, c2, c6)] = True
  print(ans)