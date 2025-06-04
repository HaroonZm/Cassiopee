def get_inputs():
    return map(int, input().split())

def init_array(n):
    return [0] * n

def outer_loop_range(n):
    return range(n)

def inner_loop_range(i, n):
    return range(i + 1, n)

def compute_distance(i, j, x, y):
    return min(j - i, abs(i - x + 1) + abs(j - y + 1) + 1)

def increment_count(arr, idx):
    arr[idx] += 1

def process_pairs(n, x, y, arr):
    for i in outer_loop_range(n):
        for j in inner_loop_range(i, n):
            d = compute_distance(i, j, x, y)
            increment_count(arr, d)

def output_result(arr):
    for b in arr[1:]:
        print(b)

def main():
    n, x, y = get_inputs()
    a = init_array(n)
    process_pairs(n, x, y, a)
    output_result(a)

main()