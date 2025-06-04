import sys
from typing import List, Tuple, Dict, Set

MOD = 10**9 + 9

class GridPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"({self.x},{self.y})"

class ObstructionSet:
    def __init__(self, obstructions: List[Tuple[int,int]]):
        self._set: Set[GridPosition] = set(GridPosition(x,y) for x,y in obstructions)

    def contains(self, pos: GridPosition) -> bool:
        return pos in self._set

class StateIndexer:
    def __init__(self, W: int, obstructions: ObstructionSet):
        # We'll keep track only cells that are not obstructed in one row
        self.W = W
        self.obstructions = obstructions
        self.index_to_pos: List[GridPosition] = []
        self.pos_to_index: Dict[GridPosition, int] = {}

    def update_for_row(self, y: int):
        self.index_to_pos = []
        self.pos_to_index = {}
        for x in range(1, self.W + 1):
            pos = GridPosition(x,y)
            if self.obstructions.contains(pos):
                continue
            idx = len(self.index_to_pos)
            self.index_to_pos.append(pos)
            self.pos_to_index[pos] = idx

    def size(self) -> int:
        return len(self.index_to_pos)

class TransitionMatrix:
    def __init__(self, size: int):
        # Represent matrix as list of lists of int modulo MOD
        self.size = size
        self.mat = [[0]*size for _ in range(size)]

    def __mul__(self, other: 'TransitionMatrix') -> 'TransitionMatrix':
        assert self.size == other.size
        result = TransitionMatrix(self.size)
        for i in range(self.size):
            row_i = self.mat[i]
            for j in range(self.size):
                s = 0
                for k in range(self.size):
                    s += row_i[k] * other.mat[k][j]
                result.mat[i][j] = s % MOD
        return result

    def multiply_vector(self, vec: List[int]) -> List[int]:
        assert self.size == len(vec)
        res = [0]*self.size
        for i in range(self.size):
            s = 0
            row_i = self.mat[i]
            for j in range(self.size):
                s += row_i[j] * vec[j]
            res[i] = s % MOD
        return res

    @staticmethod
    def identity(size: int) -> 'TransitionMatrix':
        m = TransitionMatrix(size)
        for i in range(size):
            m.mat[i][i] = 1
        return m

class MatrixExponentiator:
    @staticmethod
    def pow(mat: TransitionMatrix, exp: int) -> TransitionMatrix:
        # Binary exponentiation
        result = TransitionMatrix.identity(mat.size)
        base = mat
        e = exp
        while e > 0:
            if e & 1:
                result = result * base
            base = base * base
            e >>= 1
        return result

