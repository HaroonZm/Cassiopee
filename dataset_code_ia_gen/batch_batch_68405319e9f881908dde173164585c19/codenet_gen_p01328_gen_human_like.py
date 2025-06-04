import sys
import math

def assign_cats_to_feeders(N, M, cats, feeders):
    # Sort feeders by x coordinate for tie-breaking when distances are equal
    feeders_sorted = sorted(feeders)
    
    # Initialize feeding counts
    feed_counts = {x: 0 for x in feeders_sorted}
    
    for (cx, cy, ccount) in cats:
        min_dist = None
        chosen_feeder = None
        for fx in feeders_sorted:
            dist = math.sqrt((cx - fx)**2 + (cy)**2)
            if (min_dist is None) or (dist < min_dist) or (dist == min_dist and fx < chosen_feeder):
                min_dist = dist
                chosen_feeder = fx
        feed_counts[chosen_feeder] += ccount
    return max(feed_counts.values())

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N, M = map(int, line.strip().split())
        if N == 0 and M == 0:
            break
        cats = []
        for _ in range(N):
            x, y, c = map(int, input().strip().split())
            cats.append((x, y, c))
        feeders = []
        for _ in range(M):
            fx = int(input().strip())
            feeders.append(fx)
        result = assign_cats_to_feeders(N, M, cats, feeders)
        print(result)

if __name__ == "__main__":
    main()