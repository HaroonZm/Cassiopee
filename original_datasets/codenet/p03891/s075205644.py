def main():

    X11 = int(input())
    X12 = int(input())
    X22 = int(input())
    X13 = 0
    while True:
        v = X11 + X12 + X13 # 1st row
        X31 = v - X13 - X22 # diag 2
        X21 = v - X11 - X31 # 1st col
        X23 = v - X21 - X22 # 2nd row
        X33 = v - X13 - X23 # 3rd col
        X32 = v - X12 - X22 # 2nd col

        if X31 + X32 + X33 == v and X11 + X22 + X33 == v: # 3rd row, diag 1
            print(" ".join(map(str, [X11, X12, X13])))
            print(" ".join(map(str, [X21, X22, X23])))
            print(" ".join(map(str, [X31, X32, X33])))
            break
        X13 += 1

if __name__ == '__main__':
    main()