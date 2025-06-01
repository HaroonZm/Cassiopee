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
        prefix_p = [0]*(n+1)
        for i in range(n):
            prefix_p[i+1] = prefix_p[i] + p[i]
        dp = [0]*(n+1)
        dp[1] = p[0]
        for i in range(2, n+1):
            # option 1: don't connect pipe i-1 (dp[i-1] + p[i-1])
            # option 2: connect pipe i-2 and i-1 as one segment:
            # dp[i-2] + (p[i-2] + j[i-2] + p[i-1]) *1
            # but actually, we need to consider the number of segments: 
            # connecting reduces segment count by 1, so multiply by segments count accordingly.
            # The problem is to maximize sum of segment lengths * number of segments
            
            # The DP approach here:
            # dp[i] = max over k in [i-1]: dp[k] + (sum of p and j from k+1 to i)
            # We can optimize by keeping dp and sum arrays.
            # But the problem reduces to:
            # For each i, dp[i] = max over k < i of dp[k] + (i-k)*(segment_length from k+1 to i)
            # which can be solved with Convex Hull Trick because (i-k) and segment_length are linear.
            # To implement CHT, we rewrite dp[i] = max over k < i of dp[k] + (i-k)*S(k+1,i)
            # where S(k+1,i) = prefix_p[i] - prefix_p[k] + sum_joints(k+1,i-1)
            
            # First, compute cumulative sums of joints
            # We'll move CHT outside for performance
            pass

        # To implement efficiently, we use Convex Hull Trick:
        # Let sumPi be prefix sum of p
        # Let sumJi be prefix sum of j
        prefix_j = [0]*(n)
        for i in range(n-1):
            prefix_j[i+1] = prefix_j[i] + j[i]

        # dp[i] = max_{k < i} dp[k] + (i - k) * (sum_p(k+1 to i) + sum_j(k+1 to i-1))
        #       = max_{k < i} dp[k] + (i - k) * ((prefix_p[i] - prefix_p[k]) + (prefix_j[i-1] - prefix_j[k]))
        #       = max_{k < i} dp[k] + (i-k) * (prefix_p[i] + prefix_j[i-1] - prefix_p[k] - prefix_j[k])

        # dp[i] = max_{k < i} dp[k] - (prefix_p[k] + prefix_j[k])*(i-k) + (i-k)*(prefix_p[i] + prefix_j[i-1])
        # Because prefix_p[i] and prefix_j[i-1] are constants for i, we need to maximize:
        # dp[k] - (prefix_p[k] + prefix_j[k])*(i-k) = dp[k] - (prefix_p[k] + prefix_j[k]) * i + (prefix_p[k] + prefix_j[k]) * k
        # which is linear in i: y = m * x + b with x = i
        # So we maintain lines: slope m = (prefix_p[k] + prefix_j[k]) and intercept b = dp[k] - m * k
        # We want dp[i] = max over lines { line.value(i)} + const

        class LineContainer:
            def __init__(self):
                self.lines = []
            # Insertion of convex hull lines for max value queries
            def bad(self, l1, l2, l3):
                # return True if l2 is always worse than l3 or l1
                return (l3[1]-l1[1])*(l1[0]-l2[0]) >= (l2[1]-l1[1])*(l1[0]-l3[0])
            def add(self, m, b):
                self.lines.append((m,b))
                while len(self.lines)>=3 and self.bad(self.lines[-3], self.lines[-2], self.lines[-1]):
                    self.lines.pop(-2)
            def query(self, x):
                l, r = 0, len(self.lines)-1
                while l<r:
                    mid = (l+r)//2
                    if self.lines[mid][0]*x + self.lines[mid][1] < self.lines[mid+1][0]*x + self.lines[mid+1][1]:
                        l = mid+1
                    else:
                        r = mid
                return self.lines[l][0]*x + self.lines[l][1]

        cht = LineContainer()
        dp = [0]*(n+1)
        # Base case dp[0] = 0 line added:
        # m = prefix_p[0] + prefix_j[0] =0+0=0, b = dp[0] - m*0=0
        cht.add(0,0)
        for i in range(1,n+1):
            val = prefix_p[i] + prefix_j[i-1]
            dp[i] = cht.query(i) + i*val
            m = prefix_p[i] + prefix_j[i]
            b = dp[i] - m * i
            cht.add(m, b)
        print(dp[n])

threading.Thread(target=main).start()