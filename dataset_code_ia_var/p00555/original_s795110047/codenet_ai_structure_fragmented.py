def read_input():
    N, M, D = map(int, input().split())
    S = [list(str(input())) for _ in range(N)]
    return N, M, D, S

def get_row(board, row_idx):
    return board[row_idx]

def count_sequences_in_line(line, D):
    count = 0
    num_seq = 0
    for cell in line:
        if cell == ".":
            count += 1
            if count >= D:
                num_seq += 1
        else:
            count = 0
    return num_seq

def get_empty_grid(M, N):
    return [["" for _ in range(N)] for _ in range(M)]

def transpose_board(S, N, M):
    T = get_empty_grid(M, N)
    for i in range(N):
        for j in range(M):
            T[j][i] = S[i][j]
    return T

def count_sequences_in_rows(S, N, M, D):
    total = 0
    for i in range(N):
        yoko = get_row(S, i)
        total += count_sequences_in_line(yoko, D)
    return total

def count_sequences_in_columns(S, N, M, D):
    T = transpose_board(S, N, M)
    total = 0
    for j in range(M):
        tate = get_row(T, j)
        total += count_sequences_in_line(tate, D)
    return total

def print_result(ans):
    print(ans)

def main():
    N, M, D, S = read_input()
    ans = 0
    ans += count_sequences_in_rows(S, N, M, D)
    ans += count_sequences_in_columns(S, N, M, D)
    print_result(ans)

main()