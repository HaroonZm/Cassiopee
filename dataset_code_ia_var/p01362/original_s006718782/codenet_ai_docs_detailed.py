from collections import deque

def main():
    """
    Main function to process puzzle input grids, generate all unique rotations of a dice using BFS,
    and determine the minimum rotation steps to satisfy given grid constraints.
    Reads grids from standard input until a line with '#' is encountered.
    For each grid, outputs the minimum dice rotation steps according to the specified criteria.
    """

    # I: Dict mapping dice faces to sets of tuples representing constraints for validation.
    # Each key (face number) maps to a tuple of ((face, index), ...).
    I = {
        1: ((6, 0), (2, 1), (5, 2), (4, 3)),
        2: ((6, 3), (3, 1), (5, 3), (1, 3)),
        3: ((6, 2), (4, 1), (5, 0), (2, 3)),
        4: ((6, 1), (1, 1), (5, 1), (3, 3)),
        5: ((1, 0), (2, 0), (3, 0), (4, 0)),
        6: ((1, 2), (2, 2), (3, 2), (4, 2)),
    }

    # J: List where each sublist gives indices to check for '*' on sides of 3x3 grid faces
    J = [
        [6, 7, 8], # bottom row of grid
        [2, 5, 8], # right column of grid
        [0, 1, 2], # top row of grid
        [0, 3, 6]  # left column of grid
    ]

    # D: Each tuple represents new face positions after a dice rotation
    # Orders: (U)p, (R)ight, (D)own, (L)eft
    D = [
        (1, 5, 2, 3, 0, 4), # U: rotate up
        (3, 1, 0, 5, 4, 2), # R: rotate right
        (4, 0, 2, 3, 5, 1), # D: rotate down
        (2, 1, 5, 0, 4, 3), # L: rotate left
    ]

    def rotate_dice(L, k):
        """
        Return a tuple representing the dice's new orientation after a rotation.
        Args:
            L (tuple): Current orientation of the dice as a 6-tuple.
            k (int): Index for the rotation direction (0=U, 1=R, 2=D, 3=L).
        Returns:
            tuple: New dice orientation after rotation.
        """
        return tuple(L[e] for e in D[k])

    # R: Initial orientation of the dice, labeled by face numbers (1-6)
    R = (5, 1, 2, 4, 3, 6)  # Arbitrary canonical start orientation

    # BFS queue to enumerate all unique dice orientations and minimal rotation counts
    que = deque()
    dist = {R: 0}  # Map orientation tuple to minimum rotation steps
    que.append(R)
    while que:
        s = que.popleft()
        d = dist[s]
        for i in range(4):  # Try each of the four possible 90-degree rotations
            t = rotate_dice(s, i)
            if t in dist:
                continue
            dist[t] = d + 1
            que.append(t)

    # C: 6-element list where each item is a concatenated string representing a dice face grid (3x3).
    C = [None] * 6
    while True:
        S = input()  # Read the first line of a grid, or '#' to terminate
        if S == '#':
            break
        # Read one complete dice representation (6 faces, each a 3x3 grid)
        C[0] = "".join([S, input(), input()])
        for i in range(5):
            C[i + 1] = "".join([input() for _ in range(3)])

        ans = 10  # Initialize with a value greater than any possible minimum number of rotations

        # For each valid dice orientation (as discovered in BFS):
        for s, v in dist.items():
            a = s[0]  # Index of the current 'top' face
            b = s[1]  # Index of the current 'front' face

            # Loop over each tuple of possible connections/corners from face 'a':
            for k, (i, e) in enumerate(I[a]):
                if i == b:  # Find the relative position where the front face matches
                    # j: third face, f: edge index to test for '*'
                    j, f = I[a][k - 2]
                    # Check whether the corresponding edges (J[e], J[f]) contain at least one '*'
                    if any(C[i - 1][k1] == '*' for k1 in J[e]) and any(C[j - 1][k2] == '*' for k2 in J[f]):
                        ans = min(ans, v)  # Update answer with the minimal rotation count
                    break

        print(ans)  # Output the minimal number of rotations needed
        input()     # Skip the blank line between puzzles

if __name__ == "__main__":
    main()