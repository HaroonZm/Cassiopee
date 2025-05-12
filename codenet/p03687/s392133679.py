s=str(input())
ans=int(len(s)/2)

for i in range(97, 97+26):
  if chr(i) in s:
    ct= s.count(chr(i))
    place=[0]*ct
    for j in range(ct-1):
      place[0]=s.find(chr(i))+1
      place[j+1]=s[place[j]:].find(chr(i))+place[j]+1
    haba=max(len(s)-place[ct-1],place[0]-1)
    for j in range(ct-1):
      haba=max(haba,place[j+1]-place[j]-1)
    ans=min(ans,haba)

print(ans)