N = 1000000007
node_n = int(input())
nodes = []
for _ in range(node_n):
    kind = input()
    nodes.append({'kind': kind, 'children': [], 'n': None, 'index': []})
for _ in range(node_n - 1):
    i, j = map(int, input().split())
    nodes[i-1]['children'].append(nodes[j-1])
    nodes[i-1]['index'].append(j-1)
def product(iterator):
    result = 1
    for element in iterator:
        result = (result * (element % N)) % N
    return result
def number_of_cases(node):
    if node['n'] is not None:
        return node['n']
    cases = [number_of_cases(child) for child in node['children']]
    kind = node['kind']
    if 'E' in kind:
        result = product(cases)
        if '?' in kind:
            result = (result + 1) % N
    elif 'A' in kind:
        result = sum(cases) % N
        if '?' in kind:
            result = (result + 1) % N
    elif 'R' in kind:
        result = product((x+1 for x in cases))
        if '?' not in kind:
            result = (result - 1) % N
    else:
        raise Exception("unreachable.")
    node['n'] = result
    return result
while nodes[1:] != [None]*(len(nodes)-1):
    last_parents = []
    for node in nodes:
        if node is not None and node['children'] and all(child['children'] == [] for child in node['children']):
            last_parents.append(node)
    for parent in last_parents:
        parent['n'] = number_of_cases(parent)
        for idx in parent['index']:
            nodes[idx] = None
        parent['children'] = []
print(nodes[0]['n'] % N)