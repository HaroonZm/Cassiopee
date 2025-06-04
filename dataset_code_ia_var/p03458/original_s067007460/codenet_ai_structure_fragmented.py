def parse_input():
    return map(int, input().split())

def initialize_square(k):
    size = k * 2
    return [[0 for _ in range(size)] for _ in range(size)]

def adjust_y_for_W(y, k, c):
    if c == 'W':
        return y + k
    return y

def mod_coordinate(val, k):
    return val % (k * 2)

def increment_square(square, x, y):
    square[x][y] += 1

def process_entries(n, k, square):
    for _ in range(n):
        x, y, c = input().split()
        x = int(x)
        y = int(y)
        y = adjust_y_for_W(y, k, c)
        x = mod_coordinate(x, k)
        y = mod_coordinate(y, k)
        increment_square(square, x, y)

def get_square_cumulative_sum(square):
    return CumulativeSum2d(square)

def create_cumulative_sum_query(cs, x, y, k, area_type):
    size = k * 2
    if area_type == 'main':
        return cs.query(x, y, min(size, x+k-1), min(size, y+k-1))
    if area_type == 'left':
        return cs.query(1, y, x-k-1, min(size, y+k-1))
    if area_type == 'top':
        return cs.query(x, 1, min(size, x+k-1), y-k-1)
    if area_type == 'left_top':
        return cs.query(max(1, x-k), max(1, y-k), x-1, y-1)
    if area_type == 'left_bottom':
        return cs.query(max(1, x-k), y+k, x-1, size)
    if area_type == 'right_top':
        return cs.query(x+k, max(1, y-k), size, y-1)
    if area_type == 'right_bottom':
        return cs.query(x+k, y+k, size, size)
    return 0

def main_loop(cs, k):
    size = k * 2
    max_ans = 0
    for x in range(1, size+1):
        for y in range(1, size+1):
            sumd = 0
            sumd += create_cumulative_sum_query(cs, x, y, k, 'main')
            if x - k > 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'left')
            if y - k > 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'top')
            if x > 1 and y > 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'left_top')
            if x > 1 and y - k < 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'left_bottom')
            if x - k < 1 and y > 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'right_top')
            if x - k < 1 and y - k < 1:
                sumd += create_cumulative_sum_query(cs, x, y, k, 'right_bottom')
            if sumd > max_ans:
                max_ans = sumd
    return max_ans

class CumulativeSum2d():
    def __init__(self, collection_2d):
        self._build(collection_2d)

    def _build(self, collection_2d):
        yl = len(collection_2d)
        xl = len(collection_2d[0])
        self.data = [[0] * (xl+1) for _ in range(yl+1)]
        for y in range(1, yl+1):
            for x in range(1, xl+1):
                top_sum         = self.data[y-1][x]
                left_sum        = self.data[y][x-1]
                dup_sum         = self.data[y-1][x-1]
                self.data[y][x] = top_sum + left_sum - dup_sum
                self.data[y][x] += collection_2d[y-1][x-1]

    def query(self, x, y, x1, y1):
        return self.data[y1][x1] - self.data[y-1][x1] - self.data[y1][x-1] + self.data[y-1][x-1]

def main():
    n, k = parse_input()
    square = initialize_square(k)
    process_entries(n, k, square)
    cs = get_square_cumulative_sum(square)
    ans = main_loop(cs, k)
    print(ans, flush=True)

main()