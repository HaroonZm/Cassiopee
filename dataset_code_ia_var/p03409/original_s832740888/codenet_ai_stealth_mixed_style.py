import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A, B = [], []
    for i in range(n):
        A.append((int(data[2*i+1]), int(data[2*i+2])))
    C = []
    idx = 2*n+1
    while idx < len(data):
        y1 = int(data[idx])
        y2 = int(data[idx+1])
        C.append((y1, y2))
        idx += 2
    A.sort(key=lambda x: (x[1], x[0]))
    C = sorted(C, key=lambda z: (-z[0], -z[1]))
    counter = 0
    for y, z in reversed(C):
        for i in range(len(A)-1, -1, -1):
            u, v = A[i]
            if u < y and v < z:
                counter = counter + 1
                A.pop(i)
                break
    print(counter)
main()