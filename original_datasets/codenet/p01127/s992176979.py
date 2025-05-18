def isRect(data,dic):
  for d in dic.items():
    isValid=True
    for i in xrange(d[1][0],d[1][2]+1):
      for j in xrange(d[1][1],d[1][3]+1):
        if not (data[i][j]==d[0] or data[i][j]=="*") :
          isValid=False
    if isValid: return d[0]
  return "-"

def checker(data,dic):
  while len(dic)>0:
    r=isRect(data,dic)
    if r=="-":
      print "SUSPICIOUS"
      return
    else:
      for i in xrange(dic[r][0],dic[r][2]+1):
        for j in xrange(dic[r][1],dic[r][3]+1):
          data[i][j]="*"
      del dic[r]
  print "SAFE"

T=int(raw_input())
for _ in xrange(T):
  H,W=map(int,raw_input().split())
  data=[["-"]*W for _ in xrange(H)]
  dic={}
  for i in xrange(H):
    s=raw_input()
    for j in xrange(W):
      data[i][j]=s[j]
      if s[j] not in dic:
        dic[s[j]]=(i,j,i,j)
      else:
        dic[s[j]]=(min(dic[s[j]][0],i),min(dic[s[j]][1],j),max(dic[s[j]][2],i),max(dic[s[j]][3],j))
  checker(data, dic)