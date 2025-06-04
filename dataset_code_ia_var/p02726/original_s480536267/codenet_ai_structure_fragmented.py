def read_input():
    return map(int, input().split())

def init_list(n):
    return [0]*n

def min1(j, i):
    return j - i

def abs1(x, i):
    return abs(x - i)

def calc1(X, i):
    return abs1(X, i)

def calc2(j, Y):
    return abs1(j, Y)

def calc3(Y, i):
    return abs1(Y, i)

def calc4(j, X):
    return abs1(j, X)

def sum1(a, b):
    return a + b

def compute_dists(j, i, X, Y):
    a = min1(j, i)
    b = sum1(calc1(X, i), 1)
    b = sum1(b, calc2(j, Y))
    c = sum1(calc3(Y, i), 1)
    c = sum1(c, calc4(j, X))
    return a, b, c

def compute_min(a, b, c):
    return min(a, b, c)

def increment(C, idx):
    C[idx] += 1

def process(N, X, Y, C):
    for i in range(1, N):
        for j in range(i+1, N+1):
            a, b, c = compute_dists(j, i, X, Y)
            m = compute_min(a, b, c)
            increment(C, m)

def print_result(C, N):
    for i in range(1, N):
        print(C[i])

def main():
    N, X, Y = read_input()
    C = init_list(N)
    process(N, X, Y, C)
    print_result(C, N)

main()