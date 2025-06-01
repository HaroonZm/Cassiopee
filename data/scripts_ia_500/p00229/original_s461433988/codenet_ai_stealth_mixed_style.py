def calc(b, r, g, c, s, t):
    return 100 + (b + r) * 15 + g * 7 + c * 2 + (b * 5 + r * 3) * 13 - (t - (s + b * 5 + r * 3)) * 3

def main():
    while True:
        vals = list(map(int, input().split()))
        if all(x == 0 for x in vals):
            break
        b, r, g, c, s, t = vals
        result = calc(b, r, g, c, s, t)
        print(f"Result: {result}")

main()