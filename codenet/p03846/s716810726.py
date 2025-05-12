import numpy as np
import math
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

n = int(input())
A = iarr()
s = set(A)
if sum(A)==2*sum(s): print(pow(2, len(A)//2, int(1e9+7)))
else: print(0)