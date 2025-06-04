class PositionLetterConstraint:
    def __init__(self, position: int, letter: str):
        self.position = position
        self.letter = letter

class SubstringDuplicationHint:
    def __init__(self, start: int, length: int, linked_start: int):
        self.start = start
        self.length = length
        self.linked_start = linked_start  # 0 means no duplication hint here

class Query:
    def __init__(self, position: int):
        self.position = position

class SecretStringPuzzle:
    def __init__(self, n: int):
        self.length = n
        self.position_constraints = []
        self.substr_duplications = []
        self.queries = []

    def add_position_constraint(self, pos: int, letter: str):
        self.position_constraints.append(PositionLetterConstraint(pos, letter))

    def add_substring_duplication(self, start: int, length: int, linked_start: int):
        self.substr_duplications.append(SubstringDuplicationHint(start, length, linked_start))

    def add_query(self, pos: int):
        self.queries.append(Query(pos))

    def process_and_solve(self) -> str:
        # We must handle large length (up to 10^9), so no full arrays.
        # We'll use union-find (disjoint set) data structure indexed by positions involved in hints only.
        # Represent each position that appears in hints or queries as an index in DS.

        # Step 1: Collect all relevant positions that we must consider
        relevant_positions_set = set()
        for pc in self.position_constraints:
            relevant_positions_set.add(pc.position)
        for q in self.queries:
            relevant_positions_set.add(q.position)
        # Positions involved in duplications: all positions in the substring ranges
        for dup in self.substr_duplications:
            relevant_positions_set.add(dup.start)
            if dup.linked_start != 0:
                relevant_positions_set.add(dup.linked_start)
            # add all positions inside the substring ranges since duplication implies equality there
            # but substring length can be deduced by difference between starts of the next hint or n+1 - start
        # To be fully precise, we need all relevant positions inside the substrings described by duplication hints.
        # The substr_duplications list gives us starts sorted ascending by problem statement.
        # Each has length determined by next start - this start, or n+1 - this start if last.

        # Build sorted starts with lengths for easily iterating
        starts = [hint.start for hint in self.substr_duplications]
        starts_len = len(starts)
        start_to_length = {}
        for i, hint in enumerate(self.substr_duplications):
            start = hint.start
            if i+1 < starts_len:
                length = starts[i+1] - start
            else:
                length = self.length + 1 - start
            start_to_length[start] = length

        # Now for each duplication with linked substring, add all positions involved
        for hint in self.substr_duplications:
            if hint.linked_start != 0:
                length = start_to_length[hint.start]
                for offset in range(length):
                    relevant_positions_set.add(hint.start + offset)
                    relevant_positions_set.add(hint.linked_start + offset)

        # Add all positions from duplication substring lengths as well (for those without linked_start=0)
        for hint in self.substr_duplications:
            if hint.linked_start == 0:
                length = start_to_length[hint.start]
                for offset in range(length):
                    relevant_positions_set.add(hint.start + offset)

        # Map positions to continuous ids for Union Find
        positions_sorted = sorted(relevant_positions_set)
        pos_to_id = {pos: idx for idx, pos in enumerate(positions_sorted)}
        id_to_pos = {idx: pos for idx, pos in enumerate(positions_sorted)}

        # Define Union-Find with letter tracking
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0]*size
                # For each component track letter assigned if any
                self.assigned_letter = [None]*size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rx = self.find(x)
                ry = self.find(y)
                if rx != ry:
                    # rank union
                    if self.rank[rx] < self.rank[ry]:
                        rx, ry = ry, rx
                    self.parent[ry] = rx
                    if self.rank[rx] == self.rank[ry]:
                        self.rank[rx] += 1
                    # reconcile letters if any
                    lx = self.assigned_letter[rx]
                    ly = self.assigned_letter[ry]
                    if lx is not None and ly is not None and lx != ly:
                        # conflict is impossible by problem statement,
                        # but just for safety, will raise error if occurs
                        raise ValueError("Contradiction detected in letter assignments")
                    if lx is None and ly is not None:
                        self.assigned_letter[rx] = ly

            def assign_letter(self, x, letter):
                rx = self.find(x)
                cur = self.assigned_letter[rx]
                if cur is not None:
                    if cur != letter:
                        raise ValueError("Contradiction detected in letter assignments")
                else:
                    self.assigned_letter[rx] = letter

            def get_letter(self, x):
                rx = self.find(x)
                return self.assigned_letter[rx]

        uf = UnionFind(len(positions_sorted))

        # Union duplicated substrings positions
        # For each duplication hint with linked_start != 0:
        # substring at start of length L == substring at linked_start of length L
        for hint in self.substr_duplications:
            if hint.linked_start != 0:
                length = start_to_length[hint.start]
                for offset in range(length):
                    p1 = hint.start + offset
                    p2 = hint.linked_start + offset
                    # Both should be in pos_to_id due to above
                    id1 = pos_to_id[p1]
                    id2 = pos_to_id[p2]
                    uf.union(id1, id2)

        # Assign letters from fixed position hints
        for pc in self.position_constraints:
            # Only assign if position is in pos_to_id
            if pc.position in pos_to_id:
                uf.assign_letter(pos_to_id[pc.position], pc.letter)

        # For queries, answer letters or '?'
        result_chars = []
        for q in self.queries:
            pos = q.position
            if pos in pos_to_id:
                letter = uf.get_letter(pos_to_id[pos])
                if letter is None:
                    result_chars.append('?')
                else:
                    result_chars.append(letter)
            else:
                # Position not related to any hint, letter unknown
                result_chars.append('?')

        return ''.join(result_chars)

def main():
    import sys
    input = sys.stdin.readline
    n,a,b,q = map(int, input().split())
    puzzle = SecretStringPuzzle(n)
    for _ in range(a):
        x,c = input().split()
        puzzle.add_position_constraint(int(x), c)
    substr_dup_starts = []
    substr_dup_linked = []
    for _ in range(b):
        y,h = map(int, input().split())
        substr_dup_starts.append(y)
        substr_dup_linked.append(h)
    # We need to convert those into duplication hints with length, after reading all inputs.
    # Positions y_i are strictly increasing, so length = next_y - current_y or n+1 - last_y
    # Per problem statement the "lines with h_i = 0 do not tell any hint except that y_i indicates end of substring specified immediately above"
    # So all can be kept in one list of duplication hints, length computed from y_i's.
    # But as problem states lines with h_i=0 show only end of substring specified above, imply that substring ends there.
    # So the last segment length can be calculated correctly by using y_i's as boundaries.
    # We'll create all hints first then assign length in solve().
    # But for code clarity, we create DuplicationHint objects with start = y_i and linked_start = h_i.

    # Insert duplication hints in puzzle with lengths temporarily unknown, lengths handled inside process_and_solve.
    for y,h in zip(substr_dup_starts, substr_dup_linked):
        puzzle.add_substring_duplication(y, -1, h)  # length -1 placeholder

    for _ in range(q):
        z = int(input())
        puzzle.add_query(z)

    # Now solve and output
    print(puzzle.process_and_solve())

if __name__ == '__main__':
    main()