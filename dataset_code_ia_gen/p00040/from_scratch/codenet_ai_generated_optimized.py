import sys

def egcd(a,b):
    while b:
        a,b = b,a%b
    return a

def modinv(a,m):
    # mod inverse exists as gcd(a,m)=1
    x,y,m0 = 1,0,m
    b = m
    while b:
        q = a//b
        a,b = b,a%b
        x,y = y,x - q*y
    return x % m0

def decode(cipher, a, b):
    a_inv = modinv(a,26)
    res = []
    for c in cipher:
        if 'a' <= c <= 'z':
            val = ord(c)-97
            plain = (a_inv*(val - b))%26
            res.append(chr(plain+97))
        else:
            res.append(c)
    return ''.join(res)

input=sys.stdin.readline
n=int(input())
keywords = ('that','this')
alphas = [a for a in range(1,26,2) if egcd(a,26)==1]  # possible a values

for _ in range(n):
    enc = input().rstrip('\n')
    found = False
    for a in alphas:
        for b in range(26):
            dec = decode(enc,a,b)
            if any(k in dec for k in keywords):
                print(dec)
                found = True
                break
        if found:
            break