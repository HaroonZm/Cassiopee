S=input()
alphabet=[chr(i) for i in range(97, 97+26)]
ans=[]
for a in alphabet:
  if a not in S:
    ans.append(a)
if not ans:
  print('None')
else:
  print(ans[0])