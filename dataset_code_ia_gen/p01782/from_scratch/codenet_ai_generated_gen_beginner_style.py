N = int(input())
matrix = [list(input()) for _ in range(N)]

used_columns = [False] * N
result = []

def backtrack(row):
    if row == N:
        return True
    # Try columns in order to get lex smallest char
    candidates = []
    for col in range(N):
        if not used_columns[col]:
            candidates.append((matrix[row][col], col))
    candidates.sort(key=lambda x: ord(x[0]))
    for ch, col in candidates:
        used_columns[col] = True
        result.append(ch)
        if backtrack(row + 1):
            return True
        result.pop()
        used_columns[col] = False
    return False

backtrack(0)
print("".join(result))