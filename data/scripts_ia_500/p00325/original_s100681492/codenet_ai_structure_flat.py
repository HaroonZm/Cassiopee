n = int(input())
prog = [input().split() for _ in range(n)]
v = set()
for ss in prog:
  for s in ss:
    if "a" <= s <= "z":
      v.add(s)
v = sorted(list(v))
var_state = [0] * len(v)
var_to_ind = {}
for i, var in enumerate(v):
  var_to_ind[var] = i
line_to_ind = {}
for i, ss in enumerate(prog):
  line_to_ind[ss[0]] = i
new_prog = []
for p in prog:
  if p[1] == "ADD":
    if p[4] in var_to_ind:
      new_prog.append([0, var_to_ind[p[2]], var_to_ind[p[3]], var_to_ind[p[4]]])
    else:
      new_prog.append([1, var_to_ind[p[2]], var_to_ind[p[3]], int(p[4])])
  elif p[1] == "SUB":
    if p[4] in var_to_ind:
      new_prog.append([2, var_to_ind[p[2]], var_to_ind[p[3]], var_to_ind[p[4]]])
    else:
      new_prog.append([3, var_to_ind[p[2]], var_to_ind[p[3]], int(p[4])])
  elif p[1] == "SET":
    if p[3] in var_to_ind:
      new_prog.append([4, var_to_ind[p[2]], var_to_ind[p[3]]])
    else:
      new_prog.append([5, var_to_ind[p[2]], int(p[3])])
  elif p[1] == "IF":
    if p[3] in line_to_ind:
      new_prog.append([6, var_to_ind[p[2]], line_to_ind[p[3]]])
    else:
      new_prog.append([6, var_to_ind[p[2]], 100])
  elif p[1] == "HALT":
    new_prog.append([7])
prog = new_prog
used = [[False] * n for _ in range(16 ** len(v))]
xs = [1, 16, 256, 4096, 65536]
ind = 0
h = 0
while True:
  if ind >= n:
    flag = True
    break
  if used[h][ind]:
    flag = False
    break
  used[h][ind] = True
  p = prog[ind]
  ins = p[0]
  if ins == 0:
    v1, v2, v3 = p[1], p[2], p[3]
    temp = var_state[v2] + var_state[v3]
    if not temp < 16:
      flag = True
      break
    h += (temp - var_state[v1]) * xs[v1]
    var_state[v1] = temp
  elif ins == 1:
    v1, v2, con = p[1], p[2], p[3]
    temp = var_state[v2] + con
    if not temp < 16:
      flag = True
      break
    h += (temp - var_state[v1]) * xs[v1]
    var_state[v1] = temp
  elif ins == 2:
    v1, v2, v3 = p[1], p[2], p[3]
    temp = var_state[v2] - var_state[v3]
    if not 0 <= temp:
      flag = True
      break
    h += (temp - var_state[v1]) * xs[v1]
    var_state[v1] = temp
  elif ins == 3:
    v1, v2, con = p[1], p[2], p[3]
    temp = var_state[v2] - con
    if not 0 <= temp:
      flag = True
      break
    h += (temp - var_state[v1]) * xs[v1]
    var_state[v1] = temp
  elif ins == 4:
    v1, v2 = p[1], p[2]
    h += (var_state[v2] - var_state[v1]) * xs[v1]
    var_state[v1] = var_state[v2]
  elif ins == 5:
    v1, con = p[1], p[2]
    h += (con - var_state[v1]) * xs[v1]
    var_state[v1] = con
  elif ins == 6:
    v1, dest = p[1], p[2]
    if var_state[v1]:
      ind = dest - 1
  else:
    flag = True
    break
  ind += 1
if flag:
  for t in zip(v, var_state):
    print(t[0], "=", t[1], sep="")
else:
  print("inf")