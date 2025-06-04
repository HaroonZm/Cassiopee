class TreeNode:
    def __init__(self, val, parent=-1):
        self.val = val
        self.children = []
        self.parent_val = parent
        self.depth = None

    def node_type(self):
        if self.depth == 0:
            return "root"
        elif len(self.children) > 0:
            return "internal node"
        else:
            return "leaf"

    def children_values(self):
        vals = []
        for child in self.children:
            vals.append(child.val)
        return vals

    def __str__(self):
        s = "node " + str(self.val)
        s += ": parent = " + str(self.parent_val)
        s += ", depth = " + str(self.depth)
        s += ", " + self.node_type()
        s += ", " + str(self.children_values())
        return s

def calc_depths(node, level):
    if node is None:
        return
    node.depth = level
    for ch in node.children:
        calc_depths(ch, level+1)

num = int(input())
nodes = {}

for i in range(num):
    parts = input().split()
    val = int(parts[0])
    cnt = int(parts[1])
    children = []
    if cnt > 0:
        for j in range(2, 2+cnt):
            children.append(int(parts[j]))
    if val not in nodes:
        nodes[val] = TreeNode(val)
    n = nodes[val]
    for c in children:
        if c not in nodes:
            nodes[c] = TreeNode(c, val)
        n.children.append(nodes[c])
        nodes[c].parent_val = val

root = None
for node in nodes.values():
    if node.parent_val == -1:
        root = node
        break

calc_depths(root, 0)
items = list(nodes.items())
items.sort(key=lambda x: x[0])
for k, node in items:
    print(node)