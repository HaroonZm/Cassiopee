class GeneSequence:
    def __init__(self, sequence: str):
        self.sequence = sequence

class GeneTransformer:
    BASE_GENE = "ABC"
    
    def __init__(self):
        self.initial_state = GeneSequence(self.BASE_GENE)
    
    def can_transform_to(self, target: GeneSequence) -> bool:
        # On commence de la chaîne 'ABC' et on analyse récursivement
        memo = {}  # Pour mémoriser les résultats des sous-problèmes

        def dfs(current: str) -> bool:
            if current == self.BASE_GENE:
                return True
            if len(current) < len(self.BASE_GENE):
                return False
            if current in memo:
                return memo[current]
            
            # On tente de revenir un coup en arrière en inversant l'opération
            # L'opération consiste à remplacer toutes les occurrences de x par "ABC"
            # Donc inversement on peut chercher un caractère x tel que
            # current est obtenu en remplaçant tous les x par "ABC" dans une chaîne plus petite
            # Ce caractère x correspondra à ceux que l'on cherche à contracter en x.
            
            # La logique inverse:
            # Le multiterrain est un remplacement simultané de x -> "ABC".
            # Inversement, pour chaque caractère (A, B, C) on va essayer de co-contracter "ABC" en un seul x.
            
            # On va essayer pour chaque base A, B, C
            for ch in self.BASE_GENE:
                # Remplacer chaque occurrence de "ABC" dans current par ch, mais uniquement si cela permet de revenir.
                # Pour cela, current doit être formé uniquement par des sous-chaînes ABC ou d'autre chars ?
                
                # Nous allons chercher s'il est possible de découper current en segments "ABC" et d'autres.
                # Si on peut remplacer tous les segments "ABC" par ch et obtenir une chaîne plus petite.
                
                # Pour que ce soit valide, la chaîne doit pouvoir être segmentée en partie comme une chaîne plus petite
                # avec les "ABC" remplacés par ch.
                
                # La méthode:
                # Parcourir current, remplacer toutes les occurrences EXACTES de "ABC" par ch,
                # et voir si cette chaîne plus petite peut être atteinte.
                
                reduced = []
                i = 0
                while i < len(current):
                    if current[i:i+3] == self.BASE_GENE:
                        reduced.append(ch)
                        i += 3
                    else:
                        reduced.append(current[i])
                        i += 1
                reduced_str = "".join(reduced)
                if reduced_str != current and dfs(reduced_str):
                    memo[current] = True
                    return True
            
            memo[current] = False
            return False
        
        return dfs(target.sequence)

class GeneTransformationSolver:
    def __init__(self, sequence: str):
        self.target_sequence = GeneSequence(sequence)
        self.transformer = GeneTransformer()
    
    def solve(self) -> str:
        return "Yes" if self.transformer.can_transform_to(self.target_sequence) else "No"

def main():
    import sys
    input_sequence = sys.stdin.readline().strip()
    solver = GeneTransformationSolver(input_sequence)
    print(solver.solve())

if __name__ == "__main__":
    main()