import sys
ipts = sys.stdin.readlines()
keys = ipts[0][1:-1].split('.')

node = root = {}
for cur in xrange(1, len(ipts)):
    line = ipts[cur]
    indent = 0
    while line[indent] == ' ':
        indent += 1
    m = line[indent:]
    key, value = m.split(':')
    if ":i" not in node:
        node[":i"] = indent
    while indent < node[":i"]:
        node = node[":p"]
    if value == '\n':
        parent = node
        node[key] = node = {}
        node[":p"] = parent
    else:
        node[key] = value[1:-1]
    prev = indent
node = root
for key in keys:
    if type(node) == dict and key in node:
        node = node[key]
    else:
        print "no such property"
        break
else:
    if type(node) == dict:
        print "object"
    else:
        print "string \"%s\"" % node