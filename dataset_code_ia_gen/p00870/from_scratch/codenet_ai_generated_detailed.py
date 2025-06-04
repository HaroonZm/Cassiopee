import sys
from collections import deque, defaultdict

class AhoCorasick:
    """
    Implementation of Aho-Corasick automaton for multiple pattern matching.
    This allows searching for multiple patterns simultaneously in O(text_length + total_pattern_length + number_of_matches).
    """

    def __init__(self):
        self.goto = {}       # trie transitions: state -> char -> next_state
        self.out = defaultdict(set)  # output: state -> set(pattern_ids)
        self.fail = {}       # failure function: state -> fallback state
        self.states = 1      # number of states; state 0 is root

    def add_word(self, word, word_id):
        """
        Add a word in the trie with associated id.
        """
        current = 0
        for ch in word:
            if (current, ch) not in self.goto:
                self.goto[(current, ch)] = self.states
                self.states += 1
            current = self.goto[(current, ch)]
        self.out[current].add(word_id)

    def build(self):
        """
        Build failure links for the automaton using BFS.
        """
        queue = deque()
        self.fail = {0: 0}
        # Initialize failure links for depth 1 states
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            nxt = self.goto.get((0, ch), None)
            if nxt is not None:
                self.fail[nxt] = 0
                queue.append(nxt)
            else:
                self.goto[(0, ch)] = 0  # Add fallback loop to root for missing edges

        # BFS to build fail links and merge output sets
        while queue:
            r = queue.popleft()
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                nxt = self.goto.get((r, ch), None)
                if nxt is not None:
                    queue.append(nxt)
                    self.fail[nxt] = self.goto[(self.fail[r], ch)]
                    self.out[nxt].update(self.out[self.fail[nxt]])

def main():
    input = sys.stdin.readline

    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        n, m = map(int, line.strip().split())
        if n == 0 and m == 0:
            break

        element_strings = []
        length_sum = 0
        for _ in range(n):
            s = sys.stdin.readline().strip()
            element_strings.append(s)
            length_sum += len(s)

        # Read and concatenate all m lines of text into one string ignoring newlines
        text_lines = []
        read_length = 0
        # Since total text length is given only by m lines, read exact m lines
        for _ in range(m):
            line = sys.stdin.readline()
            text_lines.append(line.strip())
        text = ''.join(text_lines)

        # Goal:
        # Find all concatenations of the n element strings in any permutation.
        # Naive permutations is n! (up to 12! ~ very big),
        # so approach:
        # - Build an Aho-Corasick automaton for the element strings
        # - Use DP on text to find positions where concatenations occur
        #
        # Approach details:
        # We want to find in the text all substrings which are concatenations of all element strings in any order.
        # Each element string must appear once, no duplicates unless duplicated strings in elements.
        #
        # Let's assign indices 0..n-1 to element strings.
        #
        # We will run the Aho automaton on the text to find all occurrences of element strings (which element matched at each position)
        #
        # Then, use DP:
        # dp[position][mask] = whether it's possible to form a concatenation using element strings in mask ending exactly at position-1 in text
        # mask is a bitmask of length n, bits set for elements matched so far.
        #
        # dp initialized with dp[0][0] = True (empty)
        #
        # For each position in text, and mask, if dp[pos][mask] = True,
        # and from pos we find an element string ej matching text[pos:pos+len(ej)]
        # then dp[pos+len(ej)][mask|(1<<j)] = True
        #
        # Finally, count the number of positions i where dp[i][full_mask] = True
        # That means a concatenation matched ending at position i-1 (0-based)
        #
        # To do this efficiently:
        # We preprocess all occurrences of element strings in text using Aho-Corasick,
        # For each ending position in text, store list of element strings that end there (their index and length)
        #
        # Then do DP forward.
        # Because n <= 12, we can store dp with mask up to 2^12 = 4096 which is feasible.
        #
        # The length of text <= 5000, so dp size ~ 5000 * 4096 = 20 million booleans -> can be too big in memory.
        #
        # Optimization:
        # - We store dp only for positions from 0 to len(text)
        # - For each position, store a dict or bitset for mask states reachable.
        # Using a queue for BFS style DP on states (position, mask)
        #
        # This reduces memory, as we only store visited states, not the full dp matrix.
        #
        # Summary:
        # 1. Build Aho automaton
        # 2. Find all matches (element string indexes) ending at each position
        # 3. BFS over states (position, mask) starting from (0,0)
        # 4. Whenever mask == full_mask, we record position as a full match ending position.
        # 5. Count distinct starting positions of full concatenations in text.
        #
        # As we want to count the number of positions where concatenation appears (starting positions),
        # note that dp tracks end positions, so starting position = end_pos - total_length + 1

        # Precompute full mask (all elements used)
        full_mask = (1 << n) - 1
        total_length = sum(len(s) for s in element_strings)

        # Build Aho automaton for element strings
        aho = AhoCorasick()
        for i, s in enumerate(element_strings):
            aho.add_word(s, i)
        aho.build()

        # Run Aho automaton on text to find matches ending at each position
        # matches_at_pos[i] = list of tuples (element_index, length) for matches ending at i-th char (0-based)
        matches_at_pos = [[] for _ in range(len(text))]
        state = 0
        for i, ch in enumerate(text):
            state = aho.goto[(state, ch)]
            if aho.out[state]:
                for pattern_id in aho.out[state]:
                    length = len(element_strings[pattern_id])
                    matches_at_pos[i].append((pattern_id, length))

        # BFS DP
        from collections import deque

        # visited states: (position, mask)
        visited = [set() for _ in range(len(text)+1)]
        queue = deque()
        # start from position 0, mask 0 (no elements matched)
        visited[0].add(0)
        queue.append((0,0))
        result_positions = set()

        while queue:
            pos, mask = queue.popleft()
            # If all elements matched, record the match starting position
            if mask == full_mask:
                # concatenation ends at pos-1 (0-based index)
                start_pos = pos - total_length
                if start_pos >= 0:
                    result_positions.add(start_pos)
                # No need to continue from here, but can continue for overlapping occurrences

            if pos == len(text):
                # Reached end of text, can't extend further
                continue

            # For all matches that start at pos
            # Our matches_at_pos is for ending positions, so we must find matches starting at pos
            # matches are recorded by their end index, so for matches that start at pos:
            # For all positions end >= pos where a pattern ends such that start = end - len + 1 == pos
            # We do reverse lookup: For position pos, check matches ending at end_pos = pos + len -1

            # Iterate all matches that end at i where i >= pos + something?
            # Instead, for each possible offset in element_strings:
            # precalc is matches_at_pos[end_pos], so check matches ending at end_pos = pos + len(e[s]) -1

            # Let's try to do it with this approach:
            # For each element string j:
            # compute end_pos = pos + len(element_strings[j]) - 1
            # if end_pos < len(text) and matches_at_pos[end_pos] contains (j, len(element_strings[j])) then possible

            for j in range(n):
                if (mask >> j) & 1 == 1:
                    continue  # element j already used
                length_j = len(element_strings[j])
                end_pos = pos + length_j - 1
                if end_pos >= len(text):
                    continue
                # Check if element j matches ending at end_pos
                # Use a fast membership check:
                # matches_at_pos[end_pos] is small (patterns ending there)
                # Check if (j, length_j) in matches_at_pos[end_pos]
                # Using a set for matches_at_pos[end_pos] for better lookup

            # To speed up membership check, prepare sets per end_pos
            # Let's prepare once outside the loop

            # So break to outer loop to prepare sets outside for speed
            break

        # Prepare sets for membership check
    # --- Re-starting after restart for membership ---

