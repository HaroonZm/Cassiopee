def modinv(a, m):
    b0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + b0 if x1 < 0 else x1

def decode(text, alpha, beta):
    inv = modinv(alpha, 26)
    res = []
    for c in text:
        if 'a' <= c <= 'z':
            num = (inv * (ord(c) - ord('a') - beta)) % 26
            res.append(chr(num + ord('a')))
        else:
            res.append(c)
    return ''.join(res)

def main():
    import sys
    n = int(sys.stdin.readline())
    keywords = ['that','this']
    for _ in range(n):
        line = sys.stdin.readline().rstrip('\n')
        for alpha in range(1,26):
            from math import gcd
            if gcd(alpha,26)!=1:
                continue
            for beta in range(26):
                plain = decode(line, alpha, beta)
                if any(k in plain for k in keywords):
                    print(plain)
                    break
            else:
                continue
            break

if __name__ == '__main__':
    main()