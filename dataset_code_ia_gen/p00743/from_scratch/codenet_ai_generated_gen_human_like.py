import sys
import math
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        s, g = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            x, y, d, c = map(int, input().split())
            graph[x].append((y,d,c))
            graph[y].append((x,d,c))

        # State: (time, city, speed, last_city)
        # last_city used to avoid u-turns: can't immediately go back to last_city
        # Start: city=s, speed=0, but first road speed must be 1, so speed=1 leaving s is required
        # So initial moves must have speed=1 on the first road out of s.

        # dist[city][speed][last_city] = min time to reach city with speed coming from last_city
        # We'll store last_city as 0 if none (initial position)
        INF = float('inf')
        dist = [[[INF]*(n+1) for _ in range(31)] for _ in range(n+1)]

        pq = []
        # Initially at s, speed must be 0 or 1? The problem says the first road leaving s must be run at speed 1.
        # So no speed 0 on edges; speed must be 1.
        # For all neighbors of s, with speed=1 when traveling s->neighbor

        # But car arrives at s, initial speed is 0 effectively
        # So we can set the state as city=s, speed=0, last_city=0, dist=0, then expand
        # But we must only allow speed=1 as the first edge speed out.

        # We'll push initial state (s, speed=0, last_city=0) with time 0
        # When we expand, only speed 1 is allowed from s

        dist[s][0][0] = 0.0
        heapq.heappush(pq,(0.0,s,0,0)) # time, city, speed, last_city

        while pq:
            time, city, speed, last_city = heapq.heappop(pq)
            if dist[city][speed][last_city] < time - 1e-12:
                continue
            if city == g and speed == 1:
                # We reached goal city g at speed 1 => done
                print(f"{time:.6f}")
                break

            # next possible speeds: speed-1,speed,speed+1 (>=1 and <=30)
            for nspeed in [speed-1,speed, speed+1]:
                if nspeed < 1 or nspeed > 30:
                    continue
                for nxt, d, c_limit in graph[city]:
                    if nxt == last_city:
                        # no u-turn
                        continue
                    if nspeed > c_limit:
                        # speed limit
                        continue
                    # Time to travel edge: d / nspeed
                    new_time = time + d / nspeed

                    # If at start city and speed == 0 (initial state), only allow nspeed=1 out
                    # Actually this is handled above by nspeed>=1 and dist s 0 0 initializing state.

                    if dist[nxt][nspeed][city] > new_time + 1e-12:
                        dist[nxt][nspeed][city] = new_time
                        heapq.heappush(pq,(new_time,nxt,nspeed,city))
        else:
            print("unreachable")

if __name__ == "__main__":
    solve()