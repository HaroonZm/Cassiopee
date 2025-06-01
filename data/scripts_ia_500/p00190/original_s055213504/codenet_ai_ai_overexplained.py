from math import factorial
from Queue import PriorityQueue

# Calculate factorials of numbers from 0 up to 12 (inclusive) and store them in a list.
# Factorials are important in permutation-related hashing functions used later.
FACTORIAL = [factorial(i) for i in xrange(13)]

# Define constants representing movement directions.
# These will be used as indices when accessing movement neighbors in the MOVE list.
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3

# Initialize a list MOVE of length 13, where each element starts as [0].
# This will be replaced with lists representing potential moves from each cell.
MOVE = [[0] for _ in xrange(13)]

# Define the allowed moves from each position (0 to 12).
# Each sublist corresponds to possible adjacent cell indices in the order [LEFT, UP, RIGHT, DOWN].
# A value of -1 means no move is possible in that direction from that cell.
MOVE[0] =  [-1, -1, -1,  2]
MOVE[1] =  [-1, -1,  2,  5]
MOVE[2] =  [ 1,  0,  3,  6]
MOVE[3] =  [ 2, -1, -1,  7]
MOVE[4] =  [-1, -1,  5, -1]
MOVE[5] =  [ 4,  1,  6,  9]
MOVE[6] =  [ 5,  2,  7, 10]
MOVE[7] =  [ 6,  3,  8, 11]
MOVE[8] =  [ 7, -1, -1, -1]
MOVE[9] =  [-1,  5, 10, -1]
MOVE[10] = [ 9,  6, 11, 12]
MOVE[11] = [10,  7, -1, -1]
MOVE[12] = [-1, 10, -1, -1]

# Define a function to compute a unique hash for a given permutation 'cell'.
# This hash enables fast looking-up of states in puzzles or permutations.
def hash(cell):
    # Create a copy of the cell list to manipulate without modifying the original.
    work = cell[:]
    # Initialize the hash accumulator as 0.
    hash = 0
    # Loop through the first 12 elements of the cell list.
    for i in xrange(12):
        # Add the current element multiplied by the factorial of the decreasing index.
        hash += work[i] * FACTORIAL[13 - 1 - i]
        # For each element j after i, if element j is greater than element i,
        # decrement element j by 1 to maintain a proper encoding.
        for ii in xrange(i + 1, 13):
            if work[ii] > work[i]:
                work[ii] -= 1
    # Return the computed hash value representing the permutation.
    return hash

# Define a function to convert a hash value back into its corresponding permutation (dehash).
def dehash(key):
    # Initialize an empty list to store the recovered permutation.
    cell = []
    # For each position i from 0 to 12, calculate the coefficient for the factorial term.
    for i in xrange(13):
        # Integer division of key by the relevant factorial gives the digit at position i.
        cell.append(key / FACTORIAL[13 - 1 - i])
        # Set the remainder of the division as the new key for subsequent digits.
        key %= FACTORIAL[13 - 1 - i]
    # To reconstruct the actual permutation, adjust values to recover original digits.
    # Iterate backward through the positions.
    for i in xrange(13 - 1, -1, -1):
        # For each element after i, increment it if it is greater or equal to cell[i].
        for ii in xrange(i + 1, 13):
            if cell[i] <= cell[ii]:
                cell[ii] += 1
    # Return the reconstructed permutation list.
    return cell

# Define an evaluation function to calculate a heuristic score for a given cell configuration.
# The score estimates how far the permutation is from the goal state using Manhattan distance.
def evaluate(cell):
    # Each index represents a cell number and each sublist contains its coordinates (row, column).
    point = [
        [0, 2],
        [1, 1], [1, 2], [1, 3],
        [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
        [3, 1], [3, 2], [3, 3],
        [4, 2]
    ]
    # Initialize evaluation score to zero.
    eva = 0
    # Loop over all cell positions.
    for i in xrange(13):
        # Skip if cell[i] is 0 or 12 (presumably the empty spaces or corners).
        if not (cell[i] == 0 or cell[i] == 12):
            # Calculate the Manhattan distance between the current position i and target position cell[i].
            eva += abs(point[cell[i]][0] - point[i][0])
            eva += abs(point[cell[i]][1] - point[i][1])
    # Return the sum of distances as the heuristic evaluation score.
    return eva

# Precompute hash values of the two solved states as target configurations for quick lookup.
ANS_HASH = [
    hash([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    hash([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
]

# Begin an infinite loop to process multiple test cases until input signals termination.
while True:
    # Read initial input value and wrap it in a list to start building the puzzle state.
    p = [input()]
    # Check if the input is -1; if so, exit the loop and end the program.
    if p == [-1]:
        break
    # For four iterations (representing four rows or input lines):
    for u in xrange(4):
        # Read space-separated values from input, convert them to integers and extend list p.
        for pp in map(int, raw_input().split()):
            p.append(pp)
    # Replace the zero in the puzzle state with 12 to represent the empty cell with a specific id.
    p[p.index(0)] = 12

    # Initialize a priority queue to hold states prioritized by their evaluation score.
    pq = PriorityQueue()
    # Put the initial state into the priority queue with the evaluation, its hash, and 0 steps.
    pq.put([evaluate(p), hash(p), 0])
    # Dictionary visited will record hashes of states already processed to avoid repeats.
    visited = {}
    visited[hash(p)] = True
    # If the initial hash is already a solved state, set ans to 0; else mark it as "NA" (not available).
    ans = 0 if hash(p) in ANS_HASH else "NA"

    # Main search loop continues while we still have states to explore in the priority queue.
    # Cur is a list of [evaluation score, hash key, steps taken so far].
    while not pq.empty():
        # Get the state with the lowest evaluation from the priority queue.
        eva, cur_hash, cur_step = pq.get()
        # Convert hash back into a cell configuration.
        cur_cell = dehash(cur_hash)

        # If the heuristic evaluation is not better than 20 or answer was found, break the loop.
        if not (eva <= 20 and ans == "NA"):
            break

        # Iterate over all positions in cur_cell to find the empty cell(s), IDs 0 or 12.
        for i in xrange(13):
            if cur_cell[i] == 0 or cur_cell[i] == 12:
                # Try moving the empty cell in each direction: LEFT, UP, RIGHT, DOWN.
                for ii in [LEFT, UP, RIGHT, DOWN]:
                    # Check if the move from position i in direction ii is legal (not -1).
                    if not MOVE[i][ii] == -1:
                        # Swap current empty cell with adjacent cell in direction ii.
                        cur_cell[i], cur_cell[MOVE[i][ii]] = cur_cell[MOVE[i][ii]], cur_cell[i]
                        # Compute the hash key for the new configuration.
                        hashkey = hash(cur_cell)
                        # If we haven't visited this state before:
                        if not hashkey in visited:
                            # If the new state matches a solution, update ans and break loops.
                            if hashkey in ANS_HASH:
                                ans = cur_step + 1
                                break
                            # Otherwise, add the new state to the priority queue with updated evaluation.
                            pq.put([evaluate(cur_cell) + cur_step + 1, hashkey, cur_step + 1])
                            # Mark this state as visited.
                            visited[hashkey] = True
                        # Swap back to restore the original state before next trials.
                        cur_cell[i], cur_cell[MOVE[i][ii]] = cur_cell[MOVE[i][ii]], cur_cell[i]
    # Print the number of steps in the solution, or "NA" if unsolved within heuristic limit.
    print ans