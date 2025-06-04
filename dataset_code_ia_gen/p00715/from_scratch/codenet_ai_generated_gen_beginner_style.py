def main():
    while True:
        N = input()
        if N == '0':
            break
        N = int(N)
        crossings = []
        streets = set()
        ns_streets = set()
        ew_streets = set()
        for _ in range(N):
            c = input()
            crossings.append(c)
            a,b = c.split('-')
            streets.add(a)
            streets.add(b)
        M = int(input())
        questions = []
        for _ in range(M):
            q = input()
            questions.append(q)
            a,b = q.split('-')
            streets.add(a)
            streets.add(b)
        # Build graph of crossings
        # streets are nodes, edges exist if streets cross
        graph = dict()
        for s in streets:
            graph[s] = set()
        # add edges from input crossings
        for c in crossings:
            a,b = c.split('-')
            graph[a].add(b)
            graph[b].add(a)
        # Deduce the orientation of streets by checking types of crossings
        # If two streets cross, one must be NS and the other EW
        # We guess orientation by coloring the graph as bipartite
        color = dict()
        def dfs_color(s, c_col):
            color[s] = c_col
            for neigh in graph[s]:
                if neigh in color:
                    if color[neigh] == c_col:
                        # conflict - not bipartite, but problem says city is Chinese plan so bipartite
                        pass
                else:
                    dfs_color(neigh, 1 - c_col)
        for st in streets:
            if st not in color:
                dfs_color(st, 0)
        for st in streets:
            if color[st] == 0:
                ns_streets.add(st)
            else:
                ew_streets.add(st)

        # Now determine equal strength relation
        # Two streets A and B have equal strength if:
        # (1) both cross the same third street C in the input
        # (2) there is no street D such that D-A and B-D appear in input
        # (3) there is no street E such that A-E and E-B appear in input

        # we consider only streets of the same orientation (equal strength only makes sense for streets in same direction)
        same_dir = [ns_streets, ew_streets]

        equal = dict()  # key: frozenset({A,B}), value: True if equal strength

        # function to check equal strength conditions for two same-direction streets A and B
        def check_equal(A,B):
            # condition (1): exist C such that C-A in input crossings AND C-B in input crossings
            # crossings are in crossings list; due to orientation, C crosses both A and B
            # So C is in other direction, crosses A and B
            # get streets crossing A and B
            crossA = graph[A]
            crossB = graph[B]
            common = crossA & crossB
            if not common:
                return False
            # condition (2):
            # no D such that D-A and B-D in input
            # D-A means edge from D to A
            # B-D means edge from B to D
            # Note that crossings are bidirectional edges in graph
            # To match the directions: in input, they are undirected edges,
            # but here direction matters? The input lines X-Y are ordered crossings. So we treat A-B and B-A differently?
            # The problem states that input crossings like X-Y means a crossing of X and Y, but order is important

            # Build direction edges from input crossings as given (X -> Y)
            # Build directed edges dict from input lines
            dir_edges = dict()
            for c in crossings:
                x,y = c.split('-')
                if x not in dir_edges:
                    dir_edges[x]=set()
                dir_edges[x].add(y)

            # check condition (2):
            # no D with D-A and B-D edges (direction matters)
            # so exist D with edge D->A and edge B->D
            for D in streets:
                if D in dir_edges and A in dir_edges[D]:
                    if B in dir_edges and D in dir_edges[B]:
                        return False
            # condition (3):
            # no E such that A-E and E-B edges exist
            for E in streets:
                if A in dir_edges and E in dir_edges[A]:
                    if E in dir_edges and B in dir_edges[E]:
                        return False
            return True

        # build equal strength sets
        # For all pairs in ns_streets and in ew_streets, check equal strength
        # store relations in union-find structure for equal strength

        parent = dict()
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            a=find(a)
            b=find(b)
            if a!=b:
                parent[b]=a

        for st in streets:
            parent[st] = st
        for group in same_dir:
            group_list = list(group)
            for i in range(len(group_list)):
                for j in range(i+1,len(group_list)):
                    A = group_list[i]
                    B = group_list[j]
                    if check_equal(A,B):
                        union(A,B)

        # Build stronger relation graph:
        # A is stronger than B if there is sequence A = A1, A2, ..., An = B with n>=2
        # and for any i in 1 .. n-1 either Ai-Ai+1 is in input crossings or Ai and Ai+1 have equal strength
        # define a graph with nodes as street equivalence classes (equal strength classes)
        # to do so, map each street to its parent (equal strength class),
        # then add edges between classes if there is an input crossing or equal strength connection between their members

        # first create classes mapping
        classes = dict()
        for st in streets:
            p = find(st)
            if p not in classes:
                classes[p] = set()
            classes[p].add(st)

        # build a graph between classes for stronger relation edges
        class_graph = dict()
        class_list = list(classes.keys())
        for c in class_list:
            class_graph[c] = set()

        # helper to get class of a street
        def cclass(s):
            return find(s)

        # input crossing edges (directed as per input)
        dir_edges = dict()
        for c in crossings:
            x,y = c.split('-')
            if x not in dir_edges:
                dir_edges[x] = set()
            dir_edges[x].add(y)

        # Add edges between classes based on input crossing edges
        for x in dir_edges:
            for y in dir_edges[x]:
                cx = cclass(x)
                cy = cclass(y)
                if cx != cy:
                    class_graph[cx].add(cy)

        # Add equal strength edges are handled by classes merging, no edges needed within same class

        # Now, to check if X is stronger than Y, check if class of X can reach class of Y by walking edges or inside equal strength class (already united)

        # For each question:
        # print YES if X and Y are orthogonal (one NS, one EW) and X class can reach Y class by path
        # else NO

        print(len(streets))
        for q in questions:
            X,Y = q.split('-')
            if X not in color or Y not in color:
                print("NO")
                continue
            # must be orthogonal
            if color[X] == color[Y]:
                print("NO")
                continue
            # check reachability from cclass(X) to cclass(Y)
            start = cclass(X)
            goal = cclass(Y)
            visited = set()
            stack = [start]
            found = False
            while stack:
                curr = stack.pop()
                if curr == goal:
                    found = True
                    break
                if curr in visited:
                    continue
                visited.add(curr)
                for nex in class_graph[curr]:
                    if nex not in visited:
                        stack.append(nex)
            print("YES" if found else "NO")

if __name__ == "__main__":
    main()