#!/usr/bin/env python

# In[10]:

N = int(input())
b = list(map(int, input().split()))

# In[11]:

op = []
mylist = [x for x in b]
f = True
while len(mylist)>0:
    for i in reversed(range(len(mylist))):
        if mylist[i] == i+1:
            op.append(mylist.pop(i))
            break
    else:
        f = False
        break
if f:
    ans = list(reversed(op))
    for x in ans:
        print(x)
else:
    print(-1)

# In[ ]: