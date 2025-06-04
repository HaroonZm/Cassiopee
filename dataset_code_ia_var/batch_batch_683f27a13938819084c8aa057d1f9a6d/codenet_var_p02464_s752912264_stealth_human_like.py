# ok, let's try to make it a bit more "human"
n = int(input())  # first number (not really used)
A = set(int(x) for x in input().split())  # my first set
m = int(input())  # number of elements (again, maybe not useful)
B = set(map(int, input().split()))  # second set
# Now let's get intersect, twisted way!
common = list(A & B)
if len(common) > 0:
    for v in sorted(common):  # to print in ascending order
        print(v)
# else:  # original code didn't handle empty intersection (should be silent)