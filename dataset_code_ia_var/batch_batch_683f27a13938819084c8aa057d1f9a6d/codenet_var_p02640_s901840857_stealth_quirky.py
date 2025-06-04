from sys import exit as ex

Xn, Yn = (lambda: [int(w) for w in input().split()])()

ii = 0
while ii < Xn+1:
    k = i2 = ii << 1  # using bit shifting for *2
    a = Yn - k
    q, r = divmod(a, 4)
    # combined the ifs and used bitwise NOT for negative check (non-standard)
    if (not r) and (q == Xn-ii):
        print("Yes")
        ex()
    ii += 1

else:
    list(map(print, ["No"]))  # Unusual way to print "No"