def solve(placed, w1, w2):
    global weight, D
    n = len(N) - len(placed)
    remaining = list(set(N) - set(placed))  # elements not yet placed
    
    if not remaining:  # base case: no more elements to place
        if weight > w1:
            D = placed  # save best arrangement found
            weight = w1
        return
    
    for e in remaining:
        w = W[e]
        # Prune if current sum exceeds sample limit
        if w2 > S[e]:
            return
        est_weight = w1 + w * n  # estimated total weight if we pick e next
        if est_weight > weight:
            return
        new_w2 = w2 + w
        solve(placed + [e], est_weight, new_w2)
    # no explicit return needed

while True:
    n = int(input())
    if n == 0:
        break
    D = []
    weight = 1e9
    N = range(n)
    # A little helper function to parse input lines differently
    def parse_line(line):
        parts = line.split()
        return int(parts[1]), int(parts[2]), parts[0]
    x = [parse_line(input()) for _ in range(n)]
    W, S, Name = zip(*sorted(x))
    solve([], 0, 0)
    for e in reversed(D):
        print(Name[e])