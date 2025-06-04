height_main, width_main = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(height_main)]
matrix_b = [list(map(int, input().split())) for _ in range(height_main)]
height_sub, width_sub = map(int, input().split())
matrix_c = [list(map(int, input().split())) for _ in range(height_sub)]
neg_inf = 10 ** 20 * -1

def compute_matching_sum(start_x, start_y):
    total_sum = 0
    for offset_y in range(height_sub):
        for offset_x in range(width_sub):
            if matrix_b[start_y + offset_y][start_x + offset_x] != matrix_c[offset_y][offset_x]:
                return neg_inf
            total_sum += matrix_a[start_y + offset_y][start_x + offset_x]
    return total_sum

max_sum = neg_inf
for origin_y in range(height_main - height_sub + 1):
    for origin_x in range(width_main - width_sub + 1):
        current_sum = compute_matching_sum(origin_x, origin_y)
        if current_sum > max_sum:
            max_sum = current_sum
if max_sum == neg_inf:
    print("NA")
else:
    print(max_sum)