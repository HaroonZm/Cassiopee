def count_gochiusa_numbers(N):
    s = str(N)
    length = len(s)
    pattern = ['5', '1', None, '3']

    from functools import lru_cache

    @lru_cache(None)
    def dfs(pos, prefix_equal, state):
        # state: how many characters of "51?3" matched so far
        # 0: no match yet, 1: matched '5', 2: matched '51', 3: matched '51?' (any digit), 4: matched "51?3"
        if pos == length:
            return 1 if state == 4 else 0
        limit = int(s[pos]) if prefix_equal else 9
        res = 0
        for d in range(limit + 1):
            # next prefix_equal
            next_prefix_equal = prefix_equal and (d == limit)
            c = str(d)
            next_state = state
            if state == 0:
                if c == '5':
                    next_state = 1
                else:
                    next_state = 0
            elif state == 1:
                if c == '1':
                    next_state = 2
                elif c == '5':
                    next_state = 1
                else:
                    next_state = 0
            elif state == 2:
                # '?' can be any digit
                next_state = 3
            elif state == 3:
                if c == '3':
                    next_state = 4
                elif c == '5':
                    next_state = 1
                else:
                    next_state = 0
            else:  # state == 4 means already matched, stay 4
                next_state = 4
            res += dfs(pos + 1, next_prefix_equal, next_state)
        return res

    return dfs(0, True, 0)

N = int(input())
print(count_gochiusa_numbers(N))