import sys
sys.setrecursionlimit(10**7)

def can_form_shiritori(words):
    from collections import defaultdict, deque

    n = len(words)
    graph = defaultdict(list)
    indegree = [0]*26
    outdegree = [0]*26
    used_vertices = set()

    for w in words:
        f = ord(w[0]) - ord('a')
        l = ord(w[-1]) - ord('a')
        graph[f].append(l)
        outdegree[f] += 1
        indegree[l] += 1
        used_vertices.add(f)
        used_vertices.add(l)

    # Check connectivity of vertices with edges
    def dfs(v, visited, g):
        visited.add(v)
        for u in g[v]:
            if u not in visited:
                dfs(u, visited, g)

    # build undirected graph for connectivity check
    undirected = defaultdict(list)
    for v in used_vertices:
        for u in graph[v]:
            undirected[v].append(u)
            undirected[u].append(v)

    visited = set()
    start_vertex = next(iter(used_vertices))
    dfs(start_vertex, visited, undirected)
    if visited != used_vertices:
        return False

    # Check Eulerian path conditions
    start_points = 0
    end_points = 0
    for i in used_vertices:
        diff = outdegree[i] - indegree[i]
        if diff == 1:
            start_points += 1
        elif diff == -1:
            end_points += 1
        elif diff != 0:
            return False

    if (start_points == 0 and end_points == 0) or (start_points == 1 and end_points == 1):
        # Additionally, check the first letter of first word matches last letter of last word in path
        # Since a Eulerian path uses all edges, it corresponds to using all words
        # But Eulerian path doesn't ensure the first word's first char == last word's last char, 
        # So we must check that condition explicitly possible by choosing start and end arcs carefully.
        # The problem states: first word's first char == last word's last char.
        # So the Eulerian path must be a circuit (start_points == 0 and end_points == 0) to be "OK".
        # If start_points == 1 and end_points ==1, it means the path is not circular => NG.
        return start_points == 0 and end_points == 0
    else:
        return False

def main():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        words = [input().strip() for _ in range(n)]
        if can_form_shiritori(words):
            print("OK")
        else:
            print("NG")

if __name__ == "__main__":
    main()