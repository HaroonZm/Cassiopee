import sys

def main():
    for line in sys.stdin:
        try:
            parts = line.strip().split(',')
            T = tuple(map(float, parts))
            z = complex(T[0] - T[2], T[1] - T[3])
            P = complex(*T[0:2])
            Q = complex(*T[4:6])
            R = P + (Q - P).conjugate() * z / z.conjugate()
            print("{0:.6f} {1:.6f}".format(R.real, R.imag))
        except (IndexError, ValueError):
            continue

if __name__ == "__main__":
    main()