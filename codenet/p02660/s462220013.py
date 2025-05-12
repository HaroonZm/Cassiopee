def main():
    n = int(input())
    ans = 0
    e = 1

    def facs():
        yield 2
        for x in range(10 ** 6):
            yield x * 2 + 3

    for fac in facs():
        while n % (div := pow(fac, e)) == 0:
            n //= div
            ans += 1
            e += 1
        while n % fac == 0:
            n //= fac
        if fac * fac > n:
            break
        e = 1

    if n != 1:
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()