from collections import defaultdict
from typing import Dict, Set, List


class StringTransformer:
    def __init__(self, n: int, s: str, t: str):
        self.length = n
        self.s = s
        self.t = t
        self.alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        self.graph = CharMappingGraph(self.alphabet)
    
    def minimal_replacements(self) -> int:
        # Step 1: Jennifer rearranges s arbitrarily
        # Since Jennifer can rearrange arbitrarily,
        # just sort s and t's frequency sets match to minimize replacements.
        s_freq = FrequencyProfile(self.s)
        t_freq = FrequencyProfile(self.t)
        
        # Find which characters in s correspond to which characters in t
        # frequency-wise after optimal rearrangement (only counts per letter matter)
        
        # Construct character map edges by frequencies:
        # For each letter in s frequency profile that has frequency f,
        # connect it to letters in t frequency profile with frequency f,
        # because Jennifer can reorder s, and Marian can swap letters globally,
        # so actual mapping reduces to matching frequencies to minimize replacements.
        
        freq_to_chars_s = s_freq.inverse_profile()
        freq_to_chars_t = t_freq.inverse_profile()

        # Create edges between chars with same frequency
        for freq in freq_to_chars_s:
            chars_s = freq_to_chars_s[freq]
            chars_t = freq_to_chars_t.get(freq, set())
            for cs in chars_s:
                for ct in chars_t:
                    self.graph.add_edge(cs, ct)

        # Marian can swap letters to identify connected components => merge chars
        # final minimal replacements = number of connected components - number of matches
        # Actually, replacements correspond to the number of connected components - number of matched chars
        
        # But problem is actually simpler:
        # After Jennifer sorts S arbitrarily,
        # Marian swaps letters to make character sets match as closely as possible,
        # Karin then replaces chars that cannot be matched.
        # This reduces to counting connected components in the character mapping graph
        # and minimal replacements = number_of_unique_characters_in_T - number_of_connected_components

        # So build undirected graph from pairs (s_char, t_char) at same position
        pairs = list(zip(self.s, self.t))
        for cs, ct in pairs:
            self.graph.add_bi_edge(cs, ct)

        connected_components = self.graph.count_connected_components()
        unique_in_t = len(set(self.t))

        # minimal replacements = component count - number of connected components reducing to
        # replacement count = connected_components - 1 (generally in union-find approach)
        # We interpret as minimal number of replacements is (unique chars in T) - (number of connected components)

        # Correction: As per editorial reasoning below:
        # replacements = number of components - 1 (only if no isolated chars)
        # But we want minimal characters replacements after these swaps
        # Actually minimal replacements = number_of_unique_characters_in_T - number_of_connected_components
        # Because each cc corresponds to a merged character group we can swap to one unified character
        # Final characters in T minus connected components will be required replacements

        return unique_in_t - connected_components


class FrequencyProfile:
    def __init__(self, string: str):
        self.counts: Dict[str, int] = defaultdict(int)
        for c in string:
            self.counts[c] += 1

    def inverse_profile(self) -> Dict[int, Set[str]]:
        freq_map = defaultdict(set)
        for c, f in self.counts.items():
            freq_map[f].add(c)
        return freq_map


class CharMappingGraph:
    def __init__(self, alphabet: List[str]):
        self.adj: Dict[str, Set[str]] = {c: set() for c in alphabet}
        self.visited: Set[str] = set()
    
    def add_edge(self, u: str, v: str) -> None:
        # Directed edge for frequency-matching abstraction (not used directly)
        if u != v:
            self.adj[u].add(v)
    
    def add_bi_edge(self, u: str, v: str) -> None:
        if u != v:
            self.adj[u].add(v)
            self.adj[v].add(u)
    
    def _dfs(self, node: str) -> None:
        self.visited.add(node)
        for neighbor in self.adj[node]:
            if neighbor not in self.visited:
                self._dfs(neighbor)
    
    def count_connected_components(self) -> int:
        count = 0
        self.visited.clear()
        nodes_with_edges_or_letters = {c for c in self.adj if self.adj[c] or any(c == x for x in self.adj)}
        # Actually we consider all characters occurring in s or t for components:
        for node in self.adj:
            if (node not in self.visited) and (self.adj[node] or True):
                self._dfs(node)
                count += 1
        return count


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()

    transformer = StringTransformer(n, s, t)
    result = transformer.minimal_replacements()
    print(result)


if __name__ == "__main__":
    main()