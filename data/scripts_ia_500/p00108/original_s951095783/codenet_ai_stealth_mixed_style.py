from collections import Counter

def main():
 i = 1
 while True:
  n = int(input())
  if not n:
   break
  s = list(map(int, input().split()))
  c = 0
  while True:
   t = s[:]
   freq = Counter(t)
   s = list(map(lambda x: freq[x], t))
   if t == s:
    break
   c += 1
  print(c)
  print(*s)

main()