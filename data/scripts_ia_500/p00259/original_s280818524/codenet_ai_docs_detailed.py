import re

class c(int):
    """
    Classe représentant un entier modulo p.
    Cette classe hérite de int mais redéfinit les opérations arithmétiques
    pour fonctionner modulo p, où p est une variable globale définie dynamiquement.
    """
    global p  # Indique que p est une variable globale accessible dans cette classe

    def __add__(self, n):
        """
        Surcharge de l'opérateur + pour effectuer une addition modulo p.

        Args:
            n (int or c): L'opérande à additionner.

        Returns:
            c: Le résultat de l'addition modulo p, encapsulé dans la classe c.
        """
        return c((int(self) + int(n)) % p)

    def __sub__(self, n):
        """
        Surcharge de l'opérateur - pour effectuer une soustraction modulo p.

        Args:
            n (int or c): L'opérande à soustraire.

        Returns:
            c: Le résultat de la soustraction modulo p, encapsulé dans la classe c.
        """
        return c((int(self) - int(n)) % p)

    def __mul__(self, n):
        """
        Surcharge de l'opérateur * pour effectuer une multiplication modulo p.

        Args:
            n (int or c): L'opérande à multiplier.

        Returns:
            c: Le résultat de la multiplication modulo p, encapsulé dans la classe c.
        """
        return c((int(self) * int(n)) % p)

    def __truediv__(self, n):
        """
        Surcharge de l'opérateur / pour effectuer une division modulo p.
        La division est définie comme la multiplication par l'inverse multiplicatif modulo p.

        Args:
            n (int or c): Le dénominateur.

        Raises:
            ZeroDivisionError: Si n est égal à zéro.

        Returns:
            c: Le résultat de la division modulo p, encapsulé dans la classe c.
        """
        if n == 0:
            raise ZeroDivisionError("division by zero")
        # Calcul de l'inverse multiplicatif modulo p en utilisant le petit théorème de Fermat
        inv = pow(int(n), p - 2, p)
        return self * inv


while True:
    # Lecture de l'entrée utilisateur sous la forme "p : expression"
    line = input()
    p_str, f = line.replace(' ', '').split(':')  # Suppression des espaces puis séparation
    p = int(p_str)  # Conversion de p en entier

    if p == 0:
        # Condition d'arrêt du programme
        break

    try:
        # Remplacement de tous les nombres dans l'expression par des instances de la classe c
        # Cela permet d'exécuter l'expression modulo p en surchargeant les opérations
        expr_mod = re.sub(r'(\d+)', r'c(\1)', f)

        # Evaluation de l'expression modulaire
        result = eval(expr_mod)
        
        # Affichage du résultat au format demandé
        print(f"{f} = {result} (mod {p})")
    except Exception:
        # En cas d'erreur (surtout en cas de division par zéro ou syntaxe incorrecte), afficher "NG"
        print("NG")