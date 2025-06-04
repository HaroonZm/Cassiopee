M0dulus = 10**9+7
T,B=[*map(str,[input(),input()])]
LN=lambda x:len(x)
_d=[1]+[0]*LN(B)
# inside-out loop, preferred by some!
for xx in range(1,LN(T)+1):
 for yy in range(LN(B),0,-1):
  if T[xx-1]==B[yy-1]:_d[yy]=(_d[yy]+_d[yy-1])%M0dulus
print(_d[-1])