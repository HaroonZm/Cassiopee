import sys

def main():
    """
    Main function to read the input, construct the adjacency matrix for the given directed graph,
    and print the adjacency matrix.
    
    The input format is:
        n
        u k v1 v2 ... vk
        ...
    where:
        - n: number of vertices
        - For each vertex u:
            - k: number of adjacent vertices
            - v1, v2, ..., vk: indices (1-based) of adjacent vertices
    
    Output:
        - n x n adjacency matrix (each row separated by space), with 1 indicating an edge and 0 otherwise.
    """
    # For fast input reading
    input = sys.stdin.readline

    # Read the number of vertices in the graph
    n = int(input())

    # Initialize an n x n adjacency matrix filled with zeros.
    # nmap[i][j] = 1 if there is an edge from vertex i to vertex j, else 0.
    nmap = [[0 for _ in range(n)] for _ in range(n)]

    # Read adjacency information for each vertex
    for _ in range(n):
        # Read input: first number is the source vertex (1-based),
        # second is the number of adjacent vertices (not used directly),
        # followed by the list of adjacent vertices (1-based indexing).
        l = list(map(int, input().split()))
        a = l[0] - 1  # Convert source vertex to 0-based index

        # Iterate through each adjacent vertex (excluding first two entries)
        for i in l[2:]:
            # Set to 1 to indicate an edge from 'a' to 'i-1'
            nmap[a][i-1] = 1

    # Output the adjacency matrix, each row as space-separated values
    for row in nmap:
        print(*row)

if __name__ == '__main__':
    main()