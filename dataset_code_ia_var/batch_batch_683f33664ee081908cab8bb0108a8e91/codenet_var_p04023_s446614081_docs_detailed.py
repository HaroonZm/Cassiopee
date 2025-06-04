import bisect
import sys

def read_input():
    """
    Reads the first line containing two integers, N and Q.
    Also reads the following Q lines, each containing a single integer query.
    Returns N and a list of queries.
    """
    input_func = sys.stdin.readline

    N, Q = map(int, input_func().split())
    queries = [int(input_func()) for _ in range(Q)]
    return N, queries

def prepare_query_list(N, queries):
    """
    Creates a list of query tuples, each is (query_value, query_index).
    The first tuple is (N, 0), followed by the user queries.
    The list is then sorted in reverse order by query_value.
    """
    que = [(N, 0)]
    for i, q in enumerate(queries):
        que.append((q, i + 1))
    que.sort(reverse=True)
    return que

def build_ext(que):
    """
    Processes sorted query list to build the ext list.
    This collapses consecutive repeated values with increasing IDs,
    and removes duplicates according to specific rules by processing from smallest to largest.
    """
    ext = []
    while que:
        q, idx = que.pop()
        if not ext:
            ext.append((q, idx))
        else:
            if ext[-1][1] < idx:
                if ext[-1][0] == q:
                    ext.pop()
                ext.append((q, idx))
    return ext

def build_edge_and_data(ext):
    """
    Constructs the edge structure for the dynamic programming (DP) traversal,
    and precomputes data for each unique query (`data`).
    edge[i]: list of (index, count) pairs representing transitions.
    data[i]: stores the remainder after recursive divisions.
    """
    Q = len(ext)
    data = [1] * Q
    edge = [[] for _ in range(Q)]
    nowext = [ext[0][0]]
    data[0] = ext[0][0]
    for i in range(1, Q):
        q = ext[i][0]
        rest = q
        while True:
            # Find largest nowext[j] <= rest, using bisect_right
            idx = bisect.bisect_right(nowext, rest)
            if idx == 0:
                break
            else:
                # For the largest nowext[idx-1] <= rest, handle the current remainder
                edge[idx - 1].append((i, rest // nowext[idx - 1]))
                rest = rest % nowext[idx - 1]
        nowext.append(ext[i][0])
        data[i] = rest
    return edge, data

def calc_dp(edge, Q):
    """
    Performs reverse dynamic programming to calculate number of structures (`dp`)
    for each node in the edge tree/graph.
    """
    dp = [1] * Q
    # Traverse from second-to-last to first
    for i in range(Q-2, -1, -1):
        temp = 0
        for nv, c in edge[i]:
            temp += dp[nv] * c
        dp[i] = temp
    return dp

def build_minus_array(ext, data, dp):
    """
    Constructs the 'minus' array which is used for answer adjustment at each step.
    minus[x]: count of structures with remainder == x, weighted by their dp value.
    """
    minus = [0] * (ext[0][0] + 1)
    for i in range(len(ext)):
        minus[data[i]] += dp[i]
    return minus

def main():
    """
    Main function to handle the query computation and output results.
    """
    N, queries = read_input()
    que = prepare_query_list(N, queries)
    ext = build_ext(que)
    Q = len(ext)
    edge, data = build_edge_and_data(ext)
    dp = calc_dp(edge, Q)
    minus = build_minus_array(ext, data, dp)

    base = sum(dp)
    # For each i in 1 to N, print current base after subtracting minus[i-1] if applicable
    for i in range(1, N + 1):
        if i - 1 <= ext[0][0]:
            base -= minus[i - 1]
        print(base)

if __name__ == "__main__":
    main()