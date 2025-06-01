def read_dimensions():
    return map(int, input().split())

def read_matrix(h):
    matrix = []
    for _ in range(h):
        row = read_row()
        matrix.append(row)
    return matrix

def read_row():
    return list(map(int, input().split()))

def init_answer():
    return 10**9

def calculate_minimum_distance(i, j, h, w, a):
    cnt = 0
    for m in range(h):
        for n in range(w):
            cnt += calculate_contribution(i, j, m, n, a[m][n])
    return cnt

def calculate_contribution(i, j, m, n, x):
    return min(abs(i - m), abs(j - n)) * x

def find_min_answer(h, w, a):
    ans = init_answer()
    for i in range(h):
        for j in range(w):
            cnt = calculate_minimum_distance(i, j, h, w, a)
            ans = min(ans, cnt)
    return ans

def main():
    h, w = read_dimensions()
    a = read_matrix(h)
    ans = find_min_answer(h, w, a)
    print(ans)

main()