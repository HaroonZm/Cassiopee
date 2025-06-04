import sys

def main():
    f = sys.stdin
    coins = 100
    for line in f:
        splitted = line.split()
        if not splitted:
            continue
        vals = [int(x) for x in splitted]
        if vals == [0]*6:
            break
        s, b, g, c, st, ag = vals
        fg = st
        bg = s*5 + b*3
        ng = ag - fg - bg
        # Mix: imperative, list comp, inline assignment, function style
        res = coins
        res -= (bg * 2)
        res -= (ng * 3)
        win_amount = (bg + s + b) * 15
        win_amount += g * 7
        win_amount += c << 1
        print(res + win_amount)

if __name__ == '__main__':
    main()