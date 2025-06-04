import sys

sys.setrecursionlimit(10**7)

query = sys.stdin.readline().rstrip()
keys = query.strip('.').split('.')

lines = sys.stdin.read().splitlines()

# Parse YAML subset given indentation level
def parse_mapping(lines, start, indent):
    mapping = {}
    i = start
    n = len(lines)
    while i < n:
        line = lines[i]
        # Count leading spaces
        leading = 0
        while leading < len(line) and line[leading] == ' ':
            leading += 1
        # Check indentation
        if leading != indent:
            break
        # Parse key and value
        rest = line[leading:]
        if ':' not in rest:
            break
        key, sep, rest_val = rest.partition(':')
        key = key.strip()
        if rest_val == '':
            # Nested mapping starts next line(s)
            i += 1
            submap, next_i = parse_mapping(lines, i, indent + 1)
            mapping[key] = submap
            i = next_i
        else:
            # value in same line after ": "
            # rest_val starts with a space, so remove it
            val = rest_val[1:] if rest_val.startswith(' ') else rest_val
            mapping[key] = val
            i += 1
    return mapping, i

root, _ = parse_mapping(lines, 0, 0)

cur = root
for k in keys:
    if not isinstance(cur, dict) or k not in cur:
        print("no such property")
        break
    cur = cur[k]
else:
    if isinstance(cur, dict):
        print("object")
    else:
        print('string "' + cur + '"')