import sys
import math

def time_interval(dist, r, v, e, f):
    # dist is interval length
    # return sum over 0..dist-1 of time per km
    # since dist can be up to 10000, we can't loop; need formula
    # total time = sum_{x=0}^{dist-1} 1/(v - e*(x - r)) if x >= r else 1/(v - f*(r - x))
    # x from 0 to dist-1
    # for x < r: 1/(v - f*(r - x)) = 1/(v - f*r + f*x)
    # for x >= r: 1/(v - e*(x - r)) = 1/(v - e*x + e*r)
    # so split sum at x=r
    # range x=0..dist-1
    # if dist <= r: all x < r case
    # else part for x<r and part for x>=r

    t = 0.0
    if dist == 0:
        return 0.0
    # sum for x in [0,min(dist,r)-1] : 1/(v - f*r + f*x)
    left_end = min(dist, r)
    if left_end > 0:
        a = v - f * r
        # sum_{x=0}^{left_end-1} 1/(a + f*x)
        # = (1/f) * (H_{(a/f)+(left_end-1)} - H_{(a/f)-1})
        # Harmonic partial sum for general denominator not trivial, approx by loop?
        # Since dist <= 10000, loop is acceptable here.
        for x in range(left_end):
            denom = v - f * r + f * x
            t += 1.0 / denom

    # sum for x in [r, dist-1] : 1/(v - e*(x - r)) = 1/(v - e*x + e*r)
    if dist > r:
        for x in range(r, dist):
            denom = v - e * (x - r)
            t += 1.0 / denom
    return t

def main():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx >= len(input):
            break
        n = input[idx]; idx+=1
        if n == '0':
            break
        n = int(n)
        a = list(map(int, input[idx:idx+n]))
        idx+=n
        b = float(input[idx]); idx+=1
        r = int(input[idx]); idx+=1
        v = float(input[idx]); idx+=1
        e = float(input[idx]); idx+=1
        f = float(input[idx]); idx+=1

        # DP: dp[i] = minimal time to reach checkpoint i (0-based), dp[0] = time from start to a[0]
        # We consider checkpoints from i=0 to n-1 (a indices)
        # Can change tires at i<n-1, or not
        # When changing tires at checkpoint i, add b seconds
        # For dp[j], try dp[i] + interval_time(a[j]-a[i], r, v, e, f) + (b if i < j -1 else 0)
        # But changing tires only allowed at checkpoints i<n, so between i and j we compute interval from last change (at i)
        # We can either change tires at i or not. Actually, at i, can decide to change or not, but dp is minimal time to reach i
        # We must track last changed checkpoint index.
        # Better use 2D DP: dp[i][c] minimal time to reach checkpoint i with last tire change at c,
        # where c <= i
        # For c in 0..i, dp[i][c] = min over k < i of dp[k][c] + time running from a[k] to a[i]
        # But if i != c, running without changing tires, so distance is a[i]-a[c]
        # At i, can choose to change tires or not:
        # If change tires at i:
        # dp[i][i] = min over c of dp[i][c] + b
        # If no change at i:
        # dp[i][c] = dp[i-1][c] + time from a[i-1] to a[i] with last change at c

        # But since changing allowed only at checkpoints, do this:
        # dp[i] = minimal time to reach i
        # For each k < i:
        # time running from a[k] to a[i] with last tire change at k
        # If k > 0, then add b for tire change at k to start this interval
        # Actually tire change time added at the start of interval except from start(0)
        # So for k=0 (start), no tire change
        # for k>0, tire change cost b at checkpoint k

        dp = [math.inf]*(n)
        dp[0] = time_interval(a[0], r, v, e, f)
        for i in range(1,n):
            # try all previous change points k
            for k in range(i):
                dist = a[i] - a[k]
                t_run = time_interval(dist, r, v, e, f)
                t_change = 0 if k == 0 else b
                cand = dp[k] + t_change + t_run
                if cand < dp[i]:
                    dp[i] = cand
        print(f"{dp[-1]:.10f}")

if __name__=="__main__":
    main()