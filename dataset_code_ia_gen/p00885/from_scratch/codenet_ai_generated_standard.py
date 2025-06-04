import sys
import heapq

def solve(n, balloons):
    # balloons: list of (p, t), sorted by t
    # States in priority queue: (distance_sum, time, idx, pos, carrying)
    # carrying: tuple sorted balloon indices currently carried
    house = 0
    max_carry = 3
    INF = 10**15
    # dp: (idx, pos, carrying) -> (time, distance)
    # idx: next balloon to catch
    # carrying: a tuple of balloons currently carried (sorted)
    from collections import defaultdict
    dp = {}

    # initial state: idx=0, pos=0, carrying=()
    # distance = 0, time = 0
    hq = []
    heapq.heappush(hq, (0, 0, 0, 0, ()))  # distance_sum, time, idx, pos, carrying

    def move_time(dist, k):
        return dist*(k+1)

    while hq:
        dist_sum, time, idx, pos, carrying = heapq.heappop(hq)
        key = (idx, pos, carrying)
        if key in dp:
            # If found with better or equal distance, skip
            if dp[key][0] <= time and dp[key][1] <= dist_sum:
                continue
        dp[key] = (time, dist_sum)

        if idx == n and len(carrying) == 0:
            # caught all and emptied carrying
            return "OK", dist_sum

        # Option 1: if carrying > 0, try to go to house and drop all (no cost, no time)
        if len(carrying) > 0:
            if (idx, house, ()) not in dp or dp[(idx, house, ())][0] > time or dp[(idx, house, ())][1] > dist_sum + abs(pos - house):
                new_dist = dist_sum + abs(pos - house)
                new_time = time + move_time(abs(pos - house), len(carrying))
                heapq.heappush(hq, (new_dist, new_time, idx, house, ()))

        # Option 2: try to catch next balloon if any
        if idx < n:
            p, t = balloons[idx]
            # Try to move from pos to p with current carrying
            travel_dist = abs(p - pos)
            travel_time = move_time(travel_dist, len(carrying))
            arrive_time = time + travel_time
            # We must arrive <= t else balloon bursts
            if arrive_time <= t:
                # catch balloon (adding idx to carrying)
                # check not exceed max carrying
                if len(carrying) < max_carry:
                    new_carry = tuple(sorted(carrying + (idx,)))
                    new_dist = dist_sum + travel_dist
                    new_time = arrive_time
                    key2 = (idx + 1, p, new_carry)
                    if key2 not in dp or dp[key2][0] > new_time or dp[key2][1] > new_dist:
                        heapq.heappush(hq, (new_dist, new_time, idx + 1, p, new_carry))
                else:
                    # cannot catch balloon now, must drop first (already covered with option 1)
                    pass
            else:
                # cannot reach balloon in time -> NG idx+1
                return "NG", idx + 1

    # If queue exhausted without returning OK or NG during iteration, means NG earliest balloon not caught
    return "NG", 1

def main():
    input=sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        balloons = []
        for _ in range(n):
            p,t = map(int,input().split())
            balloons.append((p,t))
        res = solve(n, balloons)
        print(res[0], res[1])

if __name__ == "__main__":
    main()