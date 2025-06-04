class OrangePackagingCostOptimizer:
    class OrangeBatch:
        def __init__(self, oranges):
            self.oranges = oranges
            self.size = len(oranges)
            self.max_size = max(oranges)
            self.min_size = min(oranges)

        def cost(self, K):
            return K + self.size * (self.max_size - self.min_size)

    class OrangeConveyorBelt:
        def __init__(self, sizes):
            self.sizes = sizes
            self.N = len(sizes)

        def get_subbatch(self, start, end):
            return OrangePackagingCostOptimizer.OrangeBatch(self.sizes[start:end])

    def __init__(self, N, M, K, sizes):
        self.N = N
        self.M = M
        self.K = K
        self.conveyor = self.OrangeConveyorBelt(sizes)
        self.dp_cache = [None] * (N + 1)
        self.dp_cache[0] = 0

    def optimize(self):
        from collections import deque
        import sys

        # To avoid recalculating min and max repeatedly, we use a sliding window approach with deque
        dp = [sys.maxsize] * (self.N + 1)
        dp[0] = 0

        for i in range(1, self.N + 1):
            max_deque = deque()
            min_deque = deque()
            for j in range(i, max(i - self.M, 0), -1):
                x = self.conveyor.sizes[j - 1]
                while max_deque and max_deque[0] < x:
                    max_deque.popleft()
                max_deque.appendleft(x)
                while min_deque and min_deque[0] > x:
                    min_deque.popleft()
                min_deque.appendleft(x)
                max_orange = max_deque[-1]
                min_orange = min_deque[-1]
                size = i - j + 1
                cost = self.K + size * (max_orange - min_orange)
                if dp[j - 1] + cost < dp[i]:
                    dp[i] = dp[j - 1] + cost
                    
        return dp[self.N]

def main():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    sizes = [int(input()) for _ in range(N)]

    optimizer = OrangePackagingCostOptimizer(N, M, K, sizes)
    result = optimizer.optimize()
    print(result)

if __name__ == "__main__":
    main()