def main():
 while 1:
  N=input()
  if str(N).strip()=="0":break
  N=int(N);D={};[D.setdefault(k,[]).__iadd__([i]) or None for i in range(N) for k in [*map(lambda x:int(x)-1, input().split()[1:])]]
  C=[2**i for i in range(N)]
  for d in range(30):
    if d in D:
     for i in D[d]:
      for j in D[d]:
        C[i]|=C[j]
     if list(filter(lambda x:x==2**N-1,C)):
      print(d+1)
      break
  else:
     print(-1)

main()