shapes = {
    'A': ["00001111",
          "00000000",
          "00000000",
          "00000000",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'B': ["00000001",
          "00000001",
          "00000001",
          "00000001",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'C': ["00000000",
          "00000000",
          "00011000",
          "00011000",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'D': ["00000000",
          "00000000",
          "01100000",
          "00110000",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'E': ["00000000",
          "00000000",
          "00110000",
          "00110000",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'F': ["00000000",
          "00000000",
          "00111100",
          "00000000",
          "00000000",
          "00000000",
          "00000000",
          "00000000"],
    'G': ["00000000",
          "00000000",
          "00000011",
          "00000011",
          "00000000",
          "00000000",
          "00000000",
          "00000000"]
}

def normalize(shape):
    # shape is list of 8 strings of '0' and '1'
    # shift shape to top-left so no leading zeros in rows and in columns
    rows = [list(row) for row in shape]
    # find min row index that has 1
    min_r = 8
    min_c = 8
    for r in range(8):
        for c in range(8):
            if rows[r][c] == '1':
                if r < min_r:
                    min_r = r
                if c < min_c:
                    min_c = c
    if min_r == 8: # no ones found
        return ["00000000"] * 8
    # build new shape
    new_shape = []
    for r in range(min_r, min_r + 8):
        if r >=8:
            new_shape.append("00000000")
        else:
            row = rows[r]
            row_norm = row[min_c:min_c + 8]
            while len(row_norm) < 8:
                row_norm.append('0')
            new_shape.append("".join(row_norm))
    # pad on bottom if less than 8 rows
    while len(new_shape) < 8:
        new_shape.append("00000000")
    # finally truncate to 8 rows
    return new_shape[:8]

def shapes_equal(s1, s2):
    for i in range(8):
        if s1[i] != s2[i]:
            return False
    return True

import sys

lines = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if line == '' and lines:
        # process lines
        shape_input = lines
        shape_norm = normalize(shape_input)
        found = False
        for k, v in shapes.items():
            if normalize(v) == shape_norm:
                print(k)
                found = True
                break
        if not found:
            print("?")
        lines = []
    elif line != '':
        lines.append(line)
# last dataset
if lines:
    shape_input = lines
    shape_norm = normalize(shape_input)
    found = False
    for k, v in shapes.items():
        if normalize(v) == shape_norm:
            print(k)
            found = True
            break
    if not found:
        print("?")