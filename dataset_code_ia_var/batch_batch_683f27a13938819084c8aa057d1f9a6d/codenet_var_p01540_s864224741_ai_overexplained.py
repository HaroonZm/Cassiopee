from bisect import bisect_left  # "bisect_left" is a function used to find the position in a sorted list where the given value should be inserted to maintain order.

def main():
    # Read the first line of input and split it into two integers.
    # N is the number of treasures, M is the number of queries (areas to search for treasures).
    N, M = map(int, input().split())
    
    treasures = []  # This list will store all the treasures as (x, y) coordinate pairs.

    # Create two sets to keep track of all unique x and y coordinates among all treasures.
    # Sets are used to ensure there are no duplicate coordinates in the collected data.
    Xs = set()  # For x-coordinates
    Ys = set()  # For y-coordinates

    # Read each treasure's coordinates and store them.
    for _ in range(N):
        x, y = map(int, input().split())   # Read x and y coordinates for a treasure
        treasures.append((x, y))           # Store the tuple (x, y) in the treasures list
        Xs.add(x)                          # Add x to the set of x-coordinates
        Ys.add(y)                          # Add y to the set of y-coordinates

    # "Coordinate compression":
    # Since the possible coordinate values may be large or sparse, 
    # we convert actual coordinate values into "indices" for efficient array access.
    Xs = list(Xs)    # Convert x-coordinates set to a list
    Xs.sort()        # Sort the list in ascending order
    Ys = list(Ys)    # Convert y-coordinates set to a list
    Ys.sort()        # Sort the list in ascending order

    # Dictionaries to map each real coordinate value to its "compressed" index.
    # For example, if sorted Xs = [13, 73, 100], then 13->0, 73->1, 100->2.
    Xd = {}  # Dictionary for x-coordinate compression
    Yd = {}  # Dictionary for y-coordinate compression

    # Assign an index to each unique x-coordinate
    for i, x in enumerate(Xs):
        Xd[x] = i
    # Assign an index to each unique y-coordinate
    for i, y in enumerate(Ys):
        Yd[y] = i

    # Get count of unique x and y coordinates, which will be dimensions for our 2D array
    lx = len(Xs)  # Number of unique x indices
    ly = len(Ys)  # Number of unique y indices

    # Create a 2D array for storing compressed treasure counts.
    # This will be used to mark how many treasures exist at every (compressed) coordinate.
    # The array has one extra row and column (hence +1) to make cumulative sum calculations easier (1-based index).
    compressd_treasures = [[0 for _ in range(lx + 1)] for _ in range(ly + 1)]

    # Populate the 2D array:
    # For each treasure at (x, y), increment the count at the appropriate compressed coordinate.
    # Note: indices are shifted by +1 since we are using 1-based indices for cumulative sum calculation.
    for x, y in treasures:
        compressd_treasures[Yd[y] + 1][Xd[x] + 1] += 1

    # Build the 2-dimensional prefix sum (cumulative sum) array.
    # This lets us quickly query the total number of treasures in any rectangle by a few array accesses.
    # The prefix sum for position (y, x) represents the total number of treasures in the rectangle
    # from (1, 1) to (y, x), inclusive, in the compressed coordinate system.
    for y in range(1, ly + 1):    # Iterate over y indices (rows), starting from 1
        acc = 0                   # "acc" will accumulate values for prefix sum along the x-direction (row-wise)
        for x in range(1, lx + 1):    # Iterate over x indices (columns), starting from 1
            acc += compressd_treasures[y][x]  # Add the value to acc (row-wise accumulation)
            # Add the row-wise accumulation (acc) to the column-wise prefix (from the row above)
            compressd_treasures[y][x] = acc + compressd_treasures[y-1][x]

    # For each query, determine how many treasures are in the specified rectangular area.
    for _ in range(M):
        # Read the rectangle's two corners (bottom-left and top-right)
        # Each query specifies the range [x1, x2], [y1, y2]
        x1, y1, x2, y2 = map(int, input().split())
        
        # Convert the query's real coordinates into compressed indices.
        # bisect_left finds where to insert the coordinate in the sorted list so that order is preserved.
        # This gives us the first index where the coordinate is not less than the query value.
        idx_x1 = bisect_left(Xs, x1)  # For left x boundary
        idx_x2 = bisect_left(Xs, x2)  # For right x boundary
        idx_y1 = bisect_left(Ys, y1)  # For lower y boundary
        idx_y2 = bisect_left(Ys, y2)  # For upper y boundary

        # Handle the case when the boundary is exactly on a treasure.
        # If x2 exists in Xs, need to include it in the range.
        # Same for y2 and Ys.
        if idx_x2 < lx and Xs[idx_x2] == x2:
            idx_x2 += 1
        if idx_y2 < ly and Ys[idx_y2] == y2:
            idx_y2 += 1
        
        # Using the 2D prefix sum, calculate the total number of treasures in the rectangle:
        # (x1, y1) ~ (x2, y2), inclusive of boundaries.
        # This uses the inclusion-exclusion principle for 2D prefix sums.
        # The formula is:
        # total = S(y2,x2) - S(y2,x1) - S(y1,x2) + S(y1,x1)
        ans = (
            compressd_treasures[idx_y2][idx_x2]
            - compressd_treasures[idx_y2][idx_x1]
            - compressd_treasures[idx_y1][idx_x2]
            + compressd_treasures[idx_y1][idx_x1]
        )
        print(ans)  # Output the answer for this query

if __name__ == "__main__":
    main()  # Invoke main function when this script is run directly