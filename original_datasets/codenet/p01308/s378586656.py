dic = {"C":0, "C#":1, "D":2, "D#":3,
       "E":4, "F":5, "F#":6, "G":7,
       "G#":8, "A":9, "A#":10, "B":11}
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  t_lst = [-100] + list(map(lambda x:dic[x],input().split()))
  s_lst = list(map(lambda x:dic[x],input().split()))
  s_lst.reverse()
  
  def search(stack):
    t_index, s_index = stack.pop()
    if s_index == m: return t_index == 0
    if t_index <= 0 or t_index > n: return False
    base = t_lst[t_index]
    proc = s_lst[s_index]
    diff = (proc - base) % 12
    if diff == 1  :stack.append((t_index - 2, s_index + 1))
    if diff == 0  :stack.append((t_index - 1, s_index + 1))
    if diff == 11 :stack.append((t_index + 1, s_index + 1))
    return False
  stack = [(n, 0), (n - 1, 0)]
  while stack:
    if search(stack):
      print("Yes")
      break
  else:
    print("No")