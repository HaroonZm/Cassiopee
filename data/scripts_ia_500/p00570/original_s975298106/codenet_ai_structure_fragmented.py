from bisect import bisect

def read_input():
    return map(int, open(0).read().split())

def unpack_input(data):
    N = data[0]
    K = data[1]
    T = data[2:]
    return N, K, T

def compute_gaps(T, N):
    gaps = []
    for i in range(N-1):
        gap = compute_gap(T, i)
        gaps.append(gap)
    return gaps

def compute_gap(T, i):
    return (T[i+1] - T[i]) - 1

def sort_gaps_desc(gaps):
    return sorted(gaps, reverse=True)

def sum_top_gaps(gaps, K):
    return sum(gaps[:K-1])

def compute_total_length(T):
    return T[-1] - T[0] + 1

def main():
    data = list(read_input())
    N, K, T = unpack_input(data)
    gaps = compute_gaps(T, N)
    gaps_sorted = sort_gaps_desc(gaps)
    total_length = compute_total_length(T)
    subtract_sum = sum_top_gaps(gaps_sorted, K)
    result = total_length - subtract_sum
    print(result)

main()