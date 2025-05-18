a,b,c = map(int, input().split())
from collections import defaultdict
dic = defaultdict(lambda : 0)
for i in [a,b,c]:
    dic[i] += 1
if dic[5] == 2 and dic[7] == 1:
    print('YES')
else:
    print('NO')