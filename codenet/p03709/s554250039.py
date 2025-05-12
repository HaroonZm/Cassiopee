from bisect import bisect_left, bisect_right
import fileinput

MODULO = 1000000007
n = 0

# HANDLE INPUT
def handle_input():
    iterator = fileinput.input()
    global n
    n = int(next(iterator))
    takahashis = [None] * n
    for i in xrange(n):
        x, v = next(iterator).split()
        takahashis[i] = (int(x), int(v))
    return takahashis

def build_blocks(takahashis):
    result = [-1] * (n + 1)
    max_velocities = [0] * n
    min_velocities = [MODULO] * (n + 1)
    for i in xrange(n):
        max_velocities[i] = max(max_velocities[i - 1], takahashis[i][1])
    for i in xrange(n-1, -1, -1):
        min_velocities[i] = min(min_velocities[i + 1], takahashis[i][1])
    for i in xrange(n):
        current_velocity = takahashis[i][1]
        block_start = bisect_left(max_velocities, current_velocity)
        block_end = bisect_right(min_velocities, current_velocity) - 1
        result[block_end] = max(result[block_end], block_start)
    return result

def compute_possibilities(blocks):
    possibilities = [1] * (n + 2)
    zeros_end_cursor = -2
    for current_position in xrange(n):
        result = 2 * possibilities[current_position - 1]
        # Remove possibiltiies for (00..)1{.....} sequences.
        while zeros_end_cursor < blocks[current_position] - 1:
            result -= possibilities[zeros_end_cursor]
            zeros_end_cursor += 1
        possibilities[current_position] = result % MODULO
    return possibilities[n - 1]

def main():
    takahashis = handle_input()
    takahashis.sort()
    blocks = build_blocks(takahashis)
    return compute_possibilities(blocks)

if __name__ == '__main__':
    print main()