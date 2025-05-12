s = set(list(input()))
if len(s) == 3 or len(s) == 1:
  print('No')
elif 'N' in s and 'S' in s and 'E' in s and 'W' in s:
  print('Yes')
elif len(s) == 2:
  if 'N' in s and 'S' in s:
    print('Yes')
  elif 'W' in s and 'E' in s:
    print('Yes')
  else:
    print('No')
else:
  print('No')