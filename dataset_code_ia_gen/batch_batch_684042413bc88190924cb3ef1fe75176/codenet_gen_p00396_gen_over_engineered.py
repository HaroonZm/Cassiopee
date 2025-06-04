class StoneGameState:
    def __init__(self, white: int, black: int):
        if white < 1 or black < 1:
            raise ValueError("Each area must start with at least one white and one black stone")
        self.white = white
        self.black = black

    def grundy(self) -> int:
        # Computing mex of all reachable states:
        # moves:
        # (a) remove one white stone: (w-1, b) if w > 1
        # (b) remove 1 to white stones number of black stones <= w:
        #     for x in [1..b_min], remove x black stones if x <= w
        #     but number of removed black stones <= white stones currently there
        # (c) replace one white stone from pod with one black stone:
        #     (w, b) -> (w, b) but white decreases by 1 and black increases by 1? No,
        #     Problem states pick up a white stone from pod and replace it with black stone.
        #     So white stones does not decrease (pod is infinite), but white in area increases by 0? No,
        #     The "replace" means in the area, a white stone is replaced by a black stone:
        #     So (w,b)-> (w-1, b+1), w>=1
        #     Wait: Actually, it's picking white from *pod* and replace it in the area with black.
        #     So the operation adds one black stone and removes one white stone in the area.
        # Thus move (c) transforms (w,b) -> (w-1, b+1) if w>0
        #
        # Let's re-verify problem statement:
        # "(c) Pick up a white stone from the stone pod and replace it with a black stone."
        # The pod has infinite white stones.
        # The replacement is in the area.
        # So in the area: a white stone is converted to a black stone, number of white stones decreases by 1,
        # black stones increases by 1.
        #
        # Summary:
        # (a) (w,b) -> (w-1,b)  if w>1
        # (b) (w,b) -> (w,b - x) for 1 <= x <= min(b,w)
        # (c) (w,b) -> (w-1,b+1) if w > 0
        #
        # But from problem constraints: w >=1 etc.
        #
        # Now to implement grundy function with memoization to avoid recomputation.

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(w: int, b: int):
            if w == 0:
                # no white stones: no moves possible (rules require at least one white stone)
                # So no moves, losing position
                return 0

            reachable = set()

            # (a)
            if w - 1 >= 1:
                reachable.add(dfs(w - 1, b))

            # (b)
            max_black_remove = min(b, w)
            for x in range(1, max_black_remove + 1):
                reachable.add(dfs(w, b - x))

            # (c)
            # can only do if at least 1 white stone to replace, which is guaranteed since w>=1
            if w - 1 >= 0:
                reachable.add(dfs(w - 1, b + 1))

            # mex calculation
            g = 0
            while g in reachable:
                g += 1
            return g

        return dfs(self.white, self.black)


class StoneGame:
    def __init__(self):
        self.areas = []

    def add_area(self, white: int, black: int):
        self.areas.append(StoneGameState(white, black))

    def winner(self) -> int:
        # XOR grundy numbers of all areas
        nim_sum = 0
        for area in self.areas:
            g = area.grundy()
            nim_sum ^= g
        # 0 means first player (Koshiro) has winning strategy
        # 1 means second player (Ukiko) wins
        return 0 if nim_sum != 0 else 1


def main():
    import sys

    game = StoneGame()
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        w, b = map(int, input().split())
        game.add_area(w, b)
    print(game.winner())


if __name__ == "__main__":
    main()