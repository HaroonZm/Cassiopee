class Role:
    CODER = 'C'
    ALGORITHMER = 'A'
    NAVIGATOR = 'N'

class Formation:
    # Formation definitions mapping roles to their counts
    FORMATIONS = {
        'CCA': {Role.CODER: 2, Role.ALGORITHMER: 1, Role.NAVIGATOR: 0},
        'CCC': {Role.CODER: 3, Role.ALGORITHMER: 0, Role.NAVIGATOR: 0},
        'CAN': {Role.CODER: 1, Role.ALGORITHMER: 1, Role.NAVIGATOR: 1},
    }
    
    @classmethod
    def all_formations(cls):
        return cls.FORMATIONS.items()

class TeamComposition:
    def __init__(self, coders: int, algos: int, navis: int):
        self.roles = {
            Role.CODER: coders,
            Role.ALGORITHMER: algos,
            Role.NAVIGATOR: navis,
        }
        
    def can_form(self, formation_roles):
        """Check if we can form one team of the given formation."""
        return all(self.roles.get(role, 0) >= count for role, count in formation_roles.items())
    
    def consume(self, formation_roles, times=1):
        """Consume members of roles used to form a number of teams."""
        for role, count in formation_roles.items():
            self.roles[role] -= count * times
    
    def max_teams_for_formation(self, formation_roles):
        """Compute the max number of teams for a given formation possible."""
        return min(self.roles.get(role, 0) // count if count > 0 else float('inf')
                   for role, count in formation_roles.items())
    
    def copy(self):
        return TeamComposition(
            self.roles[Role.CODER],
            self.roles[Role.ALGORITHMER],
            self.roles[Role.NAVIGATOR]
        )

class TeamBuilder:
    def __init__(self, initial_composition: TeamComposition):
        self.initial = initial_composition
    
    def max_teams(self):
        """
        We attempt to form teams picking quantities from the three formations
        to maximize total teams formed, respecting available roles.

        Since roles are up to 1000, a complete search approach is acceptable.

        Optimizations or DP could be considered if this grew larger.
        """
        max_total = 0
        C = self.initial.roles[Role.CODER]
        A = self.initial.roles[Role.ALGORITHMER]
        N = self.initial.roles[Role.NAVIGATOR]
        
        # Formation roles mappings
        cca = Formation.FORMATIONS['CCA']
        ccc = Formation.FORMATIONS['CCC']
        can = Formation.FORMATIONS['CAN']
        
        # The counts needed for each:
        # cca needs 2 C, 1 A
        # ccc needs 3 C
        # can needs 1 C, 1 A, 1 N
        
        # Max number of teams for each formation individually:
        max_cca = min(C // 2, A)
        max_ccc = C // 3
        max_can = min(C, A, N)
        
        # Brute force over possible counts of cca and can, derive ccc:
        # We try all combinations of cca and can, compute leftover coders,
        # then fill with ccc as much as possible.
        # This is because cca and can consume A and N roles, ccc only coders.
        
        for cca_count in range(max_cca + 1):
            for can_count in range(max_can + 1):
                # Remaining coders and algos and navis:
                rem_c = C - cca_count * 2 - can_count * 1
                rem_a = A - cca_count * 1 - can_count * 1
                rem_n = N - can_count * 1
                
                if rem_c < 0 or rem_a < 0 or rem_n < 0:
                    continue
                
                ccc_count = rem_c // 3
                
                total = cca_count + can_count + ccc_count
                if total > max_total:
                    max_total = total
        
        return max_total

def main():
    import sys
    input = sys.stdin.readline
    
    Q = int(input())
    for _ in range(Q):
        c,a,n = map(int, input().split())
        composition = TeamComposition(c, a, n)
        builder = TeamBuilder(composition)
        print(builder.max_teams())

if __name__ == "__main__":
    main()