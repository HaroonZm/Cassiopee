a,b,k = map(int,input().split())

ans_t = max(a-k,0)
if a-k < 0:
  b = max(b-(k-a),0)
print(ans_t,b)