class Sequence:
    def __init__(self, elements):
        self.elements = elements
        self.length = len(elements)

    def element_at(self, index):
        """Accès à l'élément à une position 1-indexée."""
        return self.elements[index - 1]

class PeriodicityAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def _compute_prefix_function(self):
        """Calcul de la fonction préfixe de la séquence (KMP adaptée)."""
        n = self.sequence.length
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and self.sequence.element_at(i + 1) != self.sequence.element_at(j + 1):
                j = pi[j - 1]
            if self.sequence.element_at(i + 1) == self.sequence.element_at(j + 1):
                j += 1
            pi[i] = j
        return pi

    def maximal_k_part(self):
        """Détermine la plus grande valeur k telle que la séquence est k-part."""
        pi = self._compute_prefix_function()
        n = self.sequence.length
        t = n - pi[-1]
        if n % t == 0:
            return n // t
        else:
            return 1

class InputReader:
    @staticmethod
    def read_sequence_from_input():
        n = int(input())
        elements = list(map(int, input().split()))
        return Sequence(elements)

class PeriodicSequenceSolver:
    def __init__(self):
        self.sequence = None

    def run(self):
        self.sequence = InputReader.read_sequence_from_input()
        analyzer = PeriodicityAnalyzer(self.sequence)
        result = analyzer.maximal_k_part()
        print(result)

if __name__ == "__main__":
    solver = PeriodicSequenceSolver()
    solver.run()