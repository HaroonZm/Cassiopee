import sys
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Optional, Set

class MonsterIndexOutOfBounds(Exception):
    pass

class InvalidMonsterPairException(Exception):
    pass

class TeamFormationImpossible(Exception):
    pass

class InputReader(ABC):
    @abstractmethod
    def read(self) -> Tuple[int, int, int, List[Tuple[int,int,int]]]:
        pass

class StdInputReader(InputReader):
    def read(self) -> Tuple[int, int, int, List[Tuple[int,int,int]]]:
        input_lines = sys.stdin.read().strip().split('\n')
        N, M, K = map(int, input_lines[0].split())
        pairs = []
        if M > 0:
            for line in input_lines[1:1+M]:
                a,b,c = map(int, line.split())
                pairs.append((a,b,c))
        return N, M, K, pairs

class Monster:
    def __init__(self, id_: int):
        self.id = id_

class InteractionType:
    FORBIDDEN = 0    # c_i=0
    NORMAL = 1       # c_i != 0
    DEFAULT = 2      # no data, friendship=0

class Interaction:
    def __init__(self, monster1: Monster, monster2: Monster, c_value: int):
        if monster1.id == monster2.id:
            raise InvalidMonsterPairException("Monster can't interact with itself.")
        self.m1 = monster1
        self.m2 = monster2
        self.c = c_value
        self.type = InteractionType.FORBIDDEN if c_value == 0 else InteractionType.NORMAL if c_value != 0 else InteractionType.DEFAULT

    def is_forbidden(self) -> bool:
        return self.type == InteractionType.FORBIDDEN

    def friendship(self) -> int:
        if self.type == InteractionType.NORMAL:
            return self.c
        return 0

class MonsterRepository:
    def __init__(self, n: int):
        if n < 1:
            raise MonsterIndexOutOfBounds("Number of monsters must be positive")
        self.monsters: Dict[int, Monster] = {}
        for i in range(1,n+1):
            self.monsters[i] = Monster(i)

    def get(self, id_: int) -> Monster:
        if id_ not in self.monsters:
            raise MonsterIndexOutOfBounds(f"Monster ID {id_} out of bounds")
        return self.monsters[id_]

class InteractionGraph:
    def __init__(self, monster_repo: MonsterRepository):
        self.repo = monster_repo
        self.forbidden_edges: Dict[int, Set[int]] = {}  # adjacency sets
        self.friendship_edges: Dict[int, Dict[int,int]] = {}  # weighted adjacency (only normal edges)

    def add_interaction(self, a: int, b: int, c: int):
        m1 = self.repo.get(a)
        m2 = self.repo.get(b)
        inter = Interaction(m1,m2,c)
        if inter.is_forbidden():
            self.forbidden_edges.setdefault(a,set()).add(b)
            self.forbidden_edges.setdefault(b,set()).add(a)
        else:
            if a not in self.friendship_edges:
                self.friendship_edges[a] = {}
            if b not in self.friendship_edges:
                self.friendship_edges[b] = {}
            self.friendship_edges[a][b] = inter.friendship()
            self.friendship_edges[b][a] = inter.friendship()

    def is_forbidden_pair(self,a:int,b:int) -> bool:
        return b in self.forbidden_edges.get(a,set())

    def friendship_between(self,a:int,b:int) -> int:
        # If no known pair, default 0
        return self.friendship_edges.get(a,{}).get(b,0)

class TeamSelector(ABC):
    @abstractmethod
    def select_team(self) -> Optional[int]:
        pass

