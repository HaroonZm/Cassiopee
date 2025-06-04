import sys
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())
U=input()
A=list(map(int,input().split()))

edges=[]
for _ in range(M):
    s,t,b=map(int,input().split())
    edges.append((s-1,t-1,b))

# 2-SAT implementation for optimization:
# Each ghost can have two states: original facing direction (x=False), flipped (x=True)

# We want to minimize: sum of A_i * flipped_i + sum of B_i * conflict(pair)

# conflict: i-th ghost facing right and j-th ghost facing left, with i<j.

# Define function to get final direction given original direction and flip state
def facing(i,flip):
    if flip:
        return 'L' if U[i]=='R' else 'R'
    else:
        return U[i]

# Approach:
# For each constraint (s,t,b), if s faces right and t faces left, cost b occurs.
# This is:
# If facing(s,flip_s)=='R' and facing(t,flip_t)=='L' => cost b
# So conflict occurs only in states where:
# (facing(s,flip_s)=='R') AND (facing(t,flip_t)=='L')
# This condition can be rewritten in terms of flip_s and flip_t.

# We'll model the problem in terms of 2*N boolean variables (flip or not flip)
# We want to choose flips to minimize sum of flip costs plus sum of conflict costs
# We can solve this as a min-cut problem.

# Build flow graph for min-cut solution:

# Node indexing:
# For each i, two nodes: i and i+N represent flip_i = False and flip_i = True respectively.
# However, since we want to assign flip or not flip, but flip_i is a boolean.
# Actually, it's better to model each ghost with a single variable indicating flip or not.

# But since cost A_i applies if flip_i=True, cost 0 if flip_i=False.

# For conflict edges:
# If conflict occurs only if (flip_s, flip_t) in some set of combinations (flip or not flip),
# we can add edges to force paying the cost if that combination is chosen.

# We'll construct a graph with 2*N nodes: for each i, two nodes: i (flip_i=0), i+N (flip_i=1)
# We'll add edges to prohibit impossible assignments and encode the cost.

# Use the method from "Min cut with vertex costs":
# For each variable, model flip cost as edge from source or sink accordingly.

# Step 1: Build graph with 2*N+2 nodes: source (2N) and sink (2N+1)

# Step 2: For each ghost i:
#   Add edge from source to node i (flip_i=0) with capacity 0 (no cost)
#   Add edge from node i+N to sink with capacity A[i] (cost to flip)
#   Add infinite capacity edges between i and i+N to enforce exactly one choice?
# Actually, since we only decide flip or not flip, we can model as single vertex with cost A_i if flip=1

# Let's do a standard construction for 'vertex-capacitated' min cut:

# We split each variable into two nodes: in and out.
# The capacity on edge in->out is the vertex cost.
# Then, edges between variables go from out of one to in of other.

# But as N is up to 500, and M up to 1000, this approach is feasible.

from collections import deque

INF=10**9

class MaxFlow:
    def __init__(self,N):
        self.N=N
        self.graph=[[] for _ in range(N)]
    def add(self,a,b,c):
        self.graph[a].append([b,c,len(self.graph[b])])
        self.graph[b].append([a,0,len(self.graph[a])-1])
    def bfs(self,s,t,level):
        q=deque()
        q.append(s)
        level[s]=0
        while q:
            v=q.popleft()
            for i,(to,cap,rev) in enumerate(self.graph[v]):
                if cap>0 and level[to]<0:
                    level[to]=level[v]+1
                    q.append(to)
        return level[t]>=0
    def dfs(self,v,t,f,level,it):
        if v==t: return f
        while it[v]<len(self.graph[v]):
            to,cap,rev=self.graph[v][it[v]]
            if cap>0 and level[to]>level[v]:
                d=self.dfs(to,t,min(f,cap),level,it)
                if d>0:
                    self.graph[v][it[v]][1]-=d
                    self.graph[to][rev][1]+=d
                    return d
            it[v]+=1
        return 0
    def max_flow(self,s,t):
        flow=0
        level=[-1]*self.N
        while self.bfs(s,t,level):
            it=[0]*self.N
            while True:
                f=self.dfs(s,t,INF,level,it)
                if f==0:
                    break
                flow+=f
            level=[-1]*self.N
        return flow

# Nodes:
# For each ghost i:
# - in node: i
# - out node: i+N
# source: 2N
# sink: 2N+1

# Vertex capacity edges: in_i -> out_i with capacity A[i] (flip cost)
# If flip=1, pay A[i]. So cutting in_i->out_i edge corresponds to flipping 
# leaving it corresponds to no flip.

# For edges representing constraints causing cost B_i:
# For each conflict tuple (s,t,b):
# The conflict occurs if:
# facing(s,flip_s) == 'R' and facing(t,flip_t) == 'L'

# For each variable, flip_s and flip_t in {0,1}
# For these 4 combinations, we check if condition holds and if so cost b applies.

# We'll transform the conflict cost into edges between the variables' out->in nodes, with capacity b,
# so cutting these edges corresponds to paying cost b if that conflict state is chosen.

# To encode this, build edges forbidding conflicting states.

# The standard is:

# For each pair of variables with states (flip_s, flip_t) that cause conflict, we add edges:

# For pair (s,t):

# Add edges to prevent the assignment (flip_s, flip_t) without paying b.

# But since we pay B_i if that state occurs, we can model with edges from out of s to in of t or vice versa with capacity B_i

# Construct implication graph accordingly.

def node_in(i):
    return i
def node_out(i):
    return i+N

size=2*N+2
source=2*N
sink=2*N+1
mf=MaxFlow(size)

# Add vertex capacity edges: in->out with capacity = A[i]
for i in range(N):
    mf.add(node_in(i),node_out(i),A[i])

# For each ghost:
# connect source to in_i with INF capacity (to allow selection), and out_i to sink with INF capacity to allow flow
# But this is not needed since capacity on in->out accounts for cost.

# For conflict edges:
for s,t,b in edges:
    # Check for which (flip_s,flip_t) conflict occurs
    # Flip_s and flip_t in {0,1}
    # facing(s,flip_s)
    # facing(t,flip_t)
    # conflict if facing(s,flip_s)=='R' and facing(t,flip_t)=='L'
    conflict_states=[]
    for fs in [0,1]:
        for ft in [0,1]:
            dir_s = facing(s,fs)
            dir_t = facing(t,ft)
            if dir_s=='R' and dir_t=='L':
                conflict_states.append( (fs,ft) )
    # For each conflict_state, add edges to enforce paying cost b if those flips chosen
    # To model this with min-cut:
    # We add edges between nodes corresponding to variables assignment
    # Using standard 2-literal clause transformation:
    # For conflict (fs,ft),
    # encode that if flip_s=fs and flip_t=ft then pay cost b.

    # We set up edges from out_s or out_t nodes so that cutting them costs b if that state set
    # That can be encoded as:
    # Add edge from node_out(s) if fs=1 else node_in(s) to node_in(t) if ft=0 else node_out(t) with capacity b
    # But careful:
    # Reference: https://atcoder.jp/contests/abc222/editorial/2723
    # Here, we use the standard construction for cost on combination of variable assignments:
    # Add edge from s_node to t_node with capacity b, where s_node and t_node depends on chosen flip/unflip.

    # Since node_in represents flip=0, node_out represents flip=1.

    from_node = node_out(s) if fs==1 else node_in(s)
    to_node = node_in(t) if ft==0 else node_out(t)
    mf.add(from_node,to_node,b)

# The min-cut will correspond to minimal cost.

# Calculate max-flow from source to sink:

flow = mf.max_flow(source,sink)
print(flow)