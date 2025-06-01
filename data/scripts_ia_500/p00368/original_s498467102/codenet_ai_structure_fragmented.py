def read_dimensions():
    return [int(i) for i in input().split()]

def read_matrix(height):
    matrix = []
    for _ in range(height):
        matrix.append([i for i in input().split()])
    return matrix

def invert_binary_list(binary_list):
    inverted = []
    for i in binary_list:
        inverted.append(str(int(not int(i))))
    return inverted

def check_up_line_balance(up_line, width):
    zeros_count = up_line.count("0")
    if abs(zeros_count * 2 - width) >= 2:
        return False
    return True

def lines_are_equal(line1, line2):
    if len(line1) != len(line2):
        return False
    for a, b in zip(line1, line2):
        if a != b:
            return False
    return True

def check_lines_consistency(matrix, up_line, not_up_line):
    same_count = 1
    is_ok = True
    for line in matrix[1:]:
        if up_line[0] == line[0]:
            same_count += 1
            if not lines_are_equal(up_line, line):
                is_ok = False
                break
        elif not_up_line[0] == line[0]:
            if not lines_are_equal(not_up_line, line):
                is_ok = False
                break
        else:
            is_ok = False
            break
    return is_ok, same_count

def check_same_line_balance(same_count, height):
    if abs(same_count * 2 - height) >= 2:
        return False
    return True

def main():
    is_ok = True
    W, H = read_dimensions()
    matrix = read_matrix(H)
    up = matrix[0]
    not_up = invert_binary_list(up)
    if not check_up_line_balance(up, W):
        is_ok = False
    is_ok, same = check_lines_consistency(matrix, up, not_up)
    if not check_same_line_balance(same, H):
        is_ok = False
    if is_ok:
        print("yes")
    else:
        print("no")

main()