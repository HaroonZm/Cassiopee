import sys

def rotate(node, direction):
    child = node[direction]
    if direction == 1:
        node[1] = child[0]
        child[0] = node
    else:
        node[0] = child[1]
        child[1] = node
    return child

root = None

def insert(value, priority):
    global root
    path = []
    directions = []
    current = root
    while current:
        path.append(current)
        if current[2] == value:
            return
        direction = 1 if current[2] < value else 0
        directions.append(direction)
        current = current[direction]
    new_node = [None, None, value, priority]
    while path:
        parent = path.pop()
        direction = directions.pop()
        parent[direction] = new_node
        if parent[3] >= new_node[3]:
            break
        new_node = rotate(parent, direction)
    else:
        root = new_node

def remove_node(node):
    stack = []
    directions = []
    while node[0] or node[1]:
        left = node[0]
        right = node[1]
        if left and right:
            direction = 0 if left[3] <= right[3] else 1
        elif left:
            direction = 1
        else:
            direction = 0
        stack.append(rotate(node, direction))
        directions.append(direction ^ 1)
    node = x = None
    while stack:
        node = x
        x = stack.pop()
        direction = directions.pop()
        x[direction] = node
    return x

def delete(value):
    global root
    current = root
    parent = None
    direction = 0
    while current:
        if value == current[2]:
            break
        parent = current
        direction = 1 if current[2] < value else 0
        current = current[direction]
    else:
        return
    if parent:
        parent[direction] = remove_node(current)
    else:
        root = remove_node(current)

def find(value):
    current = root
    while current:
        if value == current[2]:
            return True
        current = current[1] if current[2] < value else current[0]
    return False

def debug():
    preorder = []
    inorder = []
    def traverse(node):
        preorder.append(str(node[2]))
        if node[0]:
            traverse(node[0])
        inorder.append(str(node[2]))
        if node[1]:
            traverse(node[1])
    if root:
        traverse(root)
    return " ".join(inorder), " ".join(preorder)

M = int(sys.stdin.readline())
result = []
for _ in range(M):
    data = sys.stdin.readline().split()
    if data[0] == "print":
        a, b = debug()
        result.append(a)
        result.append(b)
    elif data[0] == "find":
        if find(int(data[1])):
            result.append("yes")
        else:
            result.append("no")
    elif data[0] == "delete":
        delete(int(data[1]))
    else:
        value = int(data[1])
        priority = int(data[2])
        insert(value, priority)
sys.stdout.write("\n".join(result))
sys.stdout.write("\n")