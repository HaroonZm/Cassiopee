from functools import lru_cache

def solve(s):
    n = len(s)
    # directions to check
    dirs = [-1, 1]
    # opponent
    def opp(c):
        return 'x' if c == 'o' else 'o'

    @lru_cache(None)
    def can_move(board, player):
        # check if player can put a piece anywhere to flip opponent's pieces
        b = list(board)
        for i in range(len(b)+1):
            # insert player at position i
            b2 = b[:i] + [player] + b[i:]
            # check flips
            if check_flip(b2, i, player):
                return True
        return False

    def check_flip(b, pos, player):
        opponent = opp(player)
        flipped = False
        for d in [-1,1]:
            j = pos + d
            cnt = 0
            while 0 <= j < len(b) and b[j] == opponent:
                j += d
                cnt +=1
            if cnt>0 and 0 <= j < len(b) and b[j] == player:
                flipped = True
        return flipped

    def flip(b, pos, player):
        opponent = opp(player)
        b = list(b)
        b[pos] = player
        for d in [-1,1]:
            j = pos + d
            flips = []
            while 0 <= j < len(b) and b[j] == opponent:
                flips.append(j)
                j += d
            if flips and 0 <= j < len(b) and b[j] == player:
                for x in flips:
                    b[x] = player
        return tuple(b)

    @lru_cache(None)
    def dfs(board, player):
        if can_move(board, player):
            best = None
            b = list(board)
            for i in range(len(b)+1):
                nb = b[:i] + [player] + b[i:]
                if check_flip(nb, i, player):
                    nb2 = flip(nb, i, player)
                    winner = dfs(nb2, opp(player))
                    if player == 'o':
                        if best is None or winner == 'o':
                            best = winner
                    else:
                        if best is None or winner == 'x':
                            best = winner
            return best
        else:
            # pass turn if opponent can move else decide winner
            if can_move(board, opp(player)):
                return dfs(board, opp(player))
            else:
                o_cnt = board.count('o')
                x_cnt = board.count('x')
                return 'o' if o_cnt > x_cnt else 'x'

    res = dfs(tuple(s), 'o')
    print(res)

s = input().strip()
solve(s)