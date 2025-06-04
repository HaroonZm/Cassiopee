def parse_sequence(s, i=0):
    ops = []
    while i < len(s):
        if s[i] == '(':
            sub_ops, i = parse_sequence(s, i+1)
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            ops.append(('repeat', sub_ops, num))
        elif s[i] == ')':
            return ops, i+1
        else:
            op = s[i]
            i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            ops.append((op, num))
    return ops, i

def apply_operations(matrix, ops, N):
    for op in ops:
        if op[0] == 'repeat':
            sub_ops = op[1]
            times = op[2]
            for _ in range(times):
                apply_operations(matrix, sub_ops, N)
        else:
            shift = op[0]
            idx = op[1] - 1
            if shift == 'L':
                row = matrix[idx]
                first = row[0]
                for j in range(N-1):
                    row[j] = row[j+1]
                row[-1] = first
            elif shift == 'R':
                row = matrix[idx]
                last = row[-1]
                for j in range(N-1, 0, -1):
                    row[j] = row[j-1]
                row[0] = last
            elif shift == 'U':
                first = matrix[0][idx]
                for i in range(N-1):
                    matrix[i][idx] = matrix[i+1][idx]
                matrix[-1][idx] = first
            elif shift == 'D':
                last = matrix[-1][idx]
                for i in range(N-1, 0, -1):
                    matrix[i][idx] = matrix[i-1][idx]
                matrix[0][idx] = last

N, L = map(int, input().split())
S = input().strip()

matrix = [[(i)*N + j + 1 for j in range(N)] for i in range(N)]

operations, _ = parse_sequence(S)

apply_operations(matrix, operations, N)

for row in matrix:
    print(' '.join(map(str, row)))