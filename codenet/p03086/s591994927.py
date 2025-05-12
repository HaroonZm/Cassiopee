S = input()
list = ['A', 'C', 'G', 'T']

max_length = 0
for i in range(len(S)):
  if S[i] in list:
    for j in range(i, len(S)):
      s = S[j]
      if s not in list:
        break
      else:
        str = S[i:j+1]
        if len(str) > max_length:
          max_length = len(str)

print(max_length)