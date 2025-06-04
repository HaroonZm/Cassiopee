class Movement:
    U = 'U'
    D = 'D'
    L = 'L'
    R = 'R'

    @staticmethod
    def delta(move):
        return {
            Movement.U: (0, 1),
            Movement.D: (0, -1),
            Movement.L: (-1, 0),
            Movement.R: (1, 0),
        }[move]

class Magic:
    FLIP_VERTICAL = 1
    FLIP_HORIZONTAL = 2

class MagicState:
    def __init__(self, flip_vertical=False, flip_horizontal=False):
        self.flip_vertical = flip_vertical
        self.flip_horizontal = flip_horizontal

    def toggle(self, magic_type):
        if magic_type == Magic.FLIP_VERTICAL:
            self.flip_vertical = not self.flip_vertical
        elif magic_type == Magic.FLIP_HORIZONTAL:
            self.flip_horizontal = not self.flip_horizontal

    def copy(self):
        return MagicState(self.flip_vertical, self.flip_horizontal)

    def apply(self, move):
        if self.flip_vertical:
            if move == Movement.U:
                move = Movement.D
            elif move == Movement.D:
                move = Movement.U
        if self.flip_horizontal:
            if move == Movement.L:
                move = Movement.R
            elif move == Movement.R:
                move = Movement.L
        return move

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_by(self, move):
        dx, dy = Movement.delta(move)
        self.x += dx
        self.y += dy

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

class State:
    def __init__(self, idx, used_magic, magic_state, position):
        self.idx = idx  # current index in string
        self.used_magic = used_magic  # total magic used
        self.magic_state = magic_state  # current magic state
        self.position = position  # Position object

    def key(self):
        return (self.idx,
                self.used_magic,
                self.magic_state.flip_vertical,
                self.magic_state.flip_horizontal)

class Solution:
    def __init__(self, S, K):
        self.S = S
        self.K = K
        # For DP: key = (idx, used_magic, flipV, flipH), value = (x,y)
        self.dp = {}

    def solve(self):
        # Initialize dp with position at origin and no magic used or flips
        start_state = State(
            idx=0,
            used_magic=0,
            magic_state=MagicState(False, False),
            position=Position(0, 0)
        )
        self.dp[start_state.key()] = (0, 0)  # coordinates of position

        for i in range(len(self.S)):
            next_dp = {}
            char = self.S[i]
            for (idx, used_magic, flipV, flipH), (x, y) in self.dp.items():
                # current magic state
                magic_state = MagicState(flipV, flipH)

                # Option 0: no new magic
                new_move = magic_state.apply(char)
                dx, dy = Movement.delta(new_move)
                pos_x = x + dx
                pos_y = y + dy
                key0 = (i+1, used_magic, flipV, flipH)
                if key0 not in next_dp or abs(pos_x) + abs(pos_y) > abs(next_dp[key0][0]) + abs(next_dp[key0][1]):
                    next_dp[key0] = (pos_x, pos_y)

                # Option 1: use magic 1 before reading char
                # Flip vertical flips
                if used_magic < self.K:
                    new_magic_state = magic_state.copy()
                    new_magic_state.toggle(Magic.FLIP_VERTICAL)
                    new_move = new_magic_state.apply(char)
                    dx, dy = Movement.delta(new_move)
                    pos_x = x + dx
                    pos_y = y + dy
                    key1 = (i+1, used_magic + 1, new_magic_state.flip_vertical, new_magic_state.flip_horizontal)
                    if key1 not in next_dp or abs(pos_x)+abs(pos_y) > abs(next_dp[key1][0]) + abs(next_dp[key1][1]):
                        next_dp[key1] = (pos_x, pos_y)

                # Option 2: use magic 2 before reading char
                if used_magic < self.K:
                    new_magic_state = magic_state.copy()
                    new_magic_state.toggle(Magic.FLIP_HORIZONTAL)
                    new_move = new_magic_state.apply(char)
                    dx, dy = Movement.delta(new_move)
                    pos_x = x + dx
                    pos_y = y + dy
                    key2 = (i+1, used_magic + 1, new_magic_state.flip_vertical, new_magic_state.flip_horizontal)
                    if key2 not in next_dp or abs(pos_x)+abs(pos_y) > abs(next_dp[key2][0]) + abs(next_dp[key2][1]):
                        next_dp[key2] = (pos_x, pos_y)

                # Option 3: use both magics before reading char (2 magic uses)
                if used_magic + 1 < self.K:
                    new_magic_state = magic_state.copy()
                    new_magic_state.toggle(Magic.FLIP_VERTICAL)
                    new_magic_state.toggle(Magic.FLIP_HORIZONTAL)
                    new_move = new_magic_state.apply(char)
                    dx, dy = Movement.delta(new_move)
                    pos_x = x + dx
                    pos_y = y + dy
                    key3 = (i+1, used_magic + 2, new_magic_state.flip_vertical, new_magic_state.flip_horizontal)
                    if key3 not in next_dp or abs(pos_x)+abs(pos_y) > abs(next_dp[key3][0]) + abs(next_dp[key3][1]):
                        next_dp[key3] = (pos_x, pos_y)

            self.dp = next_dp

        # Find max manhattan distance in all dp states at end
        max_dist = 0
        for _, (x, y) in self.dp.items():
            dist = abs(x)+abs(y)
            if dist > max_dist:
                max_dist = dist
        return max_dist

def main():
    import sys
    S = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    solution = Solution(S, K)
    print(solution.solve())

if __name__ == '__main__':
    main()