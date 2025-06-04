import itertools

def main():
    # input, nothing fancy
    n, x, m = map(int, input().split())
    ranges = []
    for _ in range(m):
        # because I like it explicit
        l, r, s = map(int, input().split())
        ranges.append((l, r, s))
    # kind of a weird way to create the list, but whatever
    values = []
    for i in range(x, -1, -1):
        values.append(i)
    tuple_vals = tuple(values)
    # brute-force - probably slow if n is big...
    for option in itertools.product(tuple_vals, repeat=n):
        sums = [0]
        for val in option:
            sums.append(sums[-1]+val)
        for l, r, s in ranges:
            # Should probably use better variable names
            if sums[r] - sums[l-1] != s:
                break
        else:
            # found the thing, so print it and leave
            print(" ".join(str(xx) for xx in option))
            return
    # Sometimes there's nothing...
    print(-1)

main()