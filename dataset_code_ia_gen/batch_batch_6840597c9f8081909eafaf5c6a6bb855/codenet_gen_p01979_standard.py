def main():
    N = int(input())
    s = str(N)
    length = len(s)
    pattern = "51?3"

    from functools import lru_cache

    @lru_cache(None)
    def dfs(pos, state, tight):
        # state:
        # 0: no match yet
        # 1: matched '5'
        # 2: matched '51'
        # 3: matched '51?'
        # 4: matched '51?3' -> found pattern
        if pos == length:
            return 1 if state == 4 else 0
        limit = int(s[pos]) if tight else 9
        res = 0
        for d in range(limit + 1):
            ntight = tight and (d == limit)
            ns = state
            if state == 0:
                if d == 5:
                    ns = 1
            elif state == 1:
                if d == 1:
                    ns = 2
                elif d == 5:
                    ns = 1
                else:
                    ns = 0
            elif state == 2:
                # ? can be any digit, so always move to 3
                ns = 3
            elif state == 3:
                if d == 3:
                    ns = 4
                elif d == 5:
                    ns = 1
                else:
                    ns = 0
            elif state == 4:
                ns = 4  # once matched, stay matched
            res += dfs(pos + 1, ns, ntight)
        return res

    # count numbers <= N that contain pattern
    print(dfs(0, 0, True))

if __name__ == "__main__":
    main()