import re

def deref(d, expr):
  expr = expr.replace(']', '')
  symb = expr.split('[')
  symb[-1] = symb[-1]
  while len(symb) > 1:
    name, index = symb[-2:]
    if index not in d[name]:
      return None

    symb.pop()
    symb.pop()
    symb.append(d[name][index])

  return symb[0]

def check(s):
  d = {}
  dd = {}
  for i, stmt in enumerate(s, 1):
    if '=' not in stmt:
      name = stmt[0]
      index = stmt[2:-1]
      d[name] = {}
      dd[name] = int(index)
      continue

    lhs, rhs = stmt.split('=')
    
    name = lhs[0]
    index = lhs[2:-1]
    index = deref(d, index)
    value = deref(d, rhs)
    if index is None or value is None or int(index) >= dd[name]:
      print(i)
      return

    d[name][index] = value

  print(0)

def main():
  list_ = []
  with open(0) as fin:
    for line in fin:
      line = line.strip()
      if line == '.':
        if not list_: 
          return 0

        check(list_)
        list_ = []
        continue

      list_.append(line)

if __name__ == '__main__':
  main()