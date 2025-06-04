import sys

for input_line in sys.stdin:
    parts = input_line.split()
    ints = []
    for char in parts:
        ints.append(int(char))
    ints.sort(reverse=True)
    strs = []
    for num in ints:
        strs.append(str(num))
    out = ''
    for i in range(len(strs)):
        out += strs[i]
        if i != len(strs) - 1:
            out += ' '
    print out