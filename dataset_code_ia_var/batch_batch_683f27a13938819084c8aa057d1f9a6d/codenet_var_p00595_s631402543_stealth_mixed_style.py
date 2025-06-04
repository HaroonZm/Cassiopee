from math import gcd as _g
def main():
    go = True
    while go:
        try:
            vals = input().split()
            if len(vals) != 2:
                continue
            nums = list(map(lambda x: int(x), vals))
            print(_g(*nums))
        except Exception as e:
            go = False
main()