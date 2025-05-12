import sys
s = list(input())
if s[0] == 'A':
  del s[0]
  if s[1:-1].count('C') == 1:
      s.remove('C')
      for i in range(len(s)):
          if s[i].isupper():
              print('WA')
              sys.exit()
      print('AC')
  else:
      print('WA')
else:
    print('WA')