def main_full():
    import sys
    from collections import deque, defaultdict

    class AhoCorasick:
        def __init__(self):
            self.goto = {}
            self.out = defaultdict(set)
            self.fail = {}
            self.states = 1

        def add_word(self, word, word_id):
            current = 0
            for ch in word:
                if (current, ch) not in self.goto:
                    self.goto[(current, ch)] = self.states
                    self.states += 1
                current = self.goto[(current, ch)]
            self.out[current].add(word_id)

        def build(self):
            queue = deque()
            self.fail = {0: 0}
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                nxt = self.goto.get((0, ch), None)
                if nxt is not None:
                    self.fail[nxt] = 0
                    queue.append(nxt)
                else:
                    self.goto[(0, ch)] = 0
            while queue:
                r = queue.popleft()
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = self.goto.get((r, ch), None)
                    if nxt is not None:
                        queue.append(nxt)
                        self.fail[nxt] = self.goto[(self.fail[r], ch)]
                        self.out[nxt].update(self.out[self.fail[nxt]])

    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        n, m = map(int, line.strip().split())
        if n == 0 and m == 0:
            break

        element_strings = []
        length_sum = 0
        for _ in range(n):
            s = sys.stdin.readline().strip()
            element_strings.append(s)
            length_sum += len(s)

        text_lines = []
        for _ in range(m):
            line = sys.stdin.readline()
            text_lines.append(line.strip())
        text = ''.join(text_lines)

        full_mask = (1 << n) - 1
        total_length = length_sum

        # Build Aho automaton
        aho = AhoCorasick()
        for i, s in enumerate(element_strings):
            aho.add_word(s, i)
        aho.build()

        matches_at_pos = [[] for _ in range(len(text))]
        state = 0
        for i, ch in enumerate(text):
            state = aho.goto[(state, ch)]
            if aho.out[state]:
                for pid in aho.out[state]:
                    length_p = len(element_strings[pid])
                    matches_at_pos[i].append((pid, length_p))

        # Prepare sets for quick membership
        matches_set_at_pos = [set(m) for m in matches_at_pos]

        from collections import deque
        visited = [set() for _ in range(len(text)+1)]
        queue = deque()
        visited[0].add(0)
        queue.append((0,0))
        result_positions = set()

        while queue:
            pos, mask = queue.popleft()
            if mask == full_mask:
                start_pos = pos - total_length
                if start_pos >= 0:
                    result_positions.add(start_pos)
                # do not return, consider overlapping occurrences

            if pos == len(text):
                continue

            # Try to extend from pos with any element string not used
            for j in range(n):
                if (mask >> j) & 1 == 1:
                    continue
                length_j = len(element_strings[j])
                end_pos = pos + length_j - 1
                if end_pos >= len(text):
                    continue
                if (j, length_j) in matches_set_at_pos[end_pos]:
                    next_mask = mask | (1 << j)
                    if next_mask not in visited[end_pos+1]:
                        visited[end_pos+1].add(next_mask)
                        queue.append((end_pos+1, next_mask))

        print(len(result_positions))


if __name__ == "__main__":
    main_full()