class SocialMonstersTeamSelector(TeamSelector):
    def __init__(self, N:int, M:int, K:int, interactions: List[Tuple[int,int,int]]):
        self.N = N
        self.M = M
        self.K = K
        self.repo = MonsterRepository(N)
        self.graph = InteractionGraph(self.repo)
        for (a,b,c) in interactions:
            self.graph.add_interaction(a,b,c)

    def select_team(self) -> Optional[int]:
        # The task is to select K monsters without forbidden edges and maximize sum of friendships among them
        # Forbidden pairs can't be selected together.

        # Idea:
        # Because forbidden pairs forbid joint inclusion, they form a "conflict graph"
        # Select an independent set of size K in the forbidden graph and maximize friendship sum among chosen.
        # Friendship sum includes edges with c!=0 or 0 if no info.

        # But the forbidden edges are a conflict graph adjacency.

        # The problem reduces to:
        # - Find a size-K subset with no forbidden pairs
        # - Maximize sum of friendship edges within that subset

        # Constraints:
        # N,K up to 2000 (quite large)

        # Approach:
        # Use DP on bitsets is too big (2^N).
        # Each monster appears in up to max 2 interactions, so forbidden edges max M <= N
        # The forbidden relations are sparse.

        # Construct complement graph of forbidden edges: allowed edges for coalition.

        # Since each monster appears in forbidden edges max 2 times, forbidden graph is set of at most chains/cycle components

        # Our problem can be reduced on connected components of forbidden graph.

        # Step1: Find connected components of forbidden graph
        components = self._get_forbidden_connected_components()

        # For each connected component, select subset avoiding forbidden pairs (forbid edges inside component)
        # Outside component no forbidden edges connect

        # So total set = union of subsets from components
        # We must pick exactly K monsters in total

        # For each component, enumerate all allowed subsets (cliques in complement of forbidden edges)
        # Number of nodes per component will be very small because max edges M<=N and monsters appear max 2 times in forbidden edges.

        # Components can be up to size ~ 3 (linear chains or small ones due to constraints)

        comp_subsets = []
        for comp in components:
            subset_infos = self._enumerate_component_subsets(comp)
            comp_subsets.append(subset_infos)

        # Now we combine subsets from components to get total size K and maximize total friendship

        # Standard DP knapsack on components:
        # dp[i][s] = max friendship sum picking s monsters from first i components

        dp = [-10**15]*(self.K+1)
        dp[0] = 0

        for subset_infos in comp_subsets:
            ndp = [-10**15]*(self.K+1)
            for picked_so_far in range(self.K+1):
                if dp[picked_so_far] < -10**14:
                    continue
                for (sz, val) in subset_infos:
                    if picked_so_far+sz <= self.K:
                        nv = dp[picked_so_far] + val
                        if nv > ndp[picked_so_far+sz]:
                            ndp[picked_so_far+sz] = nv
            dp = ndp

        if dp[self.K] < -10**14:
            return None
        return dp[self.K]

    def _get_forbidden_connected_components(self) -> List[List[int]]:
        visited = [False]*(self.N+1)
        graph = self.graph.forbidden_edges
        components = []

        def dfs(u: int, comp: List[int]):
            visited[u] = True
            comp.append(u)
            for w in graph.get(u,set()):
                if not visited[w]:
                    dfs(w,comp)

        for v in range(1,self.N+1):
            if not visited[v]:
                comp = []
                dfs(v,comp)
                components.append(comp)
        return components

    def _enumerate_component_subsets(self, comp: List[int]) -> List[Tuple[int,int]]:
        # Allowed subsets: subsets with no forbidden edges inside component.
        # Forbidden edges inside component form conflict edges, so allowed subsets = independent sets of that conflict subgraph.

        # Since component sizes are small (max ~3) due to constraints, enumerate all subsets

        forbidden_subgraph = {v:set() for v in comp}
        for v in comp:
            forb = self.graph.forbidden_edges.get(v,set())
            for w in forb:
                if w in comp:
                    forbidden_subgraph[v].add(w)

        comp_size = len(comp)
        idx_map = {v:i for i,v in enumerate(comp)}

        # Precompute friendship sums for subsets
        # Friendship = sum friendship edges of all pairs in subset

        subsets = []
        for mask in range(1 << comp_size):
            valid = True
            picked = [comp[i] for i in range(comp_size) if (mask & (1 << i))]
            # Check forbidden edges
            for i in range(len(picked)):
                for j in range(i+1,len(picked)):
                    if picked[j] in forbidden_subgraph[picked[i]]:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                continue
            # Compute friendship sum:
            val = 0
            for i in range(len(picked)):
                for j in range(i+1,len(picked)):
                    val += self.graph.friendship_between(picked[i],picked[j])

            subsets.append((len(picked),val))
        return subsets


def main():
    reader = StdInputReader()
    N, M, K, pairs = reader.read()
    selector = SocialMonstersTeamSelector(N,M,K,pairs)
    res = selector.select_team()
    if res is None:
        print("Impossible")
    else:
        print(res)

if __name__ == "__main__":
    main()