import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        crossings = [input().strip() for _ in range(N)]
        M = int(input())
        questions = [input().strip() for _ in range(M)]

        street_id = {}
        ns = set()
        ew = set()
        edges = set()
        cnt = 0

        def get_id(s):
            nonlocal cnt
            if s not in street_id:
                street_id[s] = cnt
                cnt += 1
            return street_id[s]

        cross = []

        for c in crossings:
            a,b = c.split('-')
            A = get_id(a)
            B = get_id(b)
            cross.append((A,B))
            edges.add((A,B))

        # Determine orthogonality sets (no direct info, but a street is NS if appears first in crossing)
        # Heuristic: Streets appear in mixed order, so from inputs, we cannot assign orientation directly.
        # Instead, we use the order of crossing names: the first street in input crossings can be NS or EW.
        # We'll try both assumptions:
        # But problem says streets either NS or EW, and crossings are only between orthogonal streets.
        # So, for all crossings (A,B), A and B are orthogonal sets.
        # We build bipartition (graph) accordingly.

        # Build graph to find bipartition: edges between orthogonal streets
        adj = [[] for _ in range(cnt)]
        deg = [0]*cnt
        for A,B in cross:
            adj[A].append(B)
            adj[B].append(A)
            deg[A]+=1
            deg[B]+=1

        color = [-1]*cnt

        def dfs_color(u,c):
            color[u] = c
            for v in adj[u]:
                if color[v]<0:
                    if not dfs_color(v,c^1):
                        return False
                elif color[v]==c:
                    return False
            return True

        # Since streets are either NS or EW, and crossings only happen between orthogonal streets,
        # the street graph is bipartite, color parts are orientations.
        for i in range(cnt):
            if color[i]<0:
                if not dfs_color(i,0):
                    # impossible bipartition (not expected by problem)
                    pass

        # Build crossing sets for fast test if a crossing exists (input direction)
        cross_set = set(cross)

        # Equal strength:
        # A and B equal if
        # (1) both cross same third street C in input (that is, exist C such that C-A and C-B or A-C and B-C in input)
        # (2) no D such that D-A and B-D appear in input
        # (3) no E such that A-E and E-B appear in input

        # We build:
        # For each street s, in_in[s] = set of streets that cross to s (D where D-s in input)
        # out_out[s] = set of streets which s crosses (E where s-E in input)

        in_in = [set() for _ in range(cnt)]
        out_out = [set() for _ in range(cnt)]

        for A,B in cross:
            in_in[B].add(A)
            out_out[A].add(B)

        # For checking condition (1), we find if there is C with C-A and C-B crossing,
        # or A-C and B-C crossing.

        # We consider that to be equal strength, A and B must have a mutual neighbor C with following:
        # There exists C with (C,A) and (C,B) or (A,C) and (B,C) in cross_set.

        # Prepare for equal strength test:

        # We test pairs A,B in same orientation class to reduce pairs:
        # Because crossings only between orthogonal streets, equal strength between streets of same orientation.

        # Candidate pairs are pairs in same color group
        equal_pairs = []

        for cgroup in (0,1):
            group = [i for i in range(cnt) if color[i]==cgroup]
            gset = set(group)
            for i in range(len(group)):
                A = group[i]
                for j in range(i+1,len(group)):
                    B = group[j]
                    # Check condition (1): exists C with both connected to A and B with same direction
                    # Check all C: either C->A and C->B in cross_set or A->C and B->C in cross_set
                    foundC = False
                    # check C->A and C->B
                    common_in = in_in[A] & in_in[B]
                    # check A->C and B->C
                    common_out = out_out[A] & out_out[B]
                    if common_in or common_out:
                        # condition(2) no D with D-A and B-D
                        cond2 = True
                        for D in in_in[A]:
                            if (B,D) in cross_set:
                                cond2 = False
                                break
                        if not cond2:
                            continue
                        # condition(3) no E with A-E and E-B
                        cond3 = True
                        for E in out_out[A]:
                            if (E,B) in cross_set:
                                cond3 = False
                                break
                        if not cond3:
                            continue
                        # all conditions fulfilled
                        equal_pairs.append((A,B))

        parent = list(range(cnt))
        def find(u):
            while parent[u]!=u:
                parent[u]=parent[parent[u]]
                u=parent[u]
            return u
        def union(u,v):
            u=find(u)
            v=find(v)
            if u!=v:
                parent[v]=u

        for A,B in equal_pairs:
            union(A,B)

        # Build adjacency for stronger relation
        # stronger if there is a sequence A=A1, A2, ..., An=B with n>=2,
        # and for all consecutive Ai,Ai+1, either Ai-Ai+1 is input crossing (Ai stronger Ai+1)
        # or Ai and Ai+1 have equal strength

        # equal strength means in same union-find set
        # Build graph of stronger relation:
        # edges (A->B) if (A,B) in input crossing (A stronger B)

        # For equal strength, treat A,B same level, so we shrink equal strength classes into nodes:

        # Build node for each union-find class
        comp = {}
        comp_id = 0
        for i in range(cnt):
            r = find(i)
            if r not in comp:
                comp[r] = comp_id
                comp_id += 1

        # Build reduced graph according to crossings between reps
        adj_strong = [[] for _ in range(comp_id)]

        # For each crossing A-B in input, add edge from comp[A] to comp[B] if different.
        # For equal strength, merges nodes.

        for A,B in cross:
            a = comp[find(A)]
            b = comp[find(B)]
            if a!=b:
                adj_strong[a].append(b)

        # Floyd-Warshall or BFS from each node to find reachability?
        # Up to 200 streets, after union find less than 200 comps.

        reach = [set() for _ in range(comp_id)]
        for i in range(comp_id):
            reach[i].add(i)
        for i in range(comp_id):
            for v in adj_strong[i]:
                reach[i].add(v)

        # Floyd-Warshall
        changed = True
        while changed:
            changed = False
            for i in range(comp_id):
                newset = set(reach[i])
                for v in list(reach[i]):
                    newset |= reach[v]
                if len(newset)>len(reach[i]):
                    reach[i] = newset
                    changed = True

        # For each question: print YES if infer that two streets are orthogonal and X stronger than Y
        # Orthogonal means color differs
        # stronger means comp[X]'s reachable contains comp[Y]

        # The number of distinct streets equals cnt

        print(cnt)
        for q in questions:
            X,Y = q.split('-')
            if X not in street_id or Y not in street_id:
                print("NO")
                continue
            x,y = street_id[X],street_id[Y]
            if color[x]==color[y]:
                print("NO")
                continue
            a,b = comp[find(x)],comp[find(y)]
            if b in reach[a]:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()