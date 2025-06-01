def read_input():
    return map(int, input().split())

def is_invalid(n, k):
    if n == 0:
        return True
    if n & 1:
        return True
    if k >= (1 << (n >> 1)):
        return True
    return False

def initialize_array(n):
    arr = []
    for _ in range(n):
        arr.append([-1] * n)
    return arr

def set_first_row(arr, n, k):
    n1 = n - 1
    for c in range(n):
        bit_pos = (n1 - c) >> 1
        arr[0][c] = (k >> bit_pos) & 1

def count_same_neighbors(arr, n, r, c, mv):
    t = arr[r][c]
    f = 0
    for i in range(4):
        nr = r + mv[i][0]
        nc = c + mv[i][1]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == t:
            f += 1
    return f

def fill_array(arr, n, mv):
    for r in range(n - 1):
        for c in range(n):
            f = count_same_neighbors(arr, n, r, c, mv)
            t = arr[r][c]
            if f == 2:
                arr[r + 1][c] = 1 - t
            else:
                arr[r + 1][c] = t

def convert_cell(value, d2c):
    return d2c[value]

def print_array(arr, n, d2c):
    for r in range(n):
        line = ''.join(convert_cell(arr[r][c], d2c) for c in range(n))
        print(line)

def main():
    mv = ((-1,0), (0,1), (1,0), (0,-1))
    d2c = {0:'.', 1:'E'}
    while True:
        n, k = read_input()
        if n == 0:
            break
        k, n1 = k - 1, n - 1
        if is_invalid(n, k):
            print("No\n")
            continue
        arr = initialize_array(n)
        set_first_row(arr, n, k)
        fill_array(arr, n, mv)
        print_array(arr, n, d2c)
        print()

main()