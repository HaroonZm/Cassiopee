from functools import reduce

def diff(a,b):
  if a==b:
    return '0'
  elif a<b:
    return b - a
  else:
    return a - b

vals = list(map(int, input().split()))
result = diff(*vals)
print(result if isinstance(result,str) else reduce(lambda x,y: x+y, [result]))