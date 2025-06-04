import sys

ipts = sys.stdin.readlines()
keys = ipts[0][1:-1].split('.')

root = {}
node = root
indent_stack = []
node_stack = []
indent = 0
prev_indent = 0

cur = 1
while cur < len(ipts):
    line = ipts[cur]
    indent = 0
    while indent < len(line) and line[indent] == ' ':
        indent += 1
    m = line[indent:]
    key, value = m.split(':')
    if len(indent_stack) == 0:
        indent_stack.append(indent)
        node_stack.append(node)
    else:
        while len(indent_stack) > 0 and indent < indent_stack[-1]:
            indent_stack.pop()
            node_stack.pop()
        if len(indent_stack) == 0 or indent != indent_stack[-1]:
            indent_stack.append(indent)
            node_stack.append(node)
    if value == '\n':
        node[key] = {}
        node = node[key]
    else:
        node[key] = value[1:-1]
    if value == '\n':
        node_stack.append(node)
        indent_stack.append(indent + 1)
    else:
        node = node_stack[-1] if node_stack else root
    cur += 1

node = root
idx = 0
bad = False
while idx < len(keys):
    key = keys[idx]
    if type(node) == dict and key in node:
        node = node[key]
        idx += 1
    else:
        print "no such property"
        bad = True
        break
if not bad:
    if type(node) == dict:
        print "object"
    else:
        print "string \"%s\"" % node