import sys

while True:
    h, w = map(int, raw_input().split(" "))

    if (h == 0) and (w == 0):
        break

    for i in range(h):
        for j in range(w):
            if (i == 0) or (i == h - 1) or (j == 0) or (j == w - 1):
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print("")
    print("")