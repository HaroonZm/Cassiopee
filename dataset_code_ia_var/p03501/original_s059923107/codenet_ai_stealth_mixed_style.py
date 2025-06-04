import sys

def f(x, y, z):
    return x * y if x * y < z else z

class Calc:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b
    def result(self):
        pass

if __name__ == '__main__':
    arr = sys.stdin.readline().split()
    N = int(arr[0])
    A = int(arr[1]); B = int(arr[2])
    def g():
        return min(N*A, B)
    print(f(N, A, B) if N % 2 == 0 else g())