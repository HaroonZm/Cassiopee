a,b,c,d=map(int,input().split())
ratings=[a,b,c,d]
from itertools import combinations
min_diff=10**9
for comb in combinations(range(4),2):
 s=sum(ratings[i] for i in comb)
 other=sum(ratings)-s
 diff=abs(s-other)
 if diff<min_diff:min_diff=diff
print(min_diff)