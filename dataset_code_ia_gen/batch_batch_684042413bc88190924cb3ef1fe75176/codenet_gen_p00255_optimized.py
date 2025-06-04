import sys
import threading

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        p = list(map(int, input().split()))
        j = list(map(int, input().split()))
        dp = [0]*(n+1)
        # dp[i]: max salary using first i pipes
        for i in range(1, n+1):
            # not connect pipe i with i-1
            dp[i] = dp[i-1] + p[i-1]
            if i > 1:
                # connect pipe i-1 and i into one
                combined = dp[i-2] + (p[i-2] + j[i-2] + p[i-1])*1
                # check if it's better to combine or not; but combined represents merging two pipes into one pipe,
                # so count of pipes decreases by one, but salary depends on count*sum_length
                # here dp contains max salary so far for i pipes, so for combined: using (i-2) pipes + combined pipe
                # actually we must account for count * sum_length.
                # To handle multiple merges, we should keep dp with maximum sum possible with partitions.

                # Actually problem is equivalent to maximizing sum over groups:
                # sum over groups: group_count * group_length
                # where groups are formed by merging adjacent pipes with joints.

                # So, at each step, dp[i] = max over k < i of dp[k] + (i-k)*(sum_pipes + sum_joints in [k,i))

                # Optimize with prefix sums:

                pass

        # Implementation with prefix sums and DP:

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    while True:
        n = int(input())
        if n == 0:
            break
        p = list(map(int, input().split()))
        j = list(map(int, input().split()))
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + p[i]
        prefix_j = [0]*(n)
        for i in range(n-1):
            prefix_j[i+1] = prefix_j[i] + j[i]

        # dp[i]: max salary using first i pipes
        dp = [0]*(n+1)
        # To optimize naive O(n^2), use convex hull trick

        # Each segment (k,i) length sum = prefix[i] - prefix[k] + prefix_j[i-1] - prefix_j[k]
        # count = i - k
        # value = count * segment_length + dp[k] = (i-k)*(prefix[i]-prefix[k]+prefix_j[i-1]-prefix_j[k]) + dp[k]
        # = (i-k)*(prefix[i] + prefix_j[i-1]) - (i-k)*(prefix[k] + prefix_j[k]) + dp[k]

        # We want to compute dp[i] = max over k < i of dp[k] + (i-k)* (prefix[i]+prefix_j[i-1]) - (i-k)*(prefix[k]+prefix_j[k])
        # = max over k < i of dp[k] - (prefix[k]+prefix_j[k]) * (i-k) + (i-k)*(prefix[i]+prefix_j[i-1])
        # since prefix[i]+prefix_j[i-1] is constant for given i, dp[i] = (prefix[i]+prefix_j[i-1])*i + max_k[dp[k] - (prefix[k]+prefix_j[k])*i - dp[k] + (prefix[k]+prefix_j[k])*k]

        # Rearranged for easier DP and convex hull usage:

        # Let A = prefix[i] + prefix_j[i-1]
        # Then dp[i] = max over k < i of dp[k] + (i-k)*A - (i-k)* B_k, where B_k = prefix[k]+prefix_j[k]
        # = max_k (dp[k] - B_k*(-k) ) + i*(A - B_k)

        # Let's build lines: y = m*x + c with m=B_k, c=dp[k] - B_k*k
        # At dp[i], x = i, value = line(x) + i*A

        # So we maintain lines with slope = B_k and intercept = dp[k] - B_k*k
        # and query at x=i, get max line value, then add i*A to get dp[i]

        class ConvexHull:
            def __init__(self):
                self.lines = []
                self.pos = 0

            # add line m x + b, slopes m in increasing order
            def add(self, m, b):
                while len(self.lines) >= 2 and self._is_bad(self.lines[-2], self.lines[-1], (m, b)):
                    self.lines.pop()
                self.lines.append((m, b))

            def _is_bad(self, l1, l2, l3):
                # Check if l2 is unnecessary
                return (l2[1]-l1[1])*(l1[0]-l3[0]) >= (l3[1]-l1[1])*(l1[0]-l2[0])

            def query(self, x):
                if not self.lines:
                    return -float('inf')
                # Move pos to best line for x
                while self.pos+1 < len(self.lines) and self._value(self.lines[self.pos], x) <= self._value(self.lines[self.pos+1], x):
                    self.pos += 1
                return self._value(self.lines[self.pos], x)

            def _value(self, line, x):
                return line[0]*x + line[1]

        dp[0] = 0
        ch = ConvexHull()
        B0 = prefix[0] + prefix_j[0]  # prefix_j[0] = 0
        ch.add(B0, dp[0] - B0*0)

        for i in range(1, n+1):
            A = prefix[i] + prefix_j[i-1] if i > 0 else 0
            val = ch.query(i) + i*A
            dp[i] = val
            if i < n:
                B = prefix[i] + prefix_j[i]
                ch.add(B, dp[i] - B*i)

        print(dp[n])

threading.Thread(target=main).start()