INF = 0x7fffffff

def create_level_list(V):
    return [0] * V

def create_iter_list(V):
    return [0] * V

def create_edge_list(V):
    return [[] for _ in range(V)]

def create_zero_matrix(N):
    return [[0 for _ in range(N)] for _ in range(N)]

def fragment_add_edge(edge, frm, to, cap):
    f = len(edge[frm])
    t = len(edge[to])
    edge[frm].append([to, cap, t])
    edge[to].append([frm, cap, f])

def fragment_bfs_init_level(level, V, s):
    for i in range(V):
        level[i] = -1
    level[s] = 0

def fragment_bfs_process_vertex(Q, v, edge, level):
    for to, cap, rev in edge[v]:
        if cap > 0 and level[to] < 0:
            level[to] = level[v] + 1
            Q.append(to)

def fragment_bfs(edge, level, V, s):
    fragment_bfs_init_level(level, V, s)
    Q = []
    Q.append(s)
    while Q:
        v = Q.pop()
        fragment_bfs_process_vertex(Q, v, edge, level)

def fragment_dfs_check_end(v, t, f):
    if v == t:
        return f
    return None

def fragment_dfs_inner_loop(edge, iterl, level, v, t, f):
    k = iterl[v]
    while k < len(edge[v]):
        to, cap, rev = edge[v][k]
        if cap > 0 and level[v] < level[to]:
            d = fragment_dfs_all(edge, iterl, level, to, t, min(f, cap))
            if d > 0:
                edge[v][k][1] -= d
                edge[to][rev][1] += d
                return d
        iterl[v] += 1
        k += 1
    return 0

def fragment_dfs_all(edge, iterl, level, v, t, f):
    if fragment_dfs_check_end(v, t, f) is not None:
        return f
    return fragment_dfs_inner_loop(edge, iterl, level, v, t, f)

def fragment_maxflow_main(edge, level, iterl, V, s, t):
    flow = 0
    while True:
        fragment_bfs(edge, level, V, s)
        if level[t] < 0:
            break
        for i in range(V):
            iterl[i] = 0
        while True:
            f = fragment_dfs_all(edge, iterl, level, s, t, INF)
            if f <= 0:
                break
            flow += f
    return flow

class Donic:
    def __init__(self, V):
        self.V = V
        self.level = create_level_list(V)
        self.iter = create_iter_list(V)
        self.edge = create_edge_list(V)

    def add_edge(self, frm, to, cap):
        fragment_add_edge(self.edge, frm, to, cap)

    def bfs(self, s):
        fragment_bfs(self.edge, self.level, self.V, s)

    def dfs(self, v, t, f):
        return fragment_dfs_all(self.edge, self.iter, self.level, v, t, f)

    def maxFlow(self, s, t):
        return fragment_maxflow_main(self.edge, self.level, self.iter, self.V, s, t)

def fragment_input_split_and_map():
    return list(map(int, input().split()))

def fragment_matrix_assign(mat, i, j, val):
    mat[i][j] = val

def fragment_add_edge_dir_id(dir, id_mat, d, x, y, eid):
    fragment_matrix_assign(dir, y, x, 1)
    fragment_matrix_assign(id_mat, y, x, eid)
    d.add_edge(x, y, 1)

def fragment_process_flow_edges(N, d_edge, dir_mat, id_mat):
    ans = []
    for i in range(N):
        for to, cap, rev in d_edge[i]:
            if cap < 1 and dir_mat[i][to]:
                ans.append(id_mat[i][to])
    return ans

def fragment_sort(ans):
    ans.sort()

def fragment_output_result(ans):
    print(len(ans))
    if len(ans) > 0:
        print(*ans, sep='\n')

def main():
    N, M = fragment_input_split_and_map()
    dir_mat = create_zero_matrix(N)
    id_mat = create_zero_matrix(N)
    d = Donic(N)
    for i in range(M):
        x, y = fragment_input_split_and_map()
        x -= 1
        y -= 1
        fragment_add_edge_dir_id(dir_mat, id_mat, d, x, y, i+1)
    S, T = fragment_input_split_and_map()
    maxflow = d.maxFlow(S-1, T-1)
    print(maxflow)
    ans = fragment_process_flow_edges(N, d.edge, dir_mat, id_mat)
    fragment_sort(ans)
    fragment_output_result(ans)

main()