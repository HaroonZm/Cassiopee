N = int(input())
tree = []
i = 0
while i < N:
    tree.append({'parent': -1, 'left': -1, 'right': -1, 'sibling': -1})
    i += 1

parent = set()
i = 0
while i < N:
    parent.add(i)
    i += 1

i = 0
while i < N:
    inp = input().split()
    inp0 = int(inp[0])
    inp1 = int(inp[1])
    inp2 = int(inp[2])
    tree[inp0]['left'] = inp1
    tree[inp0]['right'] = inp2
    if inp1 != -1:
        tree[inp1]['parent'] = inp0
        tree[inp1]['sibling'] = inp2
    if inp2 != -1:
        tree[inp2]['parent'] = inp0
        tree[inp2]['sibling'] = inp1
    if inp1 in parent:
        parent.remove(inp1)
    if inp2 in parent:
        parent.remove(inp2)
    i += 1

root = None
for v in parent:
    root = v
    break

print('Preorder')
stack = []
u = root
stack.append(u)
while stack:
    u = stack.pop()
    if u == -1:
        continue
    print(' ' + str(u), end='')
    # Push right then left so left is processed first
    stack.append(tree[u]['right'])
    stack.append(tree[u]['left'])
print()

print('Inorder')
stack = []
u = root
current = u
while stack or current != -1:
    while current != -1:
        stack.append(current)
        current = tree[current]['left']
    current = stack.pop()
    print(' ' + str(current), end='')
    current = tree[current]['right']
print()

print('Postorder')
stack1 = []
stack2 = []
stack1.append(root)
while stack1:
    node = stack1.pop()
    if node == -1:
        continue
    stack2.append(node)
    stack1.append(tree[node]['left'])
    stack1.append(tree[node]['right'])
while stack2:
    print(' ' + str(stack2.pop()), end='')
print()