def can_arrange_dominoes(dominoes):
    from collections import defaultdict, deque
    
    # Build graph: nodes are numbers 0-6, edges are dominoes (can be multiple edges)
    graph = defaultdict(list)
    degree = defaultdict(int)
    
    # Count edges and degrees
    for d in dominoes:
        a, b = d
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # For arrangement in one line, path must be Eulerian trail or circuit:
    # Conditions:
    #   - Graph has at most two nodes with odd degree.
    #   - All nodes with edges belong to a single connected component.
    nodes_with_edges = [node for node in degree if degree[node] > 0]
    if not nodes_with_edges:
        return True  # no dominoes
    
    # Check connectivity (on nodes that have edges)
    visited = set()
    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
    bfs(nodes_with_edges[0])
    if any(node not in visited for node in nodes_with_edges):
        return False
    
    odd_degree_nodes = [node for node in degree if degree[node] % 2 == 1]
    if len(odd_degree_nodes) == 0 or len(odd_degree_nodes) == 2:
        return True
    return False

def parse_domino(s):
    # s is two digits string like "13" -> (1,3)
    return (int(s[0]), int(s[1]))

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    # Process every pair of lines
    for i in range(0, len(lines), 2):
        n = int(lines[i])
        domino_strs = lines[i+1].split()
        dominoes = [parse_domino(d) for d in domino_strs]
        print("Yes" if can_arrange_dominoes(dominoes) else "No")

if __name__ == "__main__":
    main()