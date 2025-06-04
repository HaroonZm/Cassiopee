def is_triangle_num(x):
    # check if x is a triangular number: k(k+1)/2 = x
    k = 1
    while k * (k + 1) // 2 < x:
        k += 1
    return k * (k + 1) // 2 == x, k

def is_triangle_shape(arr, k):
    # check if arr forms 1,2,3,...,k
    if len(arr) != k:
        return False
    for i in range(k):
        if arr[i] != i + 1:
            return False
    return True

def solve(N, blocks):
    total = sum(blocks)
    ok, k = is_triangle_num(total)
    if not ok:
        return -1

    arr = blocks[:]

    for step in range(10001):
        if is_triangle_shape(arr, k):
            return step
        # move bottom row blocks (blocks with height >= 1)
        bottom_blocks = [1]*len(arr)
        # all blocks in bottom row
        
        moved_blocks = bottom_blocks
        moved_count = sum(moved_blocks)
        # remove bottom blocks
        arr = [arr[i]-moved_blocks[i] for i in range(len(arr))]
        # filter zeros
        arr = [v for v in arr if v > 0]
        # moved bottom blocks all placed at right end with height 1
        arr += [1]*moved_count

        # left shift to remove gaps
        # gaps are zeros removed above already, so no zeros now

    return -1

while True:
    N = int(input())
    if N == 0:
        break
    blocks_line = input()
    blocks = list(map(int, blocks_line.split()))
    print(solve(N, blocks))