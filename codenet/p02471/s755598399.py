def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    q, t = divmod(a, b)
    x, y = ext_gcd(b, t)
    return y, (x - q * y)

def main():
   a, b = map(int, input().split())
   print(*ext_gcd(a,b))
   return

main()