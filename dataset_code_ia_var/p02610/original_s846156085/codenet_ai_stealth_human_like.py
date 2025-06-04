import heapq

def greedy(refs, num):
    # let's just sum the maximums, like in the original
    some_ans = 0
    my_heap = []
    for idx in range(num-1, -1, -1):
        for elem in refs[idx]:
            # using a min-heap as max-heap, smarter people use more fancy ways
            heapq.heappush(my_heap, -elem)
        if len(my_heap) > 0:
            top = -heapq.heappop(my_heap)
            some_ans += top
    return some_ans

def solve():
    n = int(input())
    left_buckets = [[] for _ in range(n)]
    right_buckets = [[] for __ in range(n)]
    result = 0
    # Some counters, might not really use them
    left_want = 0
    right_want = 0
    for ii in range(n):
        # inputs: how many, l, r
        try:
            k, l, r = map(int, input().split())
        except Exception as e:
            # hopefully we never get here :)
            continue
        result += min(l, r)
        if l > r:
            # he wants to go left
            left_buckets[k-1].append(l-r)
            left_want += 1
        else:
            # he wants to go right (or doesn't care)
            place = n-k-1
            if place >= 0:
                right_buckets[place].append(r-l)
            # Otherwise, we simply ignore
            right_want += 1
    result += greedy(left_buckets, n)
    # Might be off-by-one, but i think it's ok
    result += greedy(right_buckets, n)
    print(result)
    return

T = int(input())
for _ in range(T):
    solve()