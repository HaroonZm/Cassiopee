def main():
    while True:
        line = raw_input().split()
        while line == []:
            line = raw_input().split()
        if line[0] == "0":
            break
        N = int(line[0])
        s = line[1:]
        while len(s) < N:
            s += raw_input().split()
        original = make_graph(s)
        line = raw_input().split()
        while line == []:
            line = raw_input().split()
        M = int(line[0])
        t = line[1:]
        while len(t) < M:
            t += raw_input().split()
        for k in rotate_all_iter(make_graph(t)):
            if check(original, k):
                print "SAME"
                break
        else:
            print "DIFFERENT"

def check(key1, key2):
    def dfs(n1, n2):
        f1 = n1 in used1
        f2 = n2 in used2
        if f1 != f2:
            return False
        if f1 == f2 == True:
            return True
        used1[n1] = used2[n2] = True
        for k in n1.edges.keys():
            if n1.edges[k] is None:
                if n2.edges[k] is not None:
                    return False
            elif n2.edges[k] is None:
                return False
            elif not dfs(n1.edges[k], n2.edges[k]):
                return False
        return True
    for n in key2:
        used1 = {}
        used2 = {}
        if dfs(key1[0], n):
            return True
    return False

def make_graph(seq):
    D = {
        "+x": (1, 0, 0), "-x": (-1, 0, 0),
        "+y": (0, 1, 0), "-y": (0, -1, 0),
        "+z": (0, 0, 1), "-z": (0, 0, -1),
    }
    R = {
        "+x": "-x", "-x": "+x",
        "+y": "-y", "-y": "+y",
        "+z": "-z", "-z": "+z",
    }
    labels = {}
    pre = Node([0, 0, 0])
    nodes = {pre: pre}
    for s in seq:
        if s.isdigit():
            if s in labels:
                pre = labels[s]
            else:
                labels[s] = pre
        else:
            n = Node([pre[i] + D[s][i] for i in xrange(3)])
            if n in nodes:
                n = nodes[n]
            else:
                nodes[n] = n
            pre.add_edge(s, n)
            n.add_edge(R[s], pre)
            pre = n
    return nodes.values()

def rotate_all_iter(nodes):
    schedule = (
        Node.roll_x, Node.roll_x, Node.roll_x, Node.roll_x,
        Node.roll_y, Node.roll_z, Node.roll_z, Node.roll_z, Node.roll_z,
        Node.roll_y, Node.roll_x, Node.roll_x, Node.roll_x, Node.roll_x,
        Node.roll_y, Node.roll_z, Node.roll_z, Node.roll_z, Node.roll_z,
        Node.roll_x, Node.roll_y, Node.roll_y, Node.roll_y, Node.roll_y,
        Node.roll_x, Node.roll_z, Node.roll_z, Node.roll_z, Node.roll_z,
        Node.roll_x, Node.roll_y, Node.roll_y, Node.roll_y, Node.roll_y,
    )
    for f in schedule:
        f(nodes[0], {})
        yield nodes

class Node(tuple):
    def __init__(self, li):
        if len(li) != 3:
            raise ValueError
        tuple.__init__(self, li)
        self.edges = dict((k, None) for k in ["+x", "-x", "+y", "-y", "+z", "-z"])

    def add_edge(self, edge, node):
        if edge not in self.edges:
            raise ValueError
        self.edges[edge] = node

    @classmethod
    def roll_x(cls, node, memo={}):
        if node in memo:
            return []
        memo[tuple(node)] = node
        node.edges["+y"], node.edges["+z"], node.edges["-y"], node.edges["-z"] = \
            node.edges["-z"], node.edges["+y"], node.edges["+z"], node.edges["-y"]
        for n in node.edges.values():
            if n is not None:
                cls.roll_x(n, memo)

    @classmethod
    def roll_y(cls, node, memo={}):
        if node in memo:
            return []
        memo[tuple(node)] = node
        node.edges["+x"], node.edges["+z"], node.edges["-x"], node.edges["-z"] = \
            node.edges["-z"], node.edges["+x"], node.edges["+z"], node.edges["-x"]
        for n in node.edges.values():
            if n is not None:
                cls.roll_y(n, memo)

    @classmethod
    def roll_z(cls, node, memo={}):
        if node in memo:
            return []
        memo[tuple(node)] = node
        node.edges["+x"], node.edges["+y"], node.edges["-x"], node.edges["-y"] = \
            node.edges["-y"], node.edges["+x"], node.edges["+y"], node.edges["-x"]
        for n in node.edges.values():
            if n is not None:
                cls.roll_z(n, memo)

    @classmethod
    def traverse(cls, node, memo={}):
        if node in memo:
            return []
        memo[tuple(node)] = node
        ret = [node]
        for n in node.edges.values():
            if n is not None:
                ret += cls.traverse(n, memo + [node])
        return ret

if __name__ == "__main__":
    main()