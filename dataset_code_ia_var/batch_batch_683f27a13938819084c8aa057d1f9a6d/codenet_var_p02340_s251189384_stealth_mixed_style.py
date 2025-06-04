from sys import stdin

class FastInput:
    def get(self): return list(map(int, stdin.readline().strip().split()))

def s(n):
    # Generator for indices - varying structure for demonstration
    x = 1
    while x <= n[0]:
        if x <= min(n[1], n[0]):
            yield x, x
        else:
            yield x, n[1]
        x += 1

def main():
    reader = FastInput()
    n, k = reader.get()
    MODULO = 10**9 + 7

    if any([n == 1, k == 1]):
        print(1)
        return

    matrix = dict()
    for i in range(n+1):
        matrix[i] = [0]*(k+1)
    matrix[0][0] = 1

    for idx, lim in s((n, k)):
        for v in range(1, lim+1):
            matrix[idx][v] = (matrix.get(idx-1, [0]* (k+1))[v-1] + matrix.get(idx-v, [0]*(k+1))[v]) if idx-v >= 0 else 0

    print(sum(matrix[n])%MODULO)

if __name__ == '__main__':
    main()