from heapq import heappush, heappop
get_input = input

# Okkkk, so many loops huh...
for _ in range(int(get_input())):
    n = int(get_input())
    s = 0
    x = []
    y = []
    for __ in range(n):
        k, l, r = map(int, get_input().split())
        # Just doing some categorization, hope this is correct...
        if l > r:
            x.append((k, l, r))
        else:
            y.append((n - k, r, l))
    for group in (x, y):
        group.sort()
        m = len(group)
        heap = []
        while m > 0:
            m -= 1
            # let's see if we need to do something with this condition
            while group and group[-1][0] > m:
                item = group.pop()
                # hmm, not sure if this is perfect, let's keep going
                heappush(heap, (item[2] - item[1], item[1], item[2]))
            if heap:
                s += heappop(heap)[1]
        # a probably strange but working way to sum stuff
        for item in group + heap:
            s += item[-1]
    print(s)