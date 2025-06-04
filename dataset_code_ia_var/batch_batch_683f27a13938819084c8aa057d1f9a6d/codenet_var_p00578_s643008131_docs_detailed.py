def solve():
    """
    Reads input for the number of heights and the heights themselves,
    processes the data to identify 'island' structures based on changes
    in elevation, and determines the maximum number of islands that 
    appear as the 'water level' rises. It finally prints this maximum count.
    """
    # Read the number of heights from input
    N = int(input())

    # Read the height values; pad the list on both ends with 0 for ease of processing edge cases
    A = [0] + [int(i) for i in input().split()] + [0]

    # List to hold the 'edges' of the islands: each entry contains [height, up_flag]
    # up_flag is True for island 'peak' (start of island), False for 'bottom' (end of island)
    A_edge = []

    # Flag to keep track whether the previous edge was an upwards (True) or downwards (False) slope
    up_flg = True

    # Traverse the heights to identify local peaks and troughs (island edges)
    for i in range(1, len(A) - 1):
        if up_flg:
            # If we are on an upwards segment and encounter a drop, mark as peak
            if A[i] > A[i + 1]:
                A_edge.append([A[i], up_flg])
                up_flg = not up_flg
        else:
            # If we are on a downwards segment and encounter a rise, mark as trough
            if A[i] < A[i + 1]:
                A_edge.append([A[i], up_flg])
                up_flg = not up_flg

    # Sort all island edges in increasing order of height, 
    # so we simulate water level rising from lowest to highest
    A_edge.sort()

    # Initialize counters:
    # island_count - current number of islands exposed
    # max_island_count - records maximum simultaneous islands encountered
    island_count = 1  # Initially, count is 1 as there's at least one segment
    max_island_count = 1

    # Process all edges to simulate rising water and count islands
    for i in range(len(A_edge) - 1):
        if A_edge[i][1]:
            # If it's a peak, the 'top' disappears as water rises over
            island_count -= 1
        else:
            # If it's a trough, a new island emerges as water drops below this point
            island_count += 1
        # Only update max if the next edge is at a higher height
        if A_edge[i][0] < A_edge[i + 1][0]:
            max_island_count = max(max_island_count, island_count)

    # Special case: if all heights are zero or negative, there cannot be any islands
    if max(A) <= 0:
        max_island_count = 0

    # Output the final result
    print(max_island_count)

if __name__ == '__main__':
    solve()