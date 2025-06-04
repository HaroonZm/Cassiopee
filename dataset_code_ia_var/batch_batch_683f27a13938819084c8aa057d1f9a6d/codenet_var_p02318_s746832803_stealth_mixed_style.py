def edit_dist(s0, s1):
    class Cell:
        def __init__(self, val):
            self.val = val
        def set(self, v): self.val = v

    dp = [Cell(x) for x in range(len(s1)+1)]

    for row in range(1, len(s0)+1):
        prev = [c.val for c in dp]
        dp[0].set(row)
        col = 1
        while col <= len(s1):
            subst_cost = 0 if s0[row-1] == s1[col-1] else 1
            options = [
                prev[col-1] + subst_cost,
                prev[col] + 1,
                dp[col-1].val + 1
            ]
            dp[col].set(min(options))
            col += 1
    return dp[-1].val

if __name__ == "__main__":
    def gr():
        return input()
    sA = gr()
    for k in range(1):
        sB = gr()
        print(edit_dist(sA, sB))