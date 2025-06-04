import sys
import heapq

def read_input():
    """
    Read input from standard input and parse values needed for the problem.

    Returns:
        tuple: The various parameters and lists describing states.
    """
    input = sys.stdin.readline
    # Read configuration parameters
    X, Y, Z, N, M, S, T = map(int, input().split())
    
    # Read state transition data for the CS and CC sets, 
    # with one dummy state at index 0 for ease of indexing.
    CS = [[0, 0, 0]] + [list(map(int, input().split())) + [i + 1] + [0] for i in range(N)]
    CC = [[0, 0, 0]] + [list(map(int, input().split())) + [i + 1] + [1] for i in range(M)]
    
    return X, Y, Z, N, M, S, T, CS, CC

def build_transition_lists(X, Y, Z, N, M, CS, CC):
    """
    Build adjacency lists representing possible transitions for each type of move.

    Args:
        X (int): Number of types for the first attribute.
        Y (int): Number of types for the second attribute.
        Z (int): Number of types for the third attribute.
        N (int): Number of CS states.
        M (int): Number of CC states.
        CS (list): List of CS states.
        CC (list): List of CC states.

    Returns:
        tuple: Adjacency lists for each type of move/transition.
    """
    # Prepare adjacency lists for efficient transitions
    CS_SLIST = [[] for _ in range(X + 1)]  # For CS by x index
    CS_CLIST = [[] for _ in range(Y + 1)]  # For CS by y index
    CC_CLIST = [[] for _ in range(Y + 1)]  # For CC by first index
    CC_ULIST = [[] for _ in range(Z + 1)]  # For CC by y index
    
    # Populate transition lists for each CS state
    for x, y, z, _ in CS[1:]:
        CS_SLIST[x].append(z)  # For each x, keep list of possible z
        CS_CLIST[y].append(z)  # For each y, keep list of possible z
    
    # Populate transition lists for each CC state
    for x, y, z, _ in CC[1:]:
        CC_CLIST[x].append(z)  # For CC, key by first index (x)
        CC_ULIST[y].append(z)  # For CC, key by y
    
    return CS_SLIST, CS_CLIST, CC_CLIST, CC_ULIST

def find_minimum_cost(X, Y, Z, N, M, S, T, CS, CC, CS_SLIST, CS_CLIST, CC_CLIST, CC_ULIST):
    """
    Implements a modified Dijkstra's algorithm to find the minimal cost from state S to T.

    Args:
        X (int): Number of types for the first attribute.
        Y (int): Number of types for the second attribute.
        Z (int): Number of types for the third attribute.
        N (int): Number of CS states.
        M (int): Number of CC states.
        S (int): Starting state index in CS.
        T (int): Target state index in CC.
        CS (list): List of CS states.
        CC (list): List of CC states.
        CS_SLIST (list): Adjacency for CS transitions by x.
        CS_CLIST (list): Adjacency for CS transitions by y.
        CC_CLIST (list): Adjacency for CC transitions by x.
        CC_ULIST (list): Adjacency for CC transitions by y.

    Returns:
        int: The minimal cost to reach state T in CC, or -1 if unreachable.
    """
    # Initialize costs for states: very high (infinity)
    MINCOST_CS = [1 << 30] * (N + 1)  # Minimal cost to reach each CS state
    MINCOST_CC = [1 << 30] * (M + 1)  # Minimal cost to reach each CC state
    
    MINCOST_CS[S] = 0  # Starting state cost is 0
    
    # Priority queue for Dijkstra's algorithm: cost, x, y, z, state type
    # State type: 0 for CS, 1 for CC
    queue = [[0] + CS[S]]

    # Flags to mark which attribute transitions have been used to avoid double-processing
    USED_S = [0] * (X + 1)  # For attribute x in CS
    USED_C = [0] * (Y + 1)  # For attribute y in CS and CC
    USED_U = [0] * (Z + 1)  # For attribute z in CC

    while queue:
        # Pop the state with the current minimal cost
        cost, x, y, z, cs = heapq.heappop(queue)
        
        if cs == 0:
            # Current state is in CS set
            
            # Try all transitions via attribute x
            if USED_S[x] == 0:
                USED_S[x] = 1
                for to in CS_SLIST[x]:
                    if MINCOST_CS[to] > cost + 1:
                        MINCOST_CS[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CS[to])
            
            # Try all transitions via attribute y (to both CS and CC)
            if USED_C[y] == 0:
                USED_C[y] = 1
                # To CS
                for to in CS_CLIST[y]:
                    if MINCOST_CS[to] > cost + 1:
                        MINCOST_CS[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CS[to])
                # To CC
                for to in CC_CLIST[y]:
                    if MINCOST_CC[to] > cost + 1:
                        MINCOST_CC[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CC[to])
        else:
            # Current state is in CC set
            
            # Try all transitions via attribute y (only to CC via CC_ULIST)
            if USED_U[y] == 0:
                USED_U[y] = 1
                for to in CC_ULIST[y]:
                    if MINCOST_CC[to] > cost + 1:
                        MINCOST_CC[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CC[to])
            
            # Try all transitions via attribute x (to CS and CC)
            if USED_C[x] == 0:
                USED_C[x] = 1
                # To CS
                for to in CS_CLIST[x]:
                    if MINCOST_CS[to] > cost + 1:
                        MINCOST_CS[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CS[to])
                # To CC
                for to in CC_CLIST[x]:
                    if MINCOST_CC[to] > cost + 1:
                        MINCOST_CC[to] = cost + 1
                        heapq.heappush(queue, [cost + 1] + CC[to])

    # If the target state in CC set has not been reached, return -1
    if MINCOST_CC[T] == (1 << 30):
        return -1
    else:
        return MINCOST_CC[T]

def main():
    """
    Main execution function: reads input, builds data structures, and prints result.
    """
    # Read and parse all input data
    X, Y, Z, N, M, S, T, CS, CC = read_input()
    # Build adjacency lists for all transition rules
    CS_SLIST, CS_CLIST, CC_CLIST, CC_ULIST = build_transition_lists(X, Y, Z, N, M, CS, CC)
    # Find the minimal number of operations to reach the target state
    result = find_minimum_cost(X, Y, Z, N, M, S, T, CS, CC, CS_SLIST, CS_CLIST, CC_CLIST, CC_ULIST)
    print(result)

if __name__ == '__main__':
    main()