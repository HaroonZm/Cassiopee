import sys
import math

def pos_at_time(robot, t):
    times = robot['times']
    xs = robot['xs']
    ys = robot['ys']
    vxs = robot['vxs']
    vys = robot['vys']
    # Find interval containing t
    for i in range(len(times)-1):
        if times[i] <= t <= times[i+1]:
            dt = t - times[i]
            x = xs[i] + vxs[i]*dt
            y = ys[i] + vys[i]*dt
            return (x, y)
    # If t == times[-1]
    if t == times[-1]:
        return (xs[-1], ys[-1])
    # Just in case
    return (xs[0], ys[0])

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def reachable(robots, R, t):
    # Returns list of sets of connected robots at time t
    n = len(robots)
    adj = [[] for _ in range(n)]
    positions = [pos_at_time(robots[i], t) for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = dist(positions[i], positions[j])
            if d < R + 1e-10:
                adj[i].append(j)
                adj[j].append(i)
    # Build connected components
    visited = [False]*n
    groups = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            comp = []
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    comp.append(u)
                    for w in adj[u]:
                        if not visited[w]:
                            stack.append(w)
            groups.append(comp)
    return groups

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        NTR = line.strip().split()
        if len(NTR) < 3:
            continue
        N, T, R = map(int, NTR)
        if N==0 and T==0 and R==0:
            break
        robots = []
        for _ in range(N):
            # read nickname
            while True:
                nick = sys.stdin.readline().strip()
                if nick != '':
                    break
            # read times and velocities
            times = []
            xs = []
            ys = []
            vxs = []
            vys = []
            # read first line: t0 x0 y0
            while True:
                line = sys.stdin.readline()
                if line.strip() != '':
                    break
            parts = line.strip().split()
            t0 = int(parts[0])
            x0 = int(parts[1])
            y0 = int(parts[2])
            times.append(t0)
            xs.append(x0)
            ys.append(y0)
            vxs.append(0)
            vys.append(0)
            # read next lines until last t_k == T
            while True:
                line = sys.stdin.readline()
                if line.strip() == '':
                    continue
                parts = line.strip().split()
                t = int(parts[0])
                vx = int(parts[1])
                vy = int(parts[2])
                times.append(t)
                # position at t is previous position + velocity*(t-prev_t)?
                # No, t is end time, vx,vy active from times[-2] to t
                # For positions, we store at times[i]: pos = xs[i], ys[i]
                # Next positions will be computed with velocity
                # We must compute xs and ys at times because they give t and velocities
                # So to get xs and ys at t, need to compute from previous
                dt = t - times[-2]
                x_new = xs[-1] + vxs[-1]*dt
                y_new = ys[-1] + vys[-1]*dt
                xs.append(x_new)
                ys.append(y_new)
                vxs.append(vx)
                vys.append(vy)
                if t == T:
                    break
            robot = {'nick':nick, 'times':times, 'xs':xs, 'ys':ys, 'vxs':vxs, 'vys':vys}
            robots.append(robot)

        # We want to simulate from 0 to T
        # data spread initially from first robot at time 0
        # since data transfer is instantaneous, data propagate in clusters of connected robots at each time
        # but robots move, so connectivity changes
        # We'll simulate time step by step
        # To keep it simple: check every integer time from 0 to T (T <=1000)
        # For better we can check all integer times plus T
        # For each time, find connected components, for each group if any member has data, all get data

        have_data = set()
        have_data.add(0) # first robot has data initially

        # We'll do a BFS connectivity on dynamic graph for each time
        # To propagate data between times, data only accumulate

        for t in range(0, T+1):
            groups = reachable(robots, R, t)
            # For each group, if any has data, all get data
            new_data = set()
            for g in groups:
                if any(r in have_data for r in g):
                    for r in g:
                        new_data.add(r)
            have_data = have_data.union(new_data)

        # print nicknames of robots with data in dictionary order
        result = [robots[i]['nick'] for i in have_data]
        result.sort()
        for r in result:
            print(r)

if __name__ == '__main__':
    main()