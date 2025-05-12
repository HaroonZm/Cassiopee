import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# xor shift（F_2上の多項式）に関する gcd を計算する

from functools import reduce

X = int(readline().split()[1],2)
A = [int(x,2) for x in readlines()]

MOD = 998244353

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b:
        LA = a.bit_length()
        LB = b.bit_length()
        a ^= b << (LA - LB)
        if a < b:
            a,b = b,a
    return a

g = reduce(gcd,A)

# g の "倍数" で、X以下のものを作る方法の数を数える
# 上位の桁を決めると、gの倍数は一意に決まる。
# よって、上位の桁がXに一致するときのみが問題

LX = X.bit_length()
Lg = g.bit_length()
answer = X >> (Lg - 1)

prod = 0
x = X; Lx = LX
while Lx >= Lg:
    prod ^= g << (Lx - Lg)
    x ^= g << (Lx - Lg)
    Lx = x.bit_length()

if prod <= X:
    answer += 1

answer %= MOD
print(answer)