import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

# Change the maximum depth of the Python interpreter stack to prevent recursion errors in deep recursions.
sys.setrecursionlimit(10**7)

# Define a variable `inf` as a very large integer. The value 10 raised to the 20th power is used.
inf = 10**20

# Define a variable `eps` as a very small floating point value (1 divided by 10^13).
eps = 1.0 / 10**13

# Define a variable `mod` as a large prime number, often used for modulo operations in programming contests.
mod = 10**9+7

# Define a list `dd` representing the four cardinal directions as (dy, dx) pairs: up, right, down, left.
dd = [(-1,0),(0,1),(1,0),(0,-1)]

# Define a list `ddn` representing the eight directions on a 2D grid (including diagonals).
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Function to read a line from standard input, split it by whitespace, convert each item to int, and return as a list.
def LI(): 
    return [int(x) for x in sys.stdin.readline().split()]

# Function to read a line as integers, decrement each by 1 (often for 0-based indexing), and return the list.
def LI_(): 
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Function to read a line, convert each whitespace-separated token to a float, and return as a list.
def LF(): 
    return [float(x) for x in sys.stdin.readline().split()]

# Function to read a line from standard input and split the line into a list of strings by whitespace.
def LS(): 
    return sys.stdin.readline().split()

# Function to read a line from standard input and convert it to an integer.
def I(): 
    return int(sys.stdin.readline())

# Function to read a line from standard input and convert it to a float.
def F(): 
    return float(sys.stdin.readline())

# Function to read a line from standard input as a string.
def S(): 
    return input()

# Function to print a value `s` and flush the standard output buffer to ensure it appears immediately.
def pf(s): 
    return print(s, flush=True)

# Definition of a class named Flow, used to solve network flow problems.
class Flow():
    # Constructor for the Flow class. It initializes the object's variables.
    def __init__(self, e, N):
        # `E` is the edge capacity matrix (adjacency matrix); `N` is the number of nodes.
        self.E = e
        self.N = N

    # Computes the maximum flow from source node `s` to target node `t`.
    def max_flow(self, s, t):
        # Initialize the variable `r` that accumulates the flow (number of successful augmenting paths).
        r = 0
        # For convenience, assign the edge capacity matrix to local variable `e`.
        e = self.E

        # Define an inner recursive function to perform depth-first search from node `c`.
        def f(c):
            # Mark the current node as visited by setting `v[c]` to 1.
            v = self.v
            v[c] = 1
            # If the target node is reached, signal a successful path by returning 1.
            if c == t:
                return 1
            # Try each other node as a possible next node in the path.
            for i in range(self.N):
                # If node `i` has not been visited, there is available capacity, and
                # we find an augmenting path recursively, perform the flow augmentation.
                if v[i] == 0 and e[c][i] > 0 and f(i) > 0:
                    # Decrement the capacity from `c` to `i` (we use this edge).
                    e[c][i] -= 1
                    # Increment the capacity from `i` to `c` (reverse edge for residual graph).
                    e[i][c] += 1
                    # Return success up the recursion.
                    return 1
            # If no path is found from this node, return 0.
            return 0

        # Loop to search for augmenting paths repeatedly (as long as found).
        while True:
            # Reset the visited list for each search.
            self.v = [0] * self.N
            # If no augmenting path exists from source node `s`, break loop.
            if f(s) == 0:
                break
            # Each time an augmenting path is found, increment the flow count.
            r += 1

        # After no more paths can be found, return the maximum flow value.
        return r

# Define the main function that will be executed.
def main():
    # Initialize an empty list `rr` for results to be collected.
    rr = []

    # Define a function `f` that processes a network and computes values related to max-flow/min-cut.
    def f(n, m):
        # Read `m` edges from input, each as a pair of node indices (zero-based).
        a = [LI_() for _ in range(m)]
        # Read the source and sink nodes for the flow computation (decremented for 0-based indexing).
        s, t = LI_()
        # Initialize a 2D list (matrix) of zeros for edge capacities.
        e = [[0]*n for _ in range(n)]
        # For each undirected edge, set capacity from x->y and y->x to 1.
        for x, y in a:
            e[x][y] = 1
            e[y][x] = 1
        # Create a Flow object to compute max-flow.
        fl = Flow(e, n)
        # Compute the maximum flow from source `s` to sink `t`.
        r = fl.max_flow(s, t)
        # Initialize a list to hold the indices of edges that are in the computed minimum cut.
        re = []
        # For each edge, check if it is saturated (i.e., part of min-cut) by seeing if residual capacity is 0.
        for i in range(m):
            x, y = a[i]
            # Check if the edge from y to x in the residual graph has zero capacity (saturated). 
            if e[y][x] == 0:
                # Edge is part of the minimum cut; store its 1-based index.
                re.append(i+1)
        # Return a list: maximum flow value, number of cut edges, and the indices of the cut edges.
        return [r, len(re)] + re

    # Enter an infinite loop to read datasets until a stopping condition is met.
    while 1:
        # Read two integers: number of nodes `n` and number of edges `m`.
        n, m = LI()
        # If `n` is zero, this signals the end of input and we break the loop.
        if n == 0:
            break
        # Call function `f` and extend the result list `rr` with the returned values.
        rr.extend(f(n, m))
        # The next statement is commented out. It may have been for debugging.
        # print('rr', rr[-1])
        # The break here seems to temporarily disable reading multiple datasets.
        break

    # Convert the numerical results in `rr` to strings and join them with newline characters for display.
    return '\n'.join(map(str, rr))

# Call the main function and print its result to standard output.
print(main())