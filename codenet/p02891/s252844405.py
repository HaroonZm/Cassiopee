S = input()
K = int(input())

pre_c = ''
flg = 0
count = 1

f_c = S[0]
f_e = S[-1]
t = []

for c in S:
  if c == pre_c:
    count += 1
  elif pre_c == '':
    pass
  else:
    t.append(count)
    count = 1
  pre_c = c

t.append(count)
count_1 = 0
for i in t:
  count_1 += i // 2
  
if f_c == f_e and len(t) != 1:
  t[0] = t[0] + t[-1]
  t.pop(-1)

count_2 = 0
for i in t:
  count_2 += i // 2
  
if len(S) == 1:
  print(K // 2)
elif len(t) == 1:
  print(K * len(S) // 2)
else:
  print(count_1 + count_2 * (K - 1))