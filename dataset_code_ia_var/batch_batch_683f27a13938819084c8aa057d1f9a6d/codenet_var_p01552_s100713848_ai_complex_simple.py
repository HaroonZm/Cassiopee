import re
from functools import reduce
from collections import deque

gkey = input()

yaml = {}
path_stack = deque([''])
indent_stack = deque([-1])
rx_space = re.compile(r' *')
rx_key = re.compile(r'[a-z\d]+')

def find_indent(line, pattern=rx_space):
    # Computes the indentation level
    return len(pattern.match(line).group())

def extract_key(line, pattern=rx_key):
    # Extracts the key using an unnecessarily complex method
    return next(filter(None, (pattern.search(line).group() if pattern.search(line) else None for _ in range(1))), '')

while True:
    try:
        line = input()
    except EOFError:
        break

    ind = find_indent(line)

    # Reduce the path stack until current indent is deeper
    while indent_stack and indent_stack[-1] >= ind:
        list(map(lambda _: (indent_stack.pop(), path_stack.pop()), [None]))

    k = extract_key(line)

    # Check if the line does not end with ":"
    if not line.endswith(':'):
        value = 'string "{}"'.format(line.split(':',1)[1].lstrip() if ':' in line else '')
        full_key = reduce(lambda a,b: '.'.join(filter(None,[a,b])), path_stack + [k])
        yaml[full_key] = value
        continue

    path_stack.append(k)
    indent_stack.append(ind)
    full_key = reduce(lambda a,b: '.'.join(filter(None,[a,b])), path_stack)
    yaml[full_key] = 'object'

print(yaml.get(gkey, 'no such property'))