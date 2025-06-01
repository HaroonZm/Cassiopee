def experiment(v):
    n = 1
    k = 4.9
    def calc_y(x):
        return 5 * x - 5
    while True:
        y = calc_y(n)
        v_ex = 2 * k * (y / k) ** 0.5
        if v_ex >= v:
            return n
        n += 1

if __name__ == "__main__":
    import sys
    inputs = sys.stdin.read().split()
    for line in inputs:
        try:
            value = float(line)
            print(experiment(value))
        except ValueError:
            continue