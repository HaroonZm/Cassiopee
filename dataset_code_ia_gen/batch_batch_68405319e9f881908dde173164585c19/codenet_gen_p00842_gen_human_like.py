def main():
    import sys
    sys.setrecursionlimit(10**7)

    def read_matrix(n):
        matrix = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().split()))
            matrix.append(row)
        return matrix

    class TreeBuilder:
        def __init__(self, dist):
            self.n = len(dist)
            self.dist = dist
            self.next_node = self.n
            # adjacency list: key is node index, value is list of neighbors
            self.adj = {i: [] for i in range(self.n)}
        
        def is_leaf(self, node):
            return node < self.n

        def add_edge(self, u, v):
            self.adj[u].append(v)
            self.adj[v].append(u)

        def build(self):
            # We'll build the tree by repeatedly grouping leaves
            # and introducing internal nodes ("switches")
            # The algorithm:
            # While more than one cluster remains:
            #  - Find leaves i,j with minimal distance
            #  - Create a new internal node and connect to the clusters that i and j belong to
            #  - Merge clusters
            # But this is complicated if done naively,
            # so we implement a bottom-up progressive reconstruction:
            # Represent each leaf initially as a node and cluster.
            # At each step, find the pair with minimum distance,
            # connect them to a new switch node and update distances accordingly.
            
            # We manage clusters, each cluster is a set of nodes known to be connected
            # Here, since the problem is classical of additive tree reconstruction,
            # we can apply the classic additive phylogeny approach tailored for this case.

            # We implement the "Additive Tree" construction as per the problem's logic.

            # Initialize leaves as clusters
            clusters = [{i} for i in range(self.n)]
            # Initialize distance matrix between clusters; same as self.dist initially
            d = [row[:] for row in self.dist]  # copy

            # We track the nodes representing clusters:
            # initially leaves are nodes 0..n-1
            cluster_nodes = [i for i in range(self.n)]

            while len(clusters) > 1:
                # find pair of distinct clusters with minimal distance
                min_val = 10**9
                min_i = -1
                min_j = -1
                for x in range(len(clusters)):
                    for y in range(x+1, len(clusters)):
                        if d[x][y] < min_val:
                            min_val = d[x][y]
                            min_i = x
                            min_j = y

                # create new internal node representing new switch
                new_node = self.next_node
                self.next_node += 1

                ci = clusters[min_i]
                cj = clusters[min_j]
                ni = cluster_nodes[min_i]
                nj = cluster_nodes[min_j]

                # Connect new internal node to nodes representing clusters
                self.add_edge(new_node, ni)
                self.add_edge(new_node, nj)

                # merge two clusters
                new_cluster = ci.union(cj)

                # Build new distance row for merged cluster: distance between merged cluster and others:
                new_row = []
                for k in range(len(clusters)):
                    if k == min_i or k == min_j:
                        continue
                    dist_to_k = (d[min_i][k] + d[min_j][k] - d[min_i][min_j]) // 2
                    new_row.append(dist_to_k)

                # update clusters and d
                new_clusters = []
                new_cluster_nodes = []
                new_d = []

                for k in range(len(clusters)):
                    if k != min_i and k != min_j:
                        new_clusters.append(clusters[k])
                        new_cluster_nodes.append(cluster_nodes[k])

                new_clusters.append(new_cluster)
                new_cluster_nodes.append(new_node)

                # build new distance matrix
                size = len(new_clusters)
                for i in range(size-1):
                    row = [0]*size
                    for j in range(i+1,size-1):
                        row[j] = d[i if i<min_i else i+1 if i<min_j else i+2][j if j<min_i else j+1 if j<min_j else j+2]
                        row[j], row[i] = row[i], row[j] # symmetry swapped to row i j
                    row[size-1] = new_row[i]
                    new_d.append(row)
                # last row:
                last_row = new_row[:] + [0]
                new_d.append(last_row)

                # fix symmetry:
                for i in range(size):
                    for j in range(i+1,size):
                        new_d[j][i] = new_d[i][j]

                clusters = new_clusters
                cluster_nodes = new_cluster_nodes
                d = new_d

            # Finished building tree

        def get_internal_degrees(self):
            # Internal nodes are those with index >= n
            degrees = []
            for node in self.adj:
                if node >= self.n:
                    degrees.append(len(self.adj[node]))
            degrees.sort()
            return degrees

    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    while True:
        if pos >= len(input_lines):
            break
        line = input_lines[pos].strip()
        pos += 1
        if line == '0':
            break
        n = int(line)
        dist = []
        while len(dist) < n:
            row_vals = list(map(int, input_lines[pos].strip().split()))
            pos += 1
            dist.append(row_vals)
        tb = TreeBuilder(dist)
        tb.build()
        result = tb.get_internal_degrees()
        print(' '.join(map(str,result)))

if __name__ == "__main__":
    main()