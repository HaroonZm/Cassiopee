#!/usr/bin/env python

# In[1]:

N = int(input())

# In[15]:

def func(i,j,N):
    ans = []
    for x in range(1,N+1):
        x_ = str(x)
        if x_[0] == str(i) and x_[-1] == str(j):
            ans += [x]
    return ans

# In[23]:

ans = 0
for i in range(10):
    for j in range(10):
        ans += len(func(i,j,N))*len(func(j,i,N))
print(ans)

# In[ ]: