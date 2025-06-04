import math
import sys

# Valeur de pi fournie par la bibliothèque math
PI = math.pi

def approximate_pi(allowed_error):
    """
    Trouve une fraction num/den approximant pi telle que
    |num/den - pi| <= allowed_error,
    avec le plus petit dénominateur possible.
    En cas d'égalité sur le dénominateur, on choisit la meilleure approximation.

    Approach:
    - On énumère les dénominateurs à partir de 1 vers le haut.
    - Pour chaque dénominateur d, on calcule le numérateur n = round(pi * d)
      pour obtenir l'approximation la plus proche avec ce dénominateur.
    - On vérifie si |n/d - pi| <= allowed_error.
    - La première fraction trouvée avec ce critère et le plus petit dénominateur
      est renvoyée.
    - Cette méthode est efficace puisque la fraction optimale aura forcément un
      dénominateur not too large, car l'erreur tolérée est donnée comme <= 1.

    """
    d = 1
    while True:
        # Numérateur le plus proche de pi * d
        n = round(PI * d)
        approximation = n / d
        error = abs(approximation - PI)
        if error <= allowed_error:
            return f"{n}/{d}"
        d += 1

def main():
    """
    Lecture jusqu'à ce que 0.0 soit rencontré.
    Pour chaque valeur R, on calcule et affiche la fraction selon les contraintes.
    """
    for line in sys.stdin:
        line = line.strip()
        if line == "0.0":
            break
        R = float(line)
        result = approximate_pi(R)
        print(result)

if __name__ == "__main__":
    main()