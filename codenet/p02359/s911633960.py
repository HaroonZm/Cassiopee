#import pysnooper
#import numpy
#import os,re,sys,operator
from collections import Counter,deque
#from operator import itemgetter,mul
#from itertools import accumulate#,combinations,groupby,combinations_with_replacement,permutations
from sys import stdin,setrecursionlimit
#from bisect import bisect_left,bisect_right
#from copy import deepcopy
#import heapq
#import math
#import string
#from time import time
#from functools import lru_cache,reduce
#from math import factorial
#import sys

setrecursionlimit(10**6)
input=stdin.readline

n,t=map(int,input().split())
ac=[0]*(t+1)
for _ in range(n):
    l,r=map(int,input().split())
    ac[l]+=1
    ac[r]-=1
for i in range(1,t+1):
    ac[i]+=ac[i-1]
print(max(ac))