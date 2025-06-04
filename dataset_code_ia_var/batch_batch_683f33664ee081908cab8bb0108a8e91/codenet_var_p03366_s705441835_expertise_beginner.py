import sys

sys.setrecursionlimit(10000000)

def main():
    data = list(map(int, sys.stdin.read().split()))
    N = data[0]
    S = data[1]
    X = []
    P = []
    for i in range(N):
        X.append(data[2 + i * 2])
        P.append(data[3 + i * 2])

    left_count = 0
    for i in range(N):
        if X[i] < S:
            left_count += 1

    leftX = []
    leftP = []
    for i in range(left_count - 1, -1, -1):
        leftX.append(X[i])
        leftP.append(P[i])

    rightX = []
    rightP = []
    for i in range(left_count, N):
        rightX.append(X[i])
        rightP.append(P[i])

    leftN = len(leftX)
    rightN = len(rightX)

    visit = []
    while leftN > 0 and rightN > 0:
        x1 = leftX[-1]
        p1 = leftP[-1]
        x2 = rightX[-1]
        p2 = rightP[-1]
        if p1 < p2:
            visit.append(x1)
            leftX.pop()
            leftP.pop()
            leftN -= 1
            rightP[-1] = p1 + p2
        else:
            visit.append(x2)
            rightX.pop()
            rightP.pop()
            rightN -= 1
            leftP[-1] = p1 + p2

    if leftN > 0:
        for i in range(leftN-1, -1, -1):
            visit.append(leftX[i])
    else:
        for i in range(rightN-1, -1, -1):
            visit.append(rightX[i])
    visit.append(S)

    answer = 0
    for i in range(len(visit) - 1):
        answer += abs(visit[i+1] - visit[i])

    print(answer)

if __name__ == "__main__":
    main()