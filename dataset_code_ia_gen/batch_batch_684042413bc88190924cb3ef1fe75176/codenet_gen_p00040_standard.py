import sys
def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    g, x, y = 1, 0, 1
    r0, r1 = m, a
    s0, s1 = 1, 0
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if r0 != 1:
        return None
    return s0 % m

def decrypt(text, a, b):
    a_inv = modinv(a, 26)
    res = []
    for c in text:
        if 'a' <= c <= 'z':
            val = ord(c) - ord('a')
            orig = (a_inv * (val - b)) % 26
            res.append(chr(orig + ord('a')))
        else:
            res.append(c)
    return ''.join(res)

def contains_keyword(s):
    return 'that' in s or 'this' in s

n = int(sys.stdin.readline())
lines = [sys.stdin.readline().rstrip('\n') for _ in range(n)]

# Possible alpha values coprime with 26
alphas = [a for a in range(1, 26) if a % 2 != 0 and a % 13 != 0]

for line in lines:
    for a in alphas:
        for b in range(26):
            dec = decrypt(line, a, b)
            if contains_keyword(dec):
                print(dec)
                break
        else:
            continue
        break