a=input()
ans=1
from collections import defaultdict
d = defaultdict(int)
for i in range(len(a)):
    d[a[i]]+=1
    ans+=(i+1-d[a[i]])
print(ans)