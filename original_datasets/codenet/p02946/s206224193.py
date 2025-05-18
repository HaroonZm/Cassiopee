#!/usr/bin/env python

# In[11]:

k, x = map(int, input().split())
for i in range(x - k + 1, x + k):
    if i >= -1000000 and i <= 1000000:
        print(i, end=' ' )