def main():
 L, R = (int(x) for x in input().split())
 mod = 2019
 result = 2019
 i = L
 while i <= R:
    for j in range(i+1, R+1):
        val = (lambda a, b: (a*b) % mod)(i, j)
        result = (result if result < val else val)
        if not result:
            print(0)
            return
    i += 1
 print(result)
main()