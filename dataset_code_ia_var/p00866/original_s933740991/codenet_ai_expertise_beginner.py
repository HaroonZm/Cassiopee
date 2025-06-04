import itertools

def convert(v):
    h = v // 3600
    m = (v // 60) % 60
    s = v % 60
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

BASE = 12 * 3600

while True:
    N = int(input())
    if N == 0:
        break

    all_times = set()
    watches_times = []

    for _ in range(N):
        nums = list(map(int, input().split()))
        possible_times = set()
        for perm in itertools.permutations(nums, 3):
            a, b, c = perm
            for add in range(60):
                h = (a + add) % 60
                m = (b + add) % 60
                s = (c + add) % 60
                # minute hand at multiple of 12 matches hour hand
                if m // 12 == h % 5:
                    val = 3600 * (h // 5) + 60 * m + s
                    possible_times.add(val)
                    all_times.add(val)
        watches_times.append(sorted(possible_times))

    all_times = sorted(all_times)
    best_diff = 13 * 3600
    best_start = 0
    best_end = 0

    counters = [0] * N

    for t in all_times:
        current = t
        for i in range(N):
            ptr = counters[i]
            w_times = watches_times[i]
            size = len(w_times)
            while ptr < size and w_times[ptr] < t:
                ptr += 1
            counters[i] = ptr
            if ptr == size:
                current = max(current, BASE + w_times[0])
            else:
                current = max(current, w_times[ptr])
        if current - t < best_diff:
            best_diff = current - t
            best_start = t % BASE
            best_end = current % BASE

    print(convert(best_start), convert(best_end))