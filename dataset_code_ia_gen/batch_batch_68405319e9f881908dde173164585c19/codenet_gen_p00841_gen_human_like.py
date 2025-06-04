import sys
import math

def time_for_segment(start_dist, end_dist, r, v, e, f):
    total_time = 0.0
    # distance from last tire change point to current position
    # x goes from start_dist to end_dist - 1 because each km is from x to x+1
    for x in range(start_dist, end_dist):
        dist_from_change = x - start_dist
        if dist_from_change >= r:
            denom = v - e * (dist_from_change - r)
        else:
            denom = v - f * (r - dist_from_change)
        # denom guaranteed >= 0.01 as per problem statement
        total_time += 1.0 / denom
    return total_time

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if not line or line == '0':
            break
        n = int(line)
        a = list(map(int, input_lines[idx].split()))
        idx += 1
        b = float(input_lines[idx])
        idx += 1
        r, v, e, f = map(float, input_lines[idx].split())
        r = int(r)
        idx += 1

        # Positions: start at 0, checkpoints a[0],...,a[n-1]
        # We'll consider positions as [0] + a
        positions = [0] + a

        # dp[i] = minimal time to reach checkpoint i (0-based in positions)
        dp = [math.inf] * (n + 1)
        dp[0] = 0.0

        for i in range(n):
            # For next change point j in i+1..n
            for j in range(i+1, n+1):
                dist_start = positions[i]
                dist_end = positions[j]
                segment_time = time_for_segment(dist_start, dist_end, r, v, e, f)
                # Add tire change time if j != 0 (but j=0 is start, so no tire change there)
                change_time = b if j < n else 0.0
                # Actually, from the problem statement, changing tires at checkpoint i < n takes b sec
                # But if j==n, it's the goal, no tire change after the last segment
                # Actually, tire change time applies when we change tires at i-th checkpoint (before going to j)
                # The problem states: At the i-th checkpoint (i < n), tires can be changed. Choosing whether or not to change.
                # So the model is: dp at i means we already made choices up to i.
                # So when going from i to j we can choose to change tires at checkpoint i (except i=0 which is start).
                # But start point 0 is not a checkpoint, so no tire change cost there.
                # The problem is that we only pay tire change time when changing tires at a checkpoint.
                # Sequencing:
                # - If we change tires at i-th checkpoint, pay b seconds plus run the segment i->j.
                # - If not, no tire change time.
                # But we don't know if at checkpoint i we changed or not.
                # So two possibilities: change or not at checkpoint i.
                # Actually, problem states:
                # "At the i-th checkpoint (i < n), tires can be changed or not. It takes b sec to change tires."
                # The dp model should represent the state of the last tire change.
                # Let's handle this by enumerating dp states as the last checkpoint where we changed tires.
                # We'll store dp[last_change_checkpoint] = minimal time to reach that checkpoint with the last tire change at that checkpoint.

                # So we want:
                # For each i=last change checkpoint, try extending to j=next checkpoint,
                # for j < n: we change tires there (add b),
                # for j == n (goal) no tire change time added at j,
                # then dp[j] = min(dp[j], dp[i] + segment_time + (b if j < n else 0))

        # So we do that:
                dp[j] = min(dp[j], dp[i] + segment_time + (b if j < n else 0))

        print(f"{dp[n]:.7f}")

if __name__ == "__main__":
    solve()