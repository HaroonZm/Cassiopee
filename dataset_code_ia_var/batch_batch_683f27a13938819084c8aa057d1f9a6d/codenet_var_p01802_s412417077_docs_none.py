def main():
    while 1:
        d,e= map(int, input().split())
        if d == e == 0:
            break
        x = d
        y = 0
        ans = abs(d-e)
        while y != d:
            a = abs((x ** 2 + y ** 2) ** 0.5 - e)
            ans = min(a,ans)
            x -= 1
            y += 1
        print(ans)

main()