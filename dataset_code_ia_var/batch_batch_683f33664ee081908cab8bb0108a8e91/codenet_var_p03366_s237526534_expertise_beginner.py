import time
import sys

def read_int():
    return int(input())

def read_int_n():
    return list(map(int, input().split()))

def read_str():
    return input()

def read_str_n():
    return list(map(str, input().split()))

def mt(f):
    def wrap(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(end - start, 'sec', file=sys.stderr)
        return result
    return wrap

@mt
def solve(S, X, P):
    # Combine positions with their weights into a list
    combined = []
    for i in range(len(X)):
        combined.append([P[i], [X[i]]])
    i = 0
    j = len(combined) - 1
    while i < j:
        if combined[i][0] >= combined[j][0]:
            combined[i][0] += combined[j][0]
            combined[i][1] += combined[j][1]
            j -= 1
        else:
            combined[j][0] += combined[i][0]
            combined[j][1] += combined[i][1]
            i += 1

    total = 0
    pos = S
    left = S
    right = S
    for o in combined[i][1]:
        if left < o < right:
            continue
        total += abs(pos - o)
        if o < pos:
            left = o
        else:
            right = o
        pos = o
    return total

def main():
    N_S = read_int_n()
    N = N_S[0]
    S = N_S[1]
    X = []
    P = []
    for _ in range(N):
        x_p = read_int_n()
        X.append(x_p[0])
        P.append(x_p[1])
    print(solve(S, X, P))

if __name__ == '__main__':
    main()