graph = []

def init():
    global graph
    graph = [[False] * 26 + [True] for _ in xrange(27)]
    graph[26][26] = False

def atoi(c):#index
    if c == "#":
        return 26
    return ord(c) - ord("a")

def make_graph(L):
    global graph
    cur = 0
    L = [L[0]] + [L[i] for i in xrange(1, len(L)) if L[i] != L[i-1]]
    tmp = []
    for s1, s2 in zip(L, L[1:]):
        if s1[0] == s2[0]:
            tmp += [s1[1:], s2[1:]]
        else:
            if not tmp == []:
                make_graph(tmp)
            tmp = []
            graph[atoi(s2[0])][atoi(s1[0])] = True
    if not tmp == []:
        make_graph(tmp)

def check(start):
    stack = set([start])
    visited = [False] * 27
    while len(stack) != 0:
        cur = stack.pop()
        visited[cur] = True
        if graph[cur][start]:
            return False
        for i in xrange(27):
            if graph[cur][i] and not visited[i]:
                stack.add(i)
    return True

while True:
    n = input()
    if n == 0:
        break
    L = [raw_input() + "#" for _ in xrange(n)]
    init()
    make_graph(L)
    for i in xrange(27):
        if not check(i):
            print "no"
            break
    else:
        print "yes"