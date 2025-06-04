import sys

input_stream = sys.stdin

def count_patterns(line):
    joi = 0
    ioi = 0
    idx = 0
    while idx <= len(line)-3:
        substr = ''.join([line[j] for j in range(idx, idx+3)])
        if substr == "JOI":
            joi += 1
        elif substr == "IOI":
            ioi = ioi + 1
        idx += 1
    return (joi, ioi)

go = True
while go:
    current = input_stream.readline()
    if current.endswith('\n'):
        current = current[:-1]
    if len(current) == 0:
        break

    res = count_patterns(current)
    for c in res:
        sys.stdout.write(str(c)+'\n')