class SequenceInterface:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.length = len(sequence)

    def is_subsequence(self, subsequence: str) -> bool:
        # Abstract method placeholder
        raise NotImplementedError


class BinarySequence(SequenceInterface):
    def __init__(self, sequence: str):
        super().__init__(sequence)
        # Preprocessing for subsequence check via next occurrence table
        self.next_pos = self._build_next_pos_table()

    def _build_next_pos_table(self):
        # Construct next occurrence table for 0 and 1
        # next_pos[i][c] = the minimum index j >= i with sequence[j] == c, or length if none exists
        n = self.length
        next_pos = [[n, n] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            next_pos[i] = next_pos[i + 1].copy()
            bit = int(self.sequence[i])
            next_pos[i][bit] = i
        return next_pos

    def is_subsequence(self, subsequence: str) -> bool:
        # Efficient subsequence check in O(len(subsequence)) using next_pos table
        pos = 0
        n = self.length
        for ch in subsequence:
            bit = int(ch)
            if self.next_pos[pos][bit] == n:
                return False
            pos = self.next_pos[pos][bit] + 1
            if pos > n:
                return False
        return True


class ShortestCommonNonSubsequenceSolver:
    def __init__(self, seq1: str, seq2: str):
        self.seqX = BinarySequence(seq1)
        self.seqY = BinarySequence(seq2)
        self.memo = dict()

    def solve(self) -> str:
        # We seek the shortest, lex smallest string of 0 and 1 that is subsequence of neither seqX nor seqY
        # Brute force all sequences by length from 1 upward, with pruning using memoization

        # Use BFS over sequences' last matched positions in seqX and seqY
        from collections import deque

        # Each state: (posX, posY, current_sequence)
        # posX, posY: next positions in seqX, seqY for matching current_sequence as subsequence
        # We try to extend current_sequence by adding 0 or 1 at the end, transition states accordingly
        nX, nY = self.seqX.length, self.seqY.length
        start_state = (0, 0, "")
        queue = deque([start_state])
        visited = set()
        visited.add((0, 0))

        while queue:
            posX, posY, cur_seq = queue.popleft()
            # Try extending by '0' and '1' lex order
            for ch in ['0', '1']:
                bit = int(ch)
                # Compute next pos in seqX:
                next_posX = self.seqX.next_pos[posX][bit] + 1 if posX <= nX else nX + 1
                # Compute next pos in seqY:
                next_posY = self.seqY.next_pos[posY][bit] + 1 if posY <= nY else nY + 1

                new_seq = cur_seq + ch

                # If this new_seq is NOT a subsequence of seqX and seqY:
                # subsequence if next_pos <= length, so not subsequence if next_pos > length
                # We use next_posX - 1 and next_posY - 1 as last matched index, if next_posX-1 >= nX no match
                if (next_posX - 1) > nX and (next_posY - 1) > nY:
                    # Found shortest common non-subsequence (by BFS layer ordering)
                    return new_seq

                # Else continue BFS if state not visited
                # Only enqueue if subsequence so far of both sequences
                # Also prune if (next_posX, next_posY) visited
                # But also allow pos == length as valid position since next_pos can be length = n

                # Clamp to nX+1 to avoid huge indices
                next_posX_c = min(next_posX, nX+1)
                next_posY_c = min(next_posY, nY+1)

                if (next_posX_c, next_posY_c) not in visited:
                    visited.add((next_posX_c, next_posY_c))
                    queue.append((next_posX_c, next_posY_c, new_seq))


def main():
    import sys
    seq1 = sys.stdin.readline().strip()
    seq2 = sys.stdin.readline().strip()

    solver = ShortestCommonNonSubsequenceSolver(seq1, seq2)
    answer = solver.solve()
    print(answer)


if __name__ == "__main__":
    main()