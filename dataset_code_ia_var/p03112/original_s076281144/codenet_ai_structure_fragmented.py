import bisect

def read_ints():
    return map(int, raw_input().split())

def read_single_int():
    return int(raw_input())

def read_list(n):
    return [read_single_int() for _ in xrange(n)]

def add_infinities(lst, inf):
    return [-inf] + lst + [inf]

def sort_list(lst):
    lst.sort()
    return lst

def prepare_input():
    a, b, q = read_ints()
    inf = 2 << 60
    s = read_list(a)
    t = read_list(b)
    queries = [read_single_int() for _ in xrange(q)]
    return s, t, queries, inf

def process_infinities_and_sort(s, t, inf):
    s = add_infinities(s, inf)
    t = add_infinities(t, inf)
    s = sort_list(s)
    t = sort_list(t)
    return s, t

def get_candidates(lst, x):
    idx = bisect.bisect(lst, x)
    return [lst[idx-1], lst[idx]]

def compute_distances(x, ss, tt):
    d1 = abs(ss - x) + abs(tt - ss)
    d2 = abs(tt - x) + abs(ss - tt)
    return [d1, d2]

def find_min_distance(s, t, x, inf):
    scands = get_candidates(s, x)
    tcands = get_candidates(t, x)
    res = inf
    for ss in scands:
        for tt in tcands:
            dists = compute_distances(x, ss, tt)
            res = min(res, dists[0], dists[1])
    return res

def process_queries(s, t, queries, inf):
    results = []
    for x in queries:
        res = find_min_distance(s, t, x, inf)
        results.append(res)
    return results

def print_results(results):
    for r in results:
        print r

def main():
    s, t, queries, inf = prepare_input()
    s, t = process_infinities_and_sort(s, t, inf)
    results = process_queries(s, t, queries, inf)
    print_results(results)

main()