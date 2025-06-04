def solve():
    import sys
    sys.setrecursionlimit(10**7)

    N = int(sys.stdin.readline())
    A = [int(sys.stdin.readline()) for _ in range(N)]

    from functools import cmp_to_key

    def pow_compare(x, y):
        # Compare x^y and y^x without computing large powers
        if x == y:
            return 0
        # By problem definition 0^0=1
        # handle zero cases:
        if x == 0 and y == 0:
            return 0
        if x == 0 and y != 0:
            # x^y = 0^y = 0 (if y>0), y^x = y^0=1
            return 1  # x^y < y^x, so return positive means x < y
        if y == 0 and x != 0:
            # x^y = x^0=1, y^x=0^x=0 (x>0), so x^y > y^x
            return -1
        # For positive x,y , use comparison of y*log(x) and x*log(y)
        import math
        a = y * math.log(x) if x > 0 else float('-inf')
        b = x * math.log(y) if y > 0 else float('-inf')
        if abs(a - b) < 1e-14:
            return 0
        elif a > b:
            return -1
        else:
            return 1

    B = sorted(A, key=cmp_to_key(pow_compare))

    for b in B:
        print(b)