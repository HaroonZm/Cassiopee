def read_int():
    return int(raw_input())

def read_line():
    return raw_input().strip()

def parse_input_line():
    line=read_line()
    return map(int,line.split(','))

def create_graph(n):
    return [[1<<30]*n for _ in xrange(n)]

def initialize_graph(graph,n):
    edges_count=read_int()
    for _ in xrange(edges_count):
        a,b,c=parse_input_line()
        set_edge(graph,a,b,c)

def set_edge(graph,a,b,c):
    graph[a][b]=c
    graph[b][a]=c

def create_visited(n):
    return [False]*n

def mark_visited(visited, index):
    visited[index]=True

def all_visited(visited):
    return all(visited)

def find_min_edge(graph, visited, n):
    candidates = []
    for j in xrange(n):
        if not visited[j]:
            for i in xrange(n):
                if visited[i]:
                    candidates.append((i,j,graph[i][j]))
    return min(candidates, key=lambda x:x[2])

def process_one_graph(n):
    graph=create_graph(n)
    initialize_graph(graph,n)
    visited=create_visited(n)
    mark_visited(visited,0)
    ans=0
    while not all_visited(visited):
        t=find_min_edge(graph,visited,n)
        ans+=t[2]/100-1
        mark_visited(visited,t[1])
    print ans

def main_loop():
    while True:
        n=read_int()
        if n==0:
            break
        process_one_graph(n)

main_loop()