import sys

while True:
    h, w = map(int, raw_input().split(" "))

    if h == 0 & w == 0:
        break

    for i in range(h):
        for j in range(w):
            if (i == 0) | (i == h - 1) | (j == 0) | (j == w - 1):
                sys.stdout.write ("#")

            else :
                sys.stdout.write (".")

        print ("")
    print ("")