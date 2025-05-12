w = input()
l = list(set(w))
ans =0
for i in range(len(l)):
  a = w.count(l[i])
  if a %2 !=0:
    ans =1
print('Yes' if ans ==0 else 'No')