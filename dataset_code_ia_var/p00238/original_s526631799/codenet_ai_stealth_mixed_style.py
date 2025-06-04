import sys

def sub_vals(pairs):
    total = 0
    for first, second in pairs:
        total += second - first
    return total

def mainloop():
    while 1:
        t = input()
        if t == 0:
            sys.exit(0)
        pairs = []
        for _ in range(int(raw_input())):
            parts = raw_input().split()
            a, b = map(int, parts)
            pairs.append((a, b))
        t -= sub_vals(pairs)
        if t <= 0:
            print "OK"
        else:
            print t

main = lambda: mainloop()
main()