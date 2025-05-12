import collections
N = int(input())
s = [input() for i in range(N)]
 
counter = collections.Counter(s)
count = counter.most_common()
 
most = count[0][1]
 
c =[]
for i in range(len(counter)):
    if count[i][1] == most:
        c.append(count[i][0])
 
c.sort()
 
for i in range(len(c)):
    print(c[i])