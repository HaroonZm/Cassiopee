from enum import Enum
import sys
import math
 
BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001
 
 
def calc_gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    return calc_gcd(b,a%b)
 
 
A,B = map(int,input().split())
print("%d"%(calc_gcd(A,B)))