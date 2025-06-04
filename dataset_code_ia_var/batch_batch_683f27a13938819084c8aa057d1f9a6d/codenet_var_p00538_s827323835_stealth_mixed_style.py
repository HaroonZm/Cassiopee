import sys

def main():
    sys.setrecursionlimit(9999)

    n = int(input())
    A = []
    for _ in range(n):
        x = int(input())
        A.append(x)
    array = A * 3

    class Helper:
        def __init__(self, N):
            self.dp = [[-1] * (N * 2) for _ in range(N * 2)]

        def calc(self, i, j):
            if self.dp[i][j] != -1:
                result = self.dp[i][j]
            elif (j - i) == n - 1:
                self.dp[i][j] = 0
                result = 0
            elif (j - i) % 2 == 0:
                self.dp[i][j] = self.calc(i - 1, j) if array[i - 1] > array[j + 1] else self.calc(i, j + 1)
                result = self.dp[i][j]
            else:
                v1 = self.calc(i - 1, j) + array[i - 1]
                v2 = self.calc(i, j + 1) + array[j + 1]
                self.dp[i][j] = max(v1, v2)
                result = self.dp[i][j]
            return result

    helper = Helper(n)
    outputs = []
    for idx in range(n):
        res = helper.calc(idx, idx) + array[idx]
        outputs.append(res)
    print(max(outputs))

main()