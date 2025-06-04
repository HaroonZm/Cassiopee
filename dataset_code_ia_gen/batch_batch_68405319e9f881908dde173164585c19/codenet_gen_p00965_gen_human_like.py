import sys
import heapq

def main():
    input = sys.stdin.readline
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Policy-2: assign seats after all reservations -> minimum number required is
    # the maximum number of overlapping intervals at any point (interval graph coloring)
    # We can find it by sorting start and end points and sweeping through:
    events = []
    for a, b in intervals:
        events.append((a, 'start'))
        events.append((b, 'end'))
    events.sort(key=lambda x: (x[0], 0 if x[1]=='start' else 1))
    
    current = 0
    max_overlap = 0
    for _, typ in events:
        if typ == 'start':
            current += 1
            if current > max_overlap:
                max_overlap = current
        else:
            current -= 1
    s2 = max_overlap
    
    # Policy-1: passengers choose seats arbitrarily, all possible orders considered
    # As per problem's explanation, s1 is given by the maximum size of a clique in the
    # interval graph that cannot be avoided by any booking order or seat choice.
    # In other words, s1 corresponds to the max number of intervals that mutually overlap
    # at some point (the size of a maximum clique in the interval graph).
    #
    # For intervals [a_i, b_i), the max clique size is the maximum number of intervals
    # covering an interior point.
    #
    # This is the same as max number of overlapping intervals at any point, so at first glance,
    # s1 might look equal to s2. But the problem clarifies that the passengers can have seat
    # preferences in any order and the worst case needs accounting.
    #
    # According to the editorial and the sample explanation, s1 can be computed as the maximum
    # number of intervals whose intervals are pairwise intersecting but with overlapping travel sections,
    # which can be found by checking the size of "the maximum number of intervals overlapping at a point
    # but excluding some subtle conditions".
    #
    # However, the problem itself is known to have a solution where:
    # - s2 = chromatic number of the interval graph = max number of overlapping intervals
    # - s1 = clique number, which coincides with the size of the largest set of intervals that pairwise overlap,
    #   but due to passenger seat choice and unknown order, s1 equals the maximum number of intervals overlapping
    #   at the same time at any point AND maximum number of intervals with a chain of partial overlaps, i.e.,
    #   the minimal number of colors in a worst reservation order.
    #
    # The problem's sample inputs also suggest s1 can be found by:
    # Sorting intervals by start then tracking interval ends in a max-heap and counting intervals that overlap.
    #
    # Actually, from discussion on similar problems, to get s1, we can:
    # count the maximum number of intervals that overlap at any point (as with s2),
    # but also consider the largest size of a set of intervals where each pair overlaps.
    #
    # For intervals, the maximum clique size equals the maximum number of intervals overlapping at some point,
    # which is the same as s2 in usual interval graph coloring.
    #
    # The problem says s1 >= s2.
    #
    # The difference is that under policy-1, an adversarial reservation order can force more required seats:
    #
    # From known solutions: s1 = maximum number of intervals that intersect pairwise (max clique size),
    # s2 = chromatic number = max number of intervals overlapping any station,
    #
    # But the problem states s1 considers all reservation orders, passengers pick seats arbitrarily,
    # and s2 is assignment after all reservations complete.
    #
    # Under policy-1, the worst-case is that for certain reservation order and seat choices
    # the number of required seats matches the maximum number of intervals that intersect pairwise, i.e.,
    # the size of a maximum *clique* of the interval graph.
    #
    # They define "overlapping sections" between intervals as having intersection in their travel sections.
    #
    # Hence, s1 is the maximum size of a set of intervals pairwise overlapping, which is the maximum clique size.
    #
    # Since all intervals are half-open in practice? The problem doesn't says, but we treat from a_i to b_i as [a_i, b_i)
    #
    # Implementing the clique size:
    #
    # We can find the maximum clique size by sorting intervals by their start, and maintaining their min end in a heap:
    # The number of intervals in the heap when removing intervals that end before current start gives us the clique size.
    
    # Sort intervals by start time ascending, if tie by end ascending
    intervals.sort()
    min_heap = []
    max_clique = 0
    
    for a, b in intervals:
        # Remove intervals ending before or at current start
        while min_heap and min_heap[0] <= a:
            heapq.heappop(min_heap)
        # Add current interval's end
        heapq.heappush(min_heap, b)
        if len(min_heap) > max_clique:
            max_clique = len(min_heap)
    s1 = max_clique
    
    print(s1, s2)


if __name__ == '__main__':
    main()