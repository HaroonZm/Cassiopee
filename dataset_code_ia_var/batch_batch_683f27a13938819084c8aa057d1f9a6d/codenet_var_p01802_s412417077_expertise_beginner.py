def main():
    while True:
        line = input().split()
        d = int(line[0])
        e = int(line[1])
        if d == 0 and e == 0:
            break
        x = d
        y = 0
        ans = abs(d - e)
        while y != d:
            hypotenuse = (x * x + y * y) ** 0.5
            diff = abs(hypotenuse - e)
            if diff < ans:
                ans = diff
            x = x - 1
            y = y + 1
        print(ans)

main()