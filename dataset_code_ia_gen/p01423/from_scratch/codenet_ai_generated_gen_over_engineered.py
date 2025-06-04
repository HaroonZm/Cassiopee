class Rabbit:
    def __init__(self, id_):
        self.id = id_
        self.friends = {}
    
    def add_friend(self, other, friendliness):
        self.friends[other] = friendliness
    
    def potential_satisfaction(self, group):
        # Calculate minimal friendliness with other guests in the group
        if len(group) <= 1:
            return 0
        relevant = [self.friends.get(r.id, 0) for r in group if r != self]
        if 0 in relevant:
            return 0
        return min(relevant)

class Party:
    def __init__(self, rabbits):
        self.rabbits = rabbits
    
    def satisfaction(self, group):
        return sum(r.potential_satisfaction(group) for r in group)
    
    def max_satisfaction(self):
        # We seek subset of rabbits maximizing satisfaction score
        # Given n up to 100, we try advanced branch and bound with abstractions
        
        from itertools import combinations
        
        class CandidateGroup:
            def __init__(self, members):
                self.members = members
                self.score = None
            
            def compute_score(self):
                if self.score is not None:
                    return self.score
                if len(self.members) == 0:
                    self.score = 0
                    return 0
                self.score = sum(r.potential_satisfaction(self.members) for r in self.members)
                return self.score
        
        class Solver:
            def __init__(self, rabbits):
                self.rabbits = rabbits
                self.n = len(rabbits)
                self.best_score = 0
                self.best_group = []
            
            def _improve(self, group):
                score = group.compute_score()
                if score > self.best_score:
                    self.best_score = score
                    self.best_group = group.members[:]
            
            def _recursive_search(self, group, index):
                # Pruning: estimate maximum possible score from remaining rabbits
                self._improve(group)
                
                if index >= self.n:
                    return
                
                # Try excluding current rabbit
                self._recursive_search(group, index+1)
                
                # Try including current rabbit
                new_members = group.members + [self.rabbits[index]]
                new_group = CandidateGroup(new_members)
                
                # Heuristic pruning: if any in new_members has 0 friendship with others, skip
                # But allow single member groups (score=0)
                # relaxed to not prune here because 0 minimal would yield 0 satisfaction for that rabbit, but maybe group still improves overall
                self._recursive_search(new_group, index+1)
            
            def solve(self):
                initial_group = CandidateGroup([])
                self._recursive_search(initial_group, 0)
                return self.best_score
        
        solver = Solver(self.rabbits)
        return solver.solve()

class RabbitGraph:
    def __init__(self, n):
        self.rabbits = [Rabbit(i+1) for i in range(n)]
    
    def add_edge(self, u, v, f):
        self.rabbits[u-1].add_friend(self.rabbits[v-1], f)
        self.rabbits[v-1].add_friend(self.rabbits[u-1], f)
    
    def solve(self):
        party = Party(self.rabbits)
        return party.max_satisfaction()

def main():
    import sys
    input = sys.stdin.readline
    n,m = map(int, input().split())
    graph = RabbitGraph(n)
    for _ in range(m):
        u,v,f = map(int, input().split())
        graph.add_edge(u,v,f)
    print(graph.solve())

if __name__ == "__main__":
    main()