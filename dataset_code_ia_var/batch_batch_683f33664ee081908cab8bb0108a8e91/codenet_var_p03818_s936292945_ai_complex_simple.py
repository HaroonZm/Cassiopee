from functools import reduce
from itertools import groupby
from operator import itemgetter

N=int(input())
A=list(map(int,input().split()))

# Count occurrences using groupby + sorted
counts = [len(list(g)) for _,g in groupby(sorted(A))]
# Classify using map and reduce
flags = list(map(lambda x: x%2, counts))
even_count = reduce(lambda acc,x:acc+(1 if x==0 else 0), flags, 0)
odd_count = len(flags)-even_count
ans = odd_count + (even_count if even_count%2==0 else even_count-1)
print(ans)