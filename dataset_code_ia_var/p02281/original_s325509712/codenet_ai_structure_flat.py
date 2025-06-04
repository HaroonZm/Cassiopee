n = int(input())
tree = [None] * n
root_set = set(range(n))
for i in range(n):
    node_id, left, right = map(int, input().split())
    tree[node_id] = [node_id, left, right]
    if left != -1:
        root_set.discard(left)
    if right != -1:
        root_set.discard(right)
root = root_set.pop()

print("Preorder")
stack = []
cur = root
visited = set()
while stack or cur != -1:
    if cur != -1:
        print("", cur, end="")
        stack.append(cur)
        cur = tree[cur][1]
    else:
        cur = stack.pop()
        cur = tree[cur][2]
print("")

print("Inorder")
stack = []
cur = root
while stack or cur != -1:
    if cur != -1:
        stack.append(cur)
        cur = tree[cur][1]
    else:
        cur = stack.pop()
        print("", cur, end="")
        cur = tree[cur][2]
print("")

print("Postorder")
stack = []
result = []
cur = root
last_visited = None
while stack or cur != -1:
    if cur != -1:
        stack.append(cur)
        cur = tree[cur][1]
    else:
        peek = stack[-1]
        right = tree[peek][2]
        if right != -1 and last_visited != right:
            cur = right
        else:
            print("", peek, end="")
            last_visited = stack.pop()
            cur = -1
print("")