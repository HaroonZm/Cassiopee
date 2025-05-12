from itertools import zip_longest

s = input()
n = len(s)-1

total = 0
li = [0] * 2**n

for i in range(2**n):
  op = [""] * n
  for j in range(n):
    if (i >> j) & 1:
      op[j] = "+"
  li[i] = op
  
for i in li:
  siki = ""
  for j, k in zip_longest(i, s, fillvalue=""):
    siki += k+j
  total += eval(siki)
  
print(total)