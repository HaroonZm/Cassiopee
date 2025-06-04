def main():
 m, f, b = [int(x) for x in input().split()]
 if m+f < b:
  print('NA')
  return
 def check(a, c):
  if a > c: print('0')
  else: print(c - a)
 check(m, b)
main()