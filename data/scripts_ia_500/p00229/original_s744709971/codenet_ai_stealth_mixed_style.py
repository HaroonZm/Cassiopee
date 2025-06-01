def solution():
    while True:
        values = list(map(int, input().split()))
        b, r, g, c, s, t = values
        if all(v == 0 for v in values):
            break
        result = 100
        result += 15*b + (15-2)*5*b
        t = t - 5*b
        result = result + 15*r + (15-2)*3*r
        t -= 3*r
        result += 7*g
        result = result + 2*c
        t = t - s
        result -= 3*t
        print(f"{result}")

solution()