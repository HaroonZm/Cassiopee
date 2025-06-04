from collections import deque

# Directions for movement: stay, up, down, left, right
DIRECTIONS = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

def solve():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        palace = [list(input()) for _ in range(H)]

        # Find positions of Queen(Q), Army(A), and store Exits(E)
        qx = qy = ax = ay = -1
        exits = []
        for y in range(H):
            for x in range(W):
                if palace[y][x] == 'Q':
                    qx, qy = x, y
                    palace[y][x] = '.'  # treat as floor for movement
                elif palace[y][x] == 'A':
                    ax, ay = x, y
                    palace[y][x] = '.'  # treat as floor
                elif palace[y][x] == 'E':
                    exits.append((x,y))
                    # keep as 'E'

        # Precompute if a cell is accessible (not wall)
        def passable(x,y):
            return 0 <= x < W and 0 <= y < H and palace[y][x] != '#'

        # State representation:
        # (queen_x, queen_y, army_x, army_y, turn)
        # turn = 0 means queen's turn, 1 means army's turn
        # We will use a bottom-up dynamic programming approach on state space to decide outcome.
        # Outcomes per state:
        # 0 = unknown
        # 1 = queen can escape from this state (queen wins)
        # 2 = army can catch queen (army wins)
        # 3 = draw (neither can force a win)
        #
        # We'll perform retrograde analysis (backward solving) starting from terminal states:
        #
        # Terminal states for queen win:
        # After army's turn (turn=1), queen is alone on an exit cell.
        # Terminal states for army win:
        # queen and army are on the same cell, queen caught immediately.

        # Total states at most: W*H*W*H*2 ~ 540000, manageable.

        # outcome[state] stores the result for the state
        # outdegree[state] stores how many next moves can be reached from state,
        # used for detecting losing positions by standard game graph search.

        from enum import IntEnum
        class Outcome(IntEnum):
            UNKNOWN = 0
            QUEEN_WIN = 1
            ARMY_WIN = 2
            DRAW = 3

        # Helper functions to map states to indices can be avoided by using dictionaries,
        # but we use a 5D array for speed
        # We will keep:
        # dp[qy][qx][ay][ax][turn] = outcome

        dp = [[[[[Outcome.UNKNOWN for _ in range(2)] for _ in range(W)] for _ in range(H)] for _ in range(W)] for _ in range(H)]
        outdegree = [[[[[0 for _ in range(2)] for _ in range(W)] for _ in range(H)] for _ in range(W)] for _ in range(H)]

        # Compute all possible moves for queen and army
        def next_positions(x,y):
            positions = []
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if passable(nx,ny):
                    positions.append((nx,ny))
            return positions

        # Precompute possible moves for each cell to speed up
        queen_moves = [[next_positions(x,y) for x in range(W)] for y in range(H)]
        army_moves = queen_moves  # same movement rules

        # Count outdegrees for all states
        for qy_ in range(H):
            for qx_ in range(W):
                if not passable(qx_, qy_):  # queen cannot stand on wall
                    continue
                for ay_ in range(H):
                    for ax_ in range(W):
                        if not passable(ax_, ay_):  # same for army
                            continue
                        for turn in range(2):
                            # If catching condition
                            if qx_ == ax_ and qy_ == ay_:
                                # Army caught queen, immediate army win
                                dp[qy_][qx_][ay_][ax_][turn] = Outcome.ARMY_WIN
                                outdegree[qy_][qx_][ay_][ax_][turn] = 0
                                continue
                            # If queen is alone on exit cell after army's turn (turn=1), queen escapes:
                            # queen alone means queen pos != army pos,
                            # but we've already checked same cell case above
                            if turn==1 and palace[qy_][qx_] == 'E':
                                # queen escaped
                                dp[qy_][qx_][ay_][ax_][turn] = Outcome.QUEEN_WIN
                                outdegree[qy_][qx_][ay_][ax_][turn] = 0
                                continue
                            # Otherwise count how many next states
                            if turn == 0:
                                # queen moves next
                                moves = queen_moves[qy_][qx_]
                                total = 0
                                for nx, ny in moves:
                                    # army stays pos for now, next turn army moves
                                    total +=1
                                outdegree[qy_][qx_][ay_][ax_][turn] = total
                            else:
                                # army moves next
                                moves = army_moves[ay_][ax_]
                                total = 0
                                for nx, ny in moves:
                                    # queen pos unchanged (since queen moved last turn)
                                    total += 1
                                outdegree[qy_][qx_][ay_][ax_][turn] = total

        # We'll use a queue for retrograde analysis:
        # Initialize queue with all known terminal states (queue of states with known outcome)
        queue = deque()
        for qy_ in range(H):
            for qx_ in range(W):
                if not passable(qx_, qy_):
                    continue
                for ay_ in range(H):
                    for ax_ in range(W):
                        if not passable(ax_, ay_):
                            continue
                        for turn in range(2):
                            if dp[qy_][qx_][ay_][ax_][turn] != Outcome.UNKNOWN:
                                queue.append((qx_, qy_, ax_, ay_, turn))

        # Reverse moves:
        # For a current state, we find parent states that go to current state in one move, to propagate outcomes.

        # We need:
        # Given a state s = (qx, qy, ax, ay, turn), find all predecessor states p where
        # if turn == 0 (queen moves next), s is after queen moved,
        #     p has turn == 1 (army just moved), and queen was at p.qx p.qy before moving to qx,qy
        # if turn == 1 (army moves next), s is after army moved,
        #     p has turn == 0 (queen just moved), army moved from p.ax p.ay to ax ay.

        # We will propagate using standard game theory rule:

        # If current state is losing for current player, parent state is winning for the opponent.
        # If all child's states are winning for opponent, parent state is losing for current player.

        def predecessors(qx_, qy_, ax_, ay_, turn):
            # turn: 0 means queen's turn:
            # current state is after queen moved,
            # previous state is army's turn with army at ax_, ay_, queen somewhere that leads to qx_,qy_
            #
            # turn: 1 means army's turn:
            # current state is after army moved,
            # previous state is queen's turn with queen at qx_,qy_, army somewhere that leads to ax_, ay_
            preds = []
            if turn == 0:
                # current state is after queen moved
                # previous turn was army's turn = 1
                # queen was in some (px, py) that can move to current (qx_, qy_)
                for px, py in queen_moves[qy_][qx_]:
                    # px,py must have been queen position in prev state
                    # The army position and turn remain as ax_, ay_,1
                    if dp[py][px][ay_][ax_][1] == Outcome.UNKNOWN:
                        preds.append((px, py, ax_, ay_, 1))
            else:
                # current state after army moved
                # previous turn was queen's turn = 0
                # army was in some (pax, pay) that can move to current (ax_, ay_)
                for pax, pay in army_moves[ay_][ax_]:
                    if dp[qy_][qx_][pay][pax][0] == Outcome.UNKNOWN:
                        preds.append((qx_, qy_, pax, pay, 0))
            return preds

        # Implement the retrograde analysis using standard game solve approach
        while queue:
            qx_, qy_, ax_, ay_, turn = queue.popleft()
            cur_result = dp[qy_][qx_][ay_][ax_][turn]

            # Find predecessors states
            for px, py, pax, pay, pturn in predecessors(qx_, qy_, ax_, ay_, turn):
                if dp[py][px][pay][pax][pturn] != Outcome.UNKNOWN:
                    # Already known
                    continue

                # pturn: whose turn to move in predecessor state
                # cur_result is the outcome of the child state (current state)
                # pturn player tries to select move to child states
                #
                # if cur_result is winning for next player (child state),
                # then pturn player can lose if no alternative moves,
                # else pturn player can win by choosing child states losing for opponent

                # If current player at predecessor turn:
                # If cur_result == lose for pturn player => pturn player wants to move to that state to win.
                # -> dp[pred] = pturn player win
                #
                # if all next states are pturn player win (bad for pturn player),
                # dp[pred] = pturn player lose.

                # In our encoding:
                # cur_result tells who wins in the current state (child)
                # We want to determine pturn player's result.

                # pturn player's perspective:
                # If any next state is losing for opponent => winning for pturn player
                # If all next states are winning for opponent => losing for pturn player

                # Map outcome to perspective for pturn player:

                # We consider pturn's winning states:
                # - If pturn = 0 (queen's turn)
                #     -> Queen wants to find a child state which is ARMY_WIN for opponent? No.
                #     - For queen to WIN, the next state should be QUEEN_WIN or DRAW? careful:
                # We can simplify:
                # From pturn player's viewpoint, if child state result == pturn player win, then pturn player wants it.
                # if child state result == opponent win, pturn player wants to avoid it.

                # So if pturn == 0 (queen's turn) and child state result == queen win => good for queen
                # if pturn == 0 and child result == army win => bad for queen
                # if child result is DRAW ? safe for pturn?

                # Simplified approach is:
                # If any next state is losing for next player = winning for current player
                # We'll implement using standard game technique:

                # When current state's child is a losing state for opponent,
                # then predecessor is winning for pturn player.

                # Define function: For pturn player:
                # A state with outcome:
                # Outcome.QUEEN_WIN if queen can force escape
                # Outcome.ARMY_WIN if army can force catch
                # Outcome.DRAW if stalemate

                # Checking if child state is losing for opponent(pturn):
                # If pturn==queen:
                #   child state with ARMY_WIN = opponent win, so child losing for pturn?
                #   child state with QUEEN_WIN = child winning for pturn.
                #   child state DRAW = neutral

                # Thus:
                # For pturn=queen (0), child's ARMY_WIN => losing child
                # For pturn=army (1), child's QUEEN_WIN => losing child

                # If any of successor is losing for pturn, predecessor is winning for pturn.

                lose_for_pturn = False
                if pturn == 0:
                    # queen turn
                    if cur_result == Outcome.ARMY_WIN:
                        lose_for_pturn = True
                else:
                    # army turn
                    if cur_result == Outcome.QUEEN_WIN:
                        lose_for_pturn = True

                if lose_for_pturn:
                    # pturn player can force a winning move here
                    dp[py][px][pay][pax][pturn] = Outcome.QUEEN_WIN if pturn == 0 else Outcome.ARMY_WIN
                    queue.append((px, py, pax, pay, pturn))
                else:
                    # decrease outdegree of pturn player's current state since one child resolved
                    outdegree[py][px][pay][pax][pturn] -= 1
                    if outdegree[py][px][pay][pax][pturn] == 0:
                        # no winning moves left => losing state for pturn player => winning for opponent
                        dp[py][px][pay][pax][pturn] = Outcome.ARMY_WIN if pturn == 0 else Outcome.QUEEN_WIN
                        queue.append((px, py, pax, pay, pturn))

        # After above, states which remain UNKNOWN are draws
        for qy_ in range(H):
            for qx_ in range(W):
                if not passable(qx_, qy_):
                    continue
                for ay_ in range(H):
                    for ax_ in range(W):
                        if not passable(ax_, ay_):
                            continue
                        for turn in range(2):
                            if dp[qy_][qx_][ay_][ax_][turn] == Outcome.UNKNOWN:
                                dp[qy_][qx_][ay_][ax_][turn] = Outcome.DRAW

        # Initial state is queen turn = 0 at queen and army initial positions
        result = dp[qy][qx][ay][ax][0]

        if result == Outcome.QUEEN_WIN:
            print("Queen can escape.")
        elif result == Outcome.ARMY_WIN:
            print("Army can catch Queen.")
        else:
            print("Queen can not escape and Army can not catch Queen.")

if __name__ == "__main__":
    solve()