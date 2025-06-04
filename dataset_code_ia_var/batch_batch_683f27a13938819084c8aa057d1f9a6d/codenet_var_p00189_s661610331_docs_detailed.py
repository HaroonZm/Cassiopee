NULL = 10000   # Constant representing no connection or an infinite distance between towns
TOWN_COUNT = 10   # Maximum number of towns

while True:
    # Read the number of connections for this test case
    input_count = int(input())

    # If input_count is 0, terminate the program (exit condition)
    if input_count == 0:
        break

    # Initialize the adjacency matrix to represent the graph with no connections.
    # By default, all entries are set to NULL (meaning no direct path exists).
    adjacency_matrix = [[NULL] * TOWN_COUNT for _ in range(TOWN_COUNT)]

    # Set distance from each town to itself as 0
    for lp in range(TOWN_COUNT):
        adjacency_matrix[lp][lp] = 0

    # Tracks the largest town index involved to optimize the range of computations
    need_range = 0

    # Read and store all connections between towns
    for _ in range(input_count):
        # Read a connection as three space-separated values: start, end, and time
        start, end, time = [int(item) for item in input().split(" ")]

        # Set the time for both directions since the paths are bidirectional
        adjacency_matrix[start][end] = time
        adjacency_matrix[end][start] = time

        # Update the highest-indexed town participating in any connection
        need_range = max(need_range, start, end)

    # Apply the Floyd-Warshall algorithm to compute the shortest paths between all town pairs
    for intermediate in range(need_range + 1):
        for source in range(need_range + 1):
            for dest in range(need_range + 1):
                # Update the shortest distance from source to dest using the intermediate as a stepping stone
                adjacency_matrix[source][dest] = min(
                    adjacency_matrix[source][intermediate] + adjacency_matrix[intermediate][dest],
                    adjacency_matrix[source][dest]
                )

    min_time = NULL   # Initialize the best (minimal) total distance sum found to infinity
    min_index = -1    # Initialize the index of the town with minimal time to an invalid value

    # Evaluate each town's sum of distances to all other towns
    for index, row in enumerate(adjacency_matrix):
        # Filter out non-zero, finite distances (ignore self-loops and unreachable towns)
        relevant_distances = [dist for dist in row if 0 < dist < NULL]

        if len(relevant_distances) > 0:
            total_time = sum(relevant_distances)

            # If this town has a smaller sum than any previous, remember it
            if total_time < min_time:
                min_time = total_time
                min_index = index

    # Print the index of the best town and the minimal sum of travel times
    print(min_index, min_time)