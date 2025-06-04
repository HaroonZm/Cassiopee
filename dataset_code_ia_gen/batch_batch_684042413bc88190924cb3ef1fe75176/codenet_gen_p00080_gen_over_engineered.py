class CubeRootApproximator:
    """
    Une classe abstraite pour approximer la racine cubique d'un nombre positif
    en utilisant un procédé itératif défini par une fonction d'itération.
    """

    def __init__(self, q: int):
        if q <= 0:
            raise ValueError("q doit être un entier strictement positif")
        self.q = q
        self.tolerance = 0.00001 * q
        self.x = q / 2  # x1 initiale

    def iterate(self, x: float) -> float:
        """
        Calcul de la prochaine approximation selon la formule :
        x_{n+1} = x_n - (x_n^3 - q) / (3 * x_n^2)
        """
        numerator = x ** 3 - self.q
        denominator = 3 * (x ** 2)
        return x - numerator / denominator

    def has_converged(self, x: float) -> bool:
        """
        Condition de convergence : |x^3 - q| < tolerance
        """
        error = abs(x ** 3 - self.q)
        return error < self.tolerance

    def approximate(self) -> float:
        """
        Exécute l'algorithme d'approximation itérative jusqu'à convergence.
        """
        iteration_limit = 1000  # sécurité pour éviter boucle infinie
        for _ in range(iteration_limit):
            if self.has_converged(self.x):
                return self.x
            self.x = self.iterate(self.x)
        # Si on sort de la boucle, on retourne la meilleure approximation trouvée
        return self.x


class CubeRootSolver:
    """
    Gestionnaire d'exécution pour plusieurs données et affichage des résultats
    """

    def __init__(self):
        self.results = []

    def process_input(self, q_values):
        """
        Processus global pour plusieurs données
        """
        for q in q_values:
            if q == -1:
                break
            approximator = CubeRootApproximator(q)
            root = approximator.approximate()
            self.results.append(root)

    def output_results(self):
        """
        Affiche les résultats formatés selon la demande
        """
        for result in self.results:
            print(f"{result:.6f}")


def main():
    import sys

    solver = CubeRootSolver()
    input_values = []

    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        try:
            q = int(line)
            input_values.append(q)
            if q == -1:
                break
        except ValueError:
            continue

    solver.process_input(input_values)
    solver.output_results()


if __name__ == "__main__":
    main()