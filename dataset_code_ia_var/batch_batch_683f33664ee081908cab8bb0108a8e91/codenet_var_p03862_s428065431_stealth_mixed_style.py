def main():
    N_X = input().split()
    N = int(N_X[0])
    X = int(N_X[1])
    A = []
    for x in input().split():
        A.append(int(x))
    A.append(0)
    res = 0
    i = 0
    while i < N:
        s = A[i] + (A[i - 1] if i > 0 else 0) - X
        k = s if s > 0 else 0
        res = res + k
        A[i] -= k
        i += 1
    print(res)

if __name__ == "__main__":
    (lambda f: f())(main)