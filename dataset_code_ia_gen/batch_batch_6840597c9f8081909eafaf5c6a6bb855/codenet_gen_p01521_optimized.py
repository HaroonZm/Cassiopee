def solve():
    s = input()
    n = len(s)
    memo = {}

    def flip(s, i, c):
        # Flip opponent's pieces starting from i towards s[i]
        arr = list(s)
        arr[i] = c
        left = i - 1
        right = i + 1
        # Flip left side
        while left >= 0 and arr[left] != c and arr[left] != '.':
            arr[left] = c
            left -= 1
        # Flip right side
        while right < len(arr) and arr[right] != c and arr[right] != '.':
            arr[right] = c
            right += 1
        return ''.join(arr)

    def can_put(s, c, i):
        if s[i] != '.':
            return False
        left = i - 1
        right = i + 1
        # Adjacent opponent piece?
        opp = 'o' if c == 'x' else 'x'
        if (left >= 0 and s[left] == opp) or (right < n and s[right] == opp):
            return True
        return False

    def moves(s, c):
        return [i for i in range(n) if can_put(s, c, i)]

    def score(s):
        return s.count('o'), s.count('x')

    def dfs(s, c):
        if (s, c) in memo:
            return memo[(s, c)]
        opp = 'o' if c == 'x' else 'x'
        mv = moves(s, c)
        if not mv:
            opp_mv = moves(s, opp)
            if not opp_mv:
                # Game over, return who wins
                o_count, x_count = score(s)
                if o_count > x_count:
                    memo[(s, c)] = 1 if c == 'o' else -1
                else:
                    memo[(s, c)] = 1 if c == 'x' else -1
                return memo[(s, c)]
            else:
                # Pass
                res = dfs(s, opp)
                memo[(s, c)] = -res
                return -res
        results = []
        for i in mv:
            ns = flip(s, i, c)
            res = dfs(ns, opp)
            results.append(-res)
        memo[(s, c)] = max(results)
        return memo[(s, c)]

    # Initial board: given pieces at left, rest empty at right up to N
    # Actually, the given string is initial full position; no empty cells.
    # But the problem statement says infinite board; in practice, only given pieces matter.
    # We can consider empty cells represented by '.' outside given pieces? Actually no.
    # The problem is the given initial pieces connected and no empty positions.
    # The only possible moves are to put at ends if adjacent piece of opponent.
    # So we represent empty cells at ends explicitly.
    # Let's represent board as list with '.' for empty outside given pieces.

    # We'll pad the board with '.' at both ends to allow adding pieces at ends.
    board = '.' + s + '.'

    # Adjust flipping and moves to handle this
    s = board
    n = len(s)

    def flip(s, i, c):
        arr = list(s)
        arr[i] = c
        opp = 'o' if c == 'x' else 'x'
        # Flip left
        left = i - 1
        while left >= 0 and arr[left] == opp:
            arr[left] = c
            left -= 1
        # Flip right
        right = i + 1
        while right < len(arr) and arr[right] == opp:
            arr[right] = c
            right += 1
        return ''.join(arr)

    def can_put(s, c, i):
        if s[i] != '.':
            return False
        opp = 'o' if c == 'x' else 'x'
        if (i > 0 and s[i-1] == opp) or (i+1 < len(s) and s[i+1] == opp):
            return True
        return False

    def moves(s, c):
        return [i for i in range(len(s)) if can_put(s, c, i)]

    def score(s):
        o_count = s.count('o')
        x_count = s.count('x')
        return o_count, x_count

    memo = {}
    res = dfs(s, 'o')
    print('o' if res == 1 else 'x')