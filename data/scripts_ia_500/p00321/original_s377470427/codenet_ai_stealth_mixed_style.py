n,f=[*map(int,input().split())]
pair={}
for i in range(n):
  line=input().split()
  m=int(line[0])
  items=line[1:]
  for p in range(m):
    for q in range(p):
      key=tuple(sorted([items[p],items[q]]))
      if key in pair:
        pair[key]+=1
      else:
        pair[key]=1
def filter_pairs(d,threshold):
  return [k for k,v in d.items() if v>=threshold]
ans=filter_pairs(pair,f)
ans.sort()
print(len(ans))
if len(ans):
  for x in ans:
    print(x[0],x[1])