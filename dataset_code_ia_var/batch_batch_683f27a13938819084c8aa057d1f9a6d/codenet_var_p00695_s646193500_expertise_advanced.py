import sys

def checkio(data):
    from itertools import accumulate

    y, x = len(data), len(data[0])
    m = [[0] * x for _ in range(y)]

    for j, row in enumerate(data):
        m[j] = list(accumulate(row, lambda r, v: (r + 1) * v if v else 0))
    
    max_rect = 0
    for i in range(x):
        col = [m[j][i] for j in range(y)]
        stack, heights = [], []
        for idx, height in enumerate(col + [0]):
            start = idx
            while heights and heights[-1][1] > height:
                prev_idx, h = heights.pop()
                max_rect = max(max_rect, h * (idx - prev_idx))
                start = prev_idx
            heights.append((start, height))
    return max_rect

if __name__ == '__main__':
    input_func = input if sys.version_info[0] >= 3 else raw_input
    try:
        n = int(input_func())
        for _ in range(n):
            data = [list(map(int, input_func().split())) for _ in range(5)]
            print(checkio(data))
            input_func()
    except EOFError:
        pass