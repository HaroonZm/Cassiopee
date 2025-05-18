N = int(input())
S = input()

# 左は尺取り。しかも３とって失敗したら、l,r双方いんくりしてよい
# 右は総当たり。

ans = 0
l,r = 0,1
while l<N and r<N:
  findf = False
  target = S[l:r]
  L = r-l
  for k in range(l+L,N-1):
    compare = S[k:k+L]
    #print(target, compare)
    if target == S[k:k+L]:
      ans = max(ans,L)
      findf = True
      break
  if findf and r < N-1:
    r += 1
  else:
    l += 1
    r = min(r+1,N-1)
    
print(ans)