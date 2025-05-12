n=input()
a=[int(x) for x in input().split()]
num=a+[i+1 for i in a]+[i-1 for i in a]
from collections import Counter
c=Counter(num)
print(c.most_common(1)[0][1])