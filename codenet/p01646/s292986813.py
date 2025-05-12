def add_edge(node, adj_lst, adj_rev, s1, s2):
  ind = 0
  max_len = min(len(s1), len(s2))
  while ind < max_len and s1[ind] == s2[ind]:
    ind += 1
  if ind == max_len:
    if max_len < len(s1):
      return True
    return False
  c1 = ord(s1[ind]) - ord("a")
  c2 = ord(s2[ind]) - ord("a")
  adj_lst[c1].add(c2)
  adj_rev[c2].add(c1)
  node.add(c1)
  node.add(c2)
  return False
def main():
  while True:
    n = int(input())
    if n == 0:
      break
    
    lst = [input() for _ in range(n)]
    node = set()
    adj_lst = [set() for _ in range(26)]
    adj_rev = [set() for _ in range(26)]
    blank_flag = False
    for i in range(n):
      for j in range(i + 1, n):
        blank_flag = blank_flag or add_edge(node, adj_lst, adj_rev, lst[i], lst[j])
    
    visited = [False] * 26
    cycle_flag = False
  
    def visit(n):
      ret = False
      if visited[n] == 2:
        return True
      elif visited[n] == 0:
        visited[n] = 2
        for to in adj_lst[n]:
          ret = ret or visit(to)
        visited[n] = 1
      return ret
    
    for n in node:
      cycle_flag = cycle_flag or visit(n)
    if cycle_flag or blank_flag:
      print("no")
    else:
      print("yes")

main()