def read_input():
    return list(map(int, input().split()))

def init_arrays(W, H):
    return [0] * (H + 1), [0] * (W + 1)

def process_single_zone(row, col, W, H):
    x, y, w = read_input()
    update_row(row, H, y, w)
    update_col(col, W, x, w)

def update_row(row, H, y, w):
    begin = max(0, y - w)
    end = min(H, y + w)
    row[begin] += 1
    row[end] -= 1

def update_col(col, W, x, w):
    begin = max(0, x - w)
    end = min(W, x + w)
    col[begin] += 1
    col[end] -= 1

def cumulate_array(arr, size):
    for i in range(size):
        arr[i + 1] += arr[i]

def check_positive_coverage(arr, size):
    for i in range(size):
        if arr[i] <= 0:
            return False
    return True

def handle_result(flag1, flag2):
    if flag1 or flag2:
        print("Yes")
    else:
        print("No")

def main():
    N, W, H = read_input()
    row, col = init_arrays(W, H)
    for _ in range(N):
        process_single_zone(row, col, W, H)
    cumulate_array(row, H)
    flag1 = check_positive_coverage(row, H)
    if flag1:
        print("Yes")
        return
    cumulate_array(col, W)
    flag2 = check_positive_coverage(col, W)
    handle_result(flag1, flag2)

main()