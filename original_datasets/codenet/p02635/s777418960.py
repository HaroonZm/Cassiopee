#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
#from math import gcd
import bisect
import heapq
from collections import defaultdict
from collections import deque
from collections import Counter
from functools import lru_cache

#############
# Constants #
#############

MOD = 998244353
INF = float('inf')
AZ = "abcdefghijklmnopqrstuvwxyz"

#############
# Functions #
#############

######INPUT######
def I(): return int(input().strip())
def S(): return input().strip()
def IL(): return list(map(int,input().split()))
def SL(): return list(map(str,input().split()))
def ILs(n): return list(int(input()) for _ in range(n))
def SLs(n): return list(input().strip() for _ in range(n))
def ILL(n): return [list(map(int, input().split())) for _ in range(n)]
def SLL(n): return [list(map(str, input().split())) for _ in range(n)]

######OUTPUT######
def P(arg): print(arg); return
def Y(): print("Yes"); return
def N(): print("No"); return
def E(): exit()
def PE(arg): print(arg); exit()
def YE(): print("Yes"); exit()
def NE(): print("No"); exit()

#####Shorten#####
def DD(arg): return defaultdict(arg)

#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

######Factorization######
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0: 
        cnt+=1 
        temp //= i
      arr.append([i, cnt])
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
  return arr

#####MakeDivisors######
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i: 
        divisors.append(n//i)
  return divisors

#####MakePrimes######
def make_primes(N):
  max = int(math.sqrt(N))
  seachList = [i for i in range(2,N+1)]
  primeNum = []
  while seachList[0] <= max:
    primeNum.append(seachList[0])
    tmp = seachList[0]
    seachList = [i for i in seachList if i % tmp != 0]
  primeNum.extend(seachList)
  return primeNum

#####GCD#####
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#####BitCount#####
def count_bit(n):
  count = 0
  while n:
    n &= n -1
    count += 1
  return count

#####ChangeBase#####
def base_10_to_n(X, n):
  if X//n:
    return base_10_to_n(X//n, n)+[X%n]
  return [X%n]

def base_n_to_10(X, n):
  return sum(int(str(X)[-i-1])*n**i for i in range(len(str(X))))

#####IntLog#####
def int_log(n, a):
  count = 0
  while n>=a:
    n //= a
    count += 1
  return count

#############
# Main Code #
#############
S,K = SL()
K = int(K)

data = []
ones = 0
count = 0
for s in S:
  if s == "1":
    count += 1
    ones += 1
  else:
    data.append(count)
    count = 0
data.append(count)
data = data[::-1]
N = len(data)
#print(data)
K = min(K,ones)

dp = [[[0 for j in range(K+1)] for k in range(K+1)] for i in range(N)]
for i in range(N):
  dp[i][0][0] = 1
for k in range(min(data[0]+1,K+1)):
  dp[0][k][k] = 1
#print(dp[0])
for i in range(1,N):
  for k in range(K+1):   
    for j in range(K+1)[::-1]:
      if j == K:
        dp[i][k][j] = dp[i-1][k][j]
        dp[i][k][j] %= MOD
      else:
        dp[i][k][j] = dp[i-1][k][j] + dp[i][k][j+1]
        dp[i][k][j] %= MOD
  a = data[i]
  if a:
    for k in range(K):
      q = deque([dp[i-1][k][0]])
      temp = dp[i-1][k][0]
      for j in range(1,K+1):
        #print(i,k,q)
        if k+j > K: break
        dp[i][k+j][j] += temp
        dp[i][k+j][j] %= MOD
        q.append(dp[i-1][k+j][j])
        temp += dp[i-1][k+j][j]
        if len(q) > a:
          temp -= q.popleft()
        temp %= MOD
  #print(dp[i])
      
ans = 0
for k in range(K+1):
  ans += dp[-1][k][0]
  ans %= MOD
  
print(ans)