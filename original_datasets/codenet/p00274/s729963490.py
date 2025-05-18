while 1:
  n=int(input())
  if n==0: break
  a=list(map(int,input().split()))
  if max(a)<2:
    print("NA")
    continue
  print(len([x for x in a if x>0])+1)