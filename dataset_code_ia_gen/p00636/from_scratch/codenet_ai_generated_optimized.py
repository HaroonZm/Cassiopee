import sys
import math
import heapq

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def can_stand(pos, monsters):
    dists = [dist(pos, m) for m in monsters]
    if not dists:
        return True
    mind = min(dists)
    return dists.count(mind) >= 2

def generate_points(monsters):
    pts = []
    # add start and goal boundaries as points (y from 0 to 4 in steps)
    for y in [i * 0.5 for i in range(9)]:
        start = (0.0, y)
        goal = (4.0, y)
        if can_stand(start, monsters):
            pts.append(start)
        if can_stand(goal, monsters):
            pts.append(goal)
    for m in monsters:
        if can_stand(m, monsters):
            pts.append(m)
    return pts

def build_graph(points, monsters):
    n = len(points)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            p1, p2 = points[i], points[j]
            # check path validity: sample points along segment
            steps = max(10, int(dist(p1,p2)*5))
            valid = True
            for k in range(steps+1):
                t = k/steps
                x = p1[0] + (p2[0]-p1[0])*t
                y = p1[1] + (p2[1]-p1[1])*t
                if not can_stand((x,y), monsters):
                    valid = False
                    break
            if valid:
                d = dist(p1,p2)
                graph[i].append((j,d))
                graph[j].append((i,d))
    return graph

def dijkstra(graph, start_indices, goal_indices):
    n = len(graph)
    dist_arr = [math.inf]*n
    hq = []
    for si in start_indices:
        dist_arr[si] = 0.0
        heapq.heappush(hq,(0.0,si))
    goal_set = set(goal_indices)
    while hq:
        cd, u = heapq.heappop(hq)
        if dist_arr[u]<cd:
            continue
        if u in goal_set:
            return cd
        for v,w in graph[u]:
            nd = cd+w
            if nd<dist_arr[v]:
                dist_arr[v]=nd
                heapq.heappush(hq,(nd,v))
    return math.inf

def main():
    input=sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = int(n)
        if n==0:
            break
        monsters = [tuple(map(float, input().split())) for _ in range(n)]
        points = generate_points(monsters)
        if not points:
            print("impossible")
            continue
        graph = build_graph(points, monsters)
        start_indices = [i for i,p in enumerate(points) if abs(p[0]-0.0)<1e-9 and 0.0<=p[1]<=4.0]
        goal_indices = [i for i,p in enumerate(points) if abs(p[0]-4.0)<1e-9 and 0.0<=p[1]<=4.0]
        if not start_indices or not goal_indices:
            print("impossible")
            continue
        ans = dijkstra(graph,start_indices,goal_indices)
        if ans==math.inf:
            print("impossible")
        else:
            print(ans)

if __name__=="__main__":
    main()