class ThreeWayBranchSolver:
    def __init__(self, W: int, H: int, obstructions: List[Tuple[int,int]]):
        self.W = W
        self.H = H
        self.obstructions = ObstructionSet(obstructions)

    def build_transition(self, y: int, indexer_prev: StateIndexer, indexer_next: StateIndexer) -> TransitionMatrix:
        size_prev = indexer_prev.size()
        size_next = indexer_next.size()
        mat = TransitionMatrix(size_next)

        # For each cell in next row (y+1), find which indices in prev row (y) can reach it
        for idx_next, pos_next in enumerate(indexer_next.index_to_pos):
            x_next = pos_next.x
            candidates_prev_x = [x_next, x_next - 1, x_next + 1]
            for x_prev in candidates_prev_x:
                if 1 <= x_prev <= self.W:
                    pos_prev = GridPosition(x_prev, y)
                    if pos_prev in indexer_prev.pos_to_index:
                        idx_prev = indexer_prev.pos_to_index[pos_prev]
                        # From prev idx to next idx is allowed
                        mat.mat[idx_next][idx_prev] = (mat.mat[idx_next][idx_prev] + 1) % MOD
        return mat

    def solve(self) -> int:
        # We decompose transitions in rows, from y=1 to y=H
        # grid rows go from 1 to H
        # For each row we keep only allowed cells (not obstructed)
        # We'll create transition matrices from row y to y+1 that map states from prev row to next row.

        # We must handle possibly huge H (up to 10^18)
        # The rows with obstructions may block some paths
        # There are at most N=30 obstructions => we can only filter out those cells

        # The key insight: at each step, states = cells in current row (non obstructed)
        # Transitions only depend on next row's allowed cells.
        # So matrix size is number of allowed cells per row (<= W)
        # We compute transition matrix T from row_y to row_y+1: T is size(next_row) x size(prev_row)

        # Because obstructions only appear on certain rows, we can partition rows and handle
        # sequences of unobstructed rows of length L by simply powering matrix for no-obstruction transitions L times.

        # We'll:
        # - Extract all rows with obstructions
        # - Compute sorted list of obstructed rows plus first (1) and last (H)
        # - For each interval between these rows, compute transitions accordingly, and power matrices over L steps

        points_with_obstructions = dict()
        for ox, oy in self.obstructions._set:
            points_with_obstructions.setdefault(oy, [])
            # Already stored in obstruction set; this dictionary is for easier grouping

        # For all y from 1 to H, determine which cells are blocked
        # We manage only rows that appear obstructed or for starting/ending
        # The key rows to consider are 1, all rows with obstructions, and H

        key_rows = set([1, self.H])
        for y in points_with_obstructions.keys():
            key_rows.add(y)
        key_rows = sorted(key_rows)

        # We'll store for each row the indexer of allowed cells in that row
        # plus transition matrices between consecutive rows

        # Memoize indexers row->indexer
        indexers: Dict[int, StateIndexer] = {}
        def indexer_for_row(y: int) -> StateIndexer:
            if y not in indexers:
                idxr = StateIndexer(self.W, self.obstructions)
                idxr.update_for_row(y)
                indexers[y] = idxr
            return indexers[y]

        # Prepare matrices for single step between rows y to y+1:
        # We will need it multiple times for powering

        # Because transitions do not depend on the row number except obstructions,
        # we can cache some base matrices for unobstructed rows.

        # We define function to generate matrix between two consecutive rows
        def transition_matrix(y: int) -> TransitionMatrix:
            idxr_cur = indexer_for_row(y)
            idxr_next = indexer_for_row(y+1)
            return self.build_transition(y, idxr_cur, idxr_next)

        # For any row y, build transition matrix y->y+1 once and store
        # We will need powers of these matrices if intervals are large

        # Because the obstructions may only appear on some rows,
        # rows inside an interval without obstruction have identical transition structure
        # except the rows with obstruction, where available cells differ.

        # We'll process intervals between key_rows:
        # For example between row a and b, all rows in (a,b) do not contain obstruction rows,
        # so for those steps the transition matrix is the same.

        total_ways = None  # vector of ways to reach each cell in current row
        prev_row_num = 1
        # initial ways: only one cell at (1,1)
        idxr_start = indexer_for_row(1)
        ways = [0]*idxr_start.size()
        ways[idxr_start.pos_to_index[GridPosition(1,1)]]=1

        # To facilitate intervals, we need a function to compute transition matrix for a row y
        # and cache it for reuse
        transition_cache: Dict[int, TransitionMatrix] = {}

        def get_transition(y: int) -> TransitionMatrix:
            if y not in transition_cache:
                transition_cache[y] = transition_matrix(y)
            return transition_cache[y]

        # We create a list of all rows from 1 to H partitioned by key_rows:
        # For each segment between key_rows[i] and key_rows[i+1]:
        # - if difference is 1, just perform single step with that y transition
        # - if difference > 1, then do matrix exponentiation of that transition matrix over that number of steps
        # but if there is an obstruction row in between, key_rows includes those rows.

        # Actually key_rows includes only rows with obstructions and endpoints.
        # For intervals between these rows, no obstruction in intermediate rows.

        from bisect import bisect_right

        # Since H can be large, build set of all obstruction rows for checks
        obstruction_rows = set(points_with_obstructions.keys())

        # We'll iterate over all rows in the path from 1 to H-1 for transition matrices, but power them in big intervals

        # Cache mapping from a row to next row's indexer size
        # We need to handle indexer for each row:
        # Since obstructed rows only appear on key_rows, rows in between have same indexer as key_rows[i]

        # Row-to-indexer mapping + transition matrices for all rows is too big for H large
        # So we solve by noting that the grid only differs on obstructed rows

        # Between two consecutive key_rows (r1 < r2), all intermediate rows are free of obstructions => indexers stable
        # Except the rows of obstructions themselves, obviously.

        # Precompute indexers + transitions for all key rows and their next rows

        # We must ensure we can create a transition matrix for any row y < H
        # Because final row is H, no transition matrix for H needed.

        # So for each key row, cache indexer for y and y+1 if y+1 <= H
        for r in key_rows:
            indexer_for_row(r)
            if r+1 <= self.H:
                indexer_for_row(r+1)

        # Now we handle intervals:
        # key_rows are sorted: [r0=1, r1, r2, ..., rn=H]

        # For each interval [ri, ri+1):
        # We need to move from row=ri to row=ri+1

        def get_transition_for_interval(y: int, length: int) -> TransitionMatrix:
            if length == 0:
                return TransitionMatrix.identity(indexer_for_row(y).size())
            base = get_transition(y)
            return MatrixExponentiator.pow(base, length)

        for i in range(len(key_rows)-1):
            start = key_rows[i]
            end = key_rows[i+1]

            if start == end:
                # no step, no progress
                continue

            length = end - start

            # Check if rows in (start, end) contains any obstruction rows, they are in key_rows so no

            # Translation:
            # The transition matrix between rows start to start+1 is get_transition(start)
            # For length steps, power it length times.

            # BUT!!! We have a problem:
            # The transition matrices can change at rows with obstruction, but this function ensures that
            # key_rows contains those obstruction rows, so inside intervals no obstruction rows appear.

            # So transition matrix at start is stable for whole interval length.

            # Perform matrix exponentiation of transition matrix start over length steps
            # Current ways vector maps to indexer_for_row(start) size
            # Next ways vector maps to indexer_for_row(end) size

            # If sizes differ, we have to chain transformations by stepping row by row, which is not possible here,
            # => Because inside this interval the indexer is fixed except at obstruction rows (which are at endpoints only), so indexer_for_row(start) == indexer_for_row(rows in between)
            # meaning same size and index mapping applies.

            # But actually indexers for start and end may differ because obstacles at row = end

            # Because end is in key_rows, and is distinct from start, the available cells at end may differ from start.

            # So powering transition matrix length times, which maps from row= start to row = start + length
            # Should map between different indexer sizes? Not possible.

            # Thus for length > 1, indexer at consecutive rows must be equal.
            # But indexer changes only at obstruction rows - which appear only at key_rows.

            # So, we assume that indexer_for_row(y) == indexer_for_row(y+1) for rows y in [start, end-1)

            # So between start and end, the state space dimension is the same if no obstruction rows in between.
            # But start and end may differ, so length must be 1. If length > 1, then indexers in intermediate rows are the same.

            # So we'd better break the interval into unit steps, but if length large, impossible.

            # Therefore, we will generalize that inside intervals between key_rows, indexer is same for all y.

            # We must check indexer_for_row(y) is stable for y in [start, end]

            # Let's check all indexers for y in [start, end]

            # Because obstructions only on key_rows, indexers in (start,end) == indexer_for_row(start)

            base_idxr = indexer_for_row(start)
            for ymid in range(start+1, end+1):
                curr_idxr = indexer_for_row(ymid)
                if curr_idxr.index_to_pos != base_idxr.index_to_pos:
                    # This means indexer differ, must break at that row
                    # Break interval into two intervals
                    left_length = ymid - start - 1
                    if left_length > 0:
                        # recurse left interval
                        left_mat = get_transition_for_interval(start, left_length)
                        ways = left_mat.multiply_vector(ways)
                    # single step from ymid-1 to ymid
                    single_step = get_transition(ymid-1)
                    ways = single_step.multiply_vector(ways)
                    # recurse rest interval
                    right_length = end - ymid
                    if right_length > 0:
                        right_mat = get_transition_for_interval(ymid, right_length)
                        ways = right_mat.multiply_vector(ways)
                    break
            else:
                # indexers stable, dimension fixed, safe to exponentiate
                base_mat = get_transition(start)
                Tpow = MatrixExponentiator.pow(base_mat, length)
                ways = Tpow.multiply_vector(ways)

        idxr_end = indexer_for_row(self.H)
        # The ways vector corresponds to the cells at row H (final)
        # We want number of ways to reach (W, H)
        pos_end = GridPosition(self.W, self.H)
        if pos_end in idxr_end.pos_to_index:
            idx = idxr_end.pos_to_index[pos_end]
            return ways[idx] % MOD
        else:
            return 0

def main():
    input = sys.stdin.readline
    case_num = 1
    while True:
        line = ""
        while line.strip() == "":
            line = input()
            if line == '':
                return
        W,H,N = map(int, line.strip().split())
        if W==0 and H==0 and N==0:
            break
        obstructions = []
        for _ in range(N):
            x,y = map(int,input().split())
            obstructions.append((x,y))
        solver = ThreeWayBranchSolver(W,H,N=0)
        solver.obstructions = ObstructionSet(obstructions)
        solver.W = W
        solver.H = H
        ans = solver.solve()
        print(f"Case {case_num}: {ans}")
        case_num += 1

if __name__ == "__main__":
    main()