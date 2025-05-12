N = int(input())
tree = [{'parent': -1, 'left': -1, 'right': -1, 'sibling': -1} for _ in range(N)]
parent = set(n for n in range(N))

for _ in range(N):
    inp = [int(n) for n in input().split()]
    tree[inp[0]]['left'] = inp[1]
    tree[inp[0]]['right'] = inp[2]

    if inp[1] != -1:
        tree[inp[1]]['parent'] = inp[0]
        tree[inp[1]]['sibling'] = inp[2]
    if inp[2] != -1:
        tree[inp[2]]['parent'] = inp[0]
        tree[inp[2]]['sibling'] = inp[1]
    parent = parent.difference(inp[1:])

root = parent.pop()

def preParse(u):
    if u == -1:
        return 
    print(f' {u}', end = '')
    preParse(tree[u]['left'])
    preParse(tree[u]['right'])

def inParse(u):
    if u == -1:
        return 
    inParse(tree[u]['left'])
    print(f' {u}', end = '')
    inParse(tree[u]['right'])

def postParse(u):
    if u == -1:
        return 
    postParse(tree[u]['left'])
    postParse(tree[u]['right'])
    print(f' {u}', end = '')

print('Preorder')
preParse(root)
print()

print('Inorder')
inParse(root)
print()

print('Postorder')
postParse(root)
print()