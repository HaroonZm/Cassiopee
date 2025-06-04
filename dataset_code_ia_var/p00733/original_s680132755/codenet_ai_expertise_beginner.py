import sys

def main():
    def parse(S):
        S = S + "$"
        cur = [0]
        mp = {"01": 0}
        sp = {"01": set([0])}
        sv = {"01": (0, 1)}
        lbl = [1]

        def comp(left, right):
            lcs, lb = left
            rcs, rb = right
            a0, b0 = sv[lb]
            a1, b1 = sv[rb]
            if a1 * b0 != a0 * b1:
                return a1 * b0 - a0 * b1
            if lcs is None and rcs is None:
                return 0
            ll, lr = lcs
            rl, rr = rcs
            cl = comp(ll, rl)
            if cl != 0:
                return cl
            cr = comp(lr, rr)
            if cr != 0:
                return cr
            return 0

        def expr():
            if S[cur[0]] == "x":
                cur[0] += 1
                return (None, "01")
            cur[0] += 1 # "("
            left = expr()
            cur[0] += 1 # " "
            right = expr()
            cur[0] += 1 # ")"
            lb = left[1]
            rb = right[1]
            if lb < rb:
                eb = "0{}{}1".format(lb, rb)
            else:
                eb = "0{}{}1".format(rb, lb)
            if eb not in mp:
                mp[eb] = lbl[0]
                sp[eb] = sp[lb] | sp[rb] | set([lbl[0]])
                sv[eb] = (len(sp[lb] & sp[rb]), len(sp[lb] | sp[rb]))
                lbl[0] += 1
            if comp(left, right) < 0:
                left, right = right, left
            return ((left, right), eb)
        return expr()

    def dfs(root, m):
        if root[0] is None:
            return "x"
        left, right = root[0]
        if m == 0:
            return "(" + dfs(left, 0) + " " + dfs(right, 1) + ")"
        else:
            return "(" + dfs(right, 0) + " " + dfs(left, 1) + ")"

    try:
        while True:
            S = sys.stdin.readline()
            if not S:
                break
            S = S.strip()
            if S == "0":
                break
            result = parse(S)
            out = dfs(result, 0)
            print(out)
    except Exception:
        pass

if __name__ == "__main__":
    main()