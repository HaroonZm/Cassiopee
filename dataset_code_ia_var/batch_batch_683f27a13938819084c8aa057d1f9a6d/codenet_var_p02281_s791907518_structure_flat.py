import sys

# Lire l'entrée
_input = sys.stdin.readlines()
array_length = int(_input[0])
array = list(map(lambda x: x.split(), _input[1:]))

node_list = []
for i in range(array_length):
    node = {}
    node['parent'] = -1
    node['children'] = []
    node['index'] = -1
    node_list.append(node)

# Remplir les informations des noeuds et définir les parents
for each in array:
    idx, left, right = [int(x) for x in each]
    node_list[idx]['index'] = idx
    node_list[idx]['children'] = [left, right]
    if left != -1:
        node_list[left]['parent'] = idx
    if right != -1:
        node_list[right]['parent'] = idx

# Trouver la racine
for x in node_list:
    if x['parent'] == -1:
        root = x
        break

# Preorder
print('Preorder')
stack = []
stack.append(root)
first = True
while stack:
    v = stack.pop()
    if first:
        print(' ' + str(v['index']), end='')
        first = False
    else:
        print(' ' + str(v['index']), end='')
    right = v['children'][1]
    left = v['children'][0]
    if right != -1:
        stack.append(node_list[right])
    if left != -1:
        stack.append(node_list[left])
print()

# Inorder
print('Inorder')
curr = root
stack = []
first = True
while curr is not None or stack:
    while curr is not None:
        stack.append(curr)
        left = curr['children'][0]
        if left != -1:
            curr = node_list[left]
        else:
            curr = None
    curr = stack.pop()
    if first:
        print(' ' + str(curr['index']), end='')
        first = False
    else:
        print(' ' + str(curr['index']), end='')
    right = curr['children'][1]
    if right != -1:
        curr = node_list[right]
    else:
        curr = None
print()

# Postorder
print('Postorder')
stack = []
output = []
stack.append(root)
while stack:
    v = stack.pop()
    output.append(v['index'])
    left = v['children'][0]
    right = v['children'][1]
    if left != -1:
        stack.append(node_list[left])
    if right != -1:
        stack.append(node_list[right])
output = output[::-1]
first = True
for idx in output:
    if first:
        print(' ' + str(idx), end='')
        first = False
    else:
        print(' ' + str(idx), end='')
print()