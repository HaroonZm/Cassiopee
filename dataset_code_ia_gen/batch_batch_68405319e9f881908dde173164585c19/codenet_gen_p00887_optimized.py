import sys

def gauss_elimination(matrix, vector, n):
    for i in range(n):
        pivot = -1
        for r in range(i, n):
            if matrix[r][i]:
                pivot = r
                break
        if pivot == -1:
            continue
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            vector[i], vector[pivot] = vector[pivot], vector[i]
        for r in range(i+1, n):
            if matrix[r][i]:
                for c in range(i, n):
                    matrix[r][c] ^= matrix[i][c]
                vector[r] ^= vector[i]

    for i in reversed(range(n)):
        s = vector[i]
        for c in range(i+1, n):
            s ^= (matrix[i][c] & vector[c])
        if matrix[i][i] == 0 and s != 0:
            return False
        vector[i] = s
    return True

def main():
    input = sys.stdin.readline
    while True:
        m,n,d = map(int,input().split())
        if m==0 and n==0 and d==0:
            break
        size = m*n
        lights = []
        for _ in range(n):
            lights.extend(map(int,input().split()))
        A = [0]*size
        for i in range(size):
            A[i] = 0
        matrix = [[0]*size for _ in range(size)]
        for r in range(n):
            for c in range(m):
                idx = r*m+c
                for rr in range(n):
                    for cc in range(m):
                        if abs(r-rr)+abs(c-cc) == d or (r==rr and c==cc):
                            matrix[idx][rr*m+cc] = 1
        vector = lights[:]
        if gauss_elimination(matrix, vector, size):
            print(1)
        else:
            print(0)

if __name__=="__main__":
    main()