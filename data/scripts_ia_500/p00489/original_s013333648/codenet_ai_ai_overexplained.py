def f():
    # Import the functions heappop and heappush from the heapq module
    # heapq module provides an implementation of the min-heap data structure
    # heappop removes and returns the smallest element from the heap
    # heappush adds a new element to the heap while maintaining the heap property
    from heapq import heappop, heappush

    # Read an integer value N from standard input (typically user input or a file)
    # input() reads a line from input as a string
    # int() converts that string to an integer
    N = int(input())

    # Initialize a list r of length N with all elements set to 0
    # This will track some scores or points associated with each of the N entities
    r = [0] * N  

    # The expression N*~-N//2 is a somewhat cryptic way to calculate the number of edges or matches
    # ~-N is equivalent to N-1 because ~-x equals x-1 in two's complement arithmetic
    # So N*~-N//2 is the same as N*(N-1)//2, which is the number of pairs in combinations of N items
    # for each pair, read the scores of two sides of a match and assign points accordingly
    for _ in [0] * (N * ~-N // 2):  
        # For each match, read four integers: a, b, c, d
        # a and b are indices (likely representing teams or players)
        # c and d are scores of those teams in the match
        a, b, c, d = map(int, input().split())

        # Update the scores list r according to these rules:
        # For the team with index a-1 (convert to zero-based index), add:
        # 3 points if c > d, which means team a won
        # 1 point if c == d, which means a draw
        # 0 points if c < d (implicitly from multiplication)
        r[a - 1] += 3 * (c > d) + (c == d)

        # Similarly for team with index b-1:
        # 3 points if d > c, 1 point if tie, 0 if loss
        r[b - 1] += 3 * (d > c) + (d == c)

    # Create a list of empty lists, where the length is three times N
    # This list b will be used to bucket teams by their point scores
    # The reason for 3*N size is probably based on the maximum possible point value
    b = [[] for _ in [0] * (N * 3)]

    # For each team i in 0 to N-1, append the team index i to the bucket corresponding to their score r[i]
    # So b[score] will hold all teams with that score
    for i in range(N):
        b[r[i]] += [i]

    # Initialize an empty priority queue (min-heap)
    pq = []

    # For each team index i and its score s,
    # push a tuple [-s, i] onto the heap
    # Negate the score to simulate a max-heap because heapq is a min-heap by default
    # This way, teams with higher scores come out first when we pop from the heap
    for i, s in enumerate(r):
        heappush(pq, [-s, i])

    # Initialize rank variables:
    # rank will track the ranking number assigned to a team
    rank = 1

    # display_rank keeps count of the order in which teams are popped from the heap, starting at 1
    display_rank = 1

    # prev_score is initialized to positive infinity to ensure the first comparison sets the first rank properly
    prev_score = float('inf')

    # While there are elements in the priority queue (teams not yet ranked)
    while pq:
        # Pop the next element from the heap, which will be the team with the highest score left
        s, i = heappop(pq)

        # If the score has changed from the previous team's score,
        # update the rank to match the current display_rank
        # This handles teams with the same score receiving the same rank
        if s != prev_score:
            rank = display_rank

        # Assign the rank to the team's position in the score list r (repurposing r to hold ranks now)
        r[i] = rank

        # Increment display_rank for the next team to be ranked (whether same or different score)
        display_rank += 1

        # Update prev_score for the next iteration comparisons
        prev_score = s

    # Finally, print the ranks of all teams in order
    # Using unpacking (*) to pass all elements of r to print
    # sep='\n' ensures each rank is printed on its own line
    print(*r, sep='\n')

# Call the function f to run the whole process
f()