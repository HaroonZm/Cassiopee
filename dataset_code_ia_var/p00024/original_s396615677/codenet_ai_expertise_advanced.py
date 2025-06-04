from math import sqrt
from itertools import count

def experiment(v, k=4.9):
    # y = 5*n - 5, v_ex = 2*k*sqrt(y/k) >= v
    # => 2*k*sqrt((5*n-5)/k) >= v
    # => sqrt((5*n-5)/k) >= v/(2*k)
    # => (5*n-5)/k >= (v/(2*k))**2
    # => 5*n-5 >= k*(v/(2*k))**2
    # => 5*n >= k*(v/(2*k))**2 + 5
    # => n >= (k*(v/(2*k))**2 + 5)/5
    min_n = int(-(-((k*(v/(2*k))**2 + 5) // 5)))  # ceiling division
    return min_n

def main():
    import sys
    for line in sys.stdin:
        try:
            v = float(line.strip())
            print(experiment(v))
        except ValueError:
            continue

if __name__ == "__main__":
    main()