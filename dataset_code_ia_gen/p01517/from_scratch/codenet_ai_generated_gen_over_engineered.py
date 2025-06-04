class Country:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.neighbors = set()

    def add_neighbor(self, neighbor_name: str) -> None:
        self.neighbors.add(neighbor_name)

class AllianceGraph:
    def __init__(self):
        self.countries = {}
        self.name_to_index = {}
        self.index_to_name = []

    def add_country(self, country: Country) -> None:
        if country.name not in self.countries:
            self.countries[country.name] = country
            self.index_to_name.append(country.name)
            self.name_to_index[country.name] = len(self.index_to_name) - 1

    def build_adjacency_matrix(self):
        n = len(self.countries)
        adj = [0] * n
        for i in range(n):
            name_i = self.index_to_name[i]
            country_i = self.countries[name_i]
            bitmask = 0
            for nb in country_i.neighbors:
                j = self.name_to_index[nb]
                bitmask |= 1 << j
            adj[i] = bitmask
        self.adj = adj

    def maximum_alliance_power(self) -> int:
        # This problem can be modeled as a maximum weighted independent set in a graph,
        # with an additional constraint that no neighbors-of-neighbors are included.
        # Since alliance forbids including neighbors and neighbors of neighbors as members,
        # the set must be independent in the square of the adjacency graph.
        #
        # We'll construct the "conflict graph" where an edge (u,v) exists if v is neighbor or
        # neighbor-of-neighbor of u in the original graph. Then find max weighted independent set.
        #
        # Constraints: N <= 40. Use a branch and bound with bitset and memoization.
        n = len(self.countries)
        powers = [self.countries[self.index_to_name[i]].power for i in range(n)]

        # Build second order adjacency including neighbors and neighbors-of-neighbors
        adj2 = [0] * n
        for i in range(n):
            first_order = self.adj[i]
            second_order = 0
            # accumulate neighbors-of-neighbors
            neighbors = first_order
            # iterate over bits set in first_order:
            nb = neighbors
            while nb:
                lsb = nb & (-nb)
                idx = (lsb.bit_length() - 1)
                second_order |= self.adj[idx]
                nb &= nb - 1
            adj2[i] = first_order | second_order | (1 << i)  # also exclude self for independent set

        # We want to select subset S of countries including country 0 (our country),
        # which is independent set in adj2.
        # We must include country 0, so we only consider sets containing 0.

        # We'll implement a bitset branch and bound:
        must_include = 1 << 0

        # Prepare candidates mask (only nodes not conflicting with 0)
        # Must pick 0, so remove anything conflicting with 0 from candidates
        forbidden = adj2[0]
        candidates = ((1 << n) - 1) & (~forbidden)
        # 0 is not in candidates because it is picked
        candidates |= 0

        # The maximum will be at least powers[0] because we must include 0
        best = powers[0]

        # Order nodes for branching: sort decreasing by power to get good bounds
        nodes = list(range(n))
        nodes.remove(0)
        nodes.sort(key=lambda x: powers[x], reverse=True)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(selected_mask: int, candidates_mask: int) -> int:
            nonlocal best
            if candidates_mask == 0:
                # no more nodes to consider
                s = 0
                # compute sum power of selected_mask
                # selected_mask always contains 0
                # but compute sum only once in caller to avoid overhead
                # here we only return 0 and add in caller
                return 0

            # Branch and bound - compute upper bound on remaining selected powers
            # Sum power of candidates + sum selected already
            # Lazy upper bound: sum all candidates possibly included
            upper_bound = 0
            c = candidates_mask
            while c:
                lsb = c & (-c)
                idx = (lsb.bit_length() -1)
                upper_bound += powers[idx]
                c &= c - 1
            # fast check
            # if current best is >= selected + upper_bound => prune
            current_selected_power = 0
            sm = selected_mask
            while sm:
                lsb = sm & (-sm)
                idx = (lsb.bit_length() - 1)
                current_selected_power += powers[idx]
                sm &= sm - 1
            if current_selected_power + upper_bound <= best:
                return 0

            # choose next node for branching - heuristic: max power
            # find node in candidates with max power
            max_power_node = -1
            max_power_val = -1
            c = candidates_mask
            while c:
                lsb = c & (-c)
                idx = (lsb.bit_length()-1)
                if powers[idx] > max_power_val:
                    max_power_val = powers[idx]
                    max_power_node = idx
                c &= c -1

            v = max_power_node

            # Try including v
            # if include v, remove v and neighbors in adj2[v] from candidates
            new_selected = selected_mask | (1 << v)
            new_candidates = candidates_mask & (~adj2[v])
            res_incl = dfs(new_selected, new_candidates)
            res_incl += powers[v]

            # Try excluding v
            # just remove v from candidates
            new_candidates_excl = candidates_mask & (~(1 << v))
            res_excl = dfs(selected_mask, new_candidates_excl)

            res = max(res_incl, res_excl)
            nonlocal best
            if res > best:
                best = res
            return res

        # Starting point: selected_mask includes country 0
        # Candidates cannot include anything conflicting with 0
        selected_mask = 1 << 0
        candidates_mask = ((1 << n) - 1) & (~adj2[0])
        # 0 is already selected, so remove 0 from candidates_mask if present
        candidates_mask &= ~(1 << 0)

        answer = powers[0] + dfs(selected_mask, candidates_mask)
        return answer

class InputProcessor:
    def __init__(self):
        self.graph = AllianceGraph()

    def reset(self):
        self.graph = AllianceGraph()

    def process_dataset(self, lines: list[str]) -> int:
        self.reset()
        N = int(lines[0])
        for i in range(N):
            parts = lines[1 + i].split()
            name = parts[0]
            power = int(parts[1])
            c = int(parts[2])
            neighbors = parts[3:] if c > 0 else []
            country = Country(name, power)
            for nb in neighbors:
                country.add_neighbor(nb)
            self.graph.add_country(country)
        self.graph.build_adjacency_matrix()
        return self.graph.maximum_alliance_power()


def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    processor = InputProcessor()
    while True:
        if idx >= len(input_lines):
            break
        if input_lines[idx].strip() == '0':
            break
        N = int(input_lines[idx].strip())
        if N == 0:
            break
        dataset_lines = input_lines[idx:idx+N+1]
        idx += N+1
        result = processor.process_dataset(dataset_lines)
        print(result)

if __name__ == "__main__":
    main()