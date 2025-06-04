from decimal import Decimal, Context, ROUND_HALF_UP, setcontext

def calculate_probability(n: int, k: int, m: int, r: int) -> str:
    """
    Calcule la probabilité selon les paramètres donnés et renvoie le résultat 
    comme une chaîne de caractères formatée à la précision demandée.

    Paramètres:
    n (int): Le nombre total de cartes.
    k (int): (Inutilisé dans le calcul, paramètre existant pour compatibilité)
    m (int): Le mode de calcul de la probabilité.
    r (int): Le nombre de décimales à afficher.

    Retourne:
    str: La probabilité calculée formatée avec exactement (r+1) décimales après la virgule.
    """
    # Définir le contexte de précision pour les calculs décimaux
    setcontext(Context(prec=r, rounding=ROUND_HALF_UP))
    one = Decimal(1)

    # Probabilité de base : 1 divisé par le nombre de cartes
    ans = one / Decimal(n)

    # Si le mode m est 1, on effectue un calcul supplémentaire
    if m == 1:
        s = 0
        # Calcule la somme des inverse des n-1 premiers entiers
        for i in range(1, n):
            s += one / Decimal(i)
        # Ajustement de la probabilité selon la sommation
        ans *= 1 + s

    # Convertir le résultat en chaîne pour limiter le nombre de décimales
    ans_str = str(ans)[:r + 2]
    # Ajouter les zéros manquants si la chaîne est plus courte que requis
    if len(ans_str) < r + 2:
        ans_str += '0' * (r + 2 - len(ans_str))
    return ans_str

def main():
    """
    Fonction principale. Lit les paramètres en entrée, puis calcule et affiche la probabilité
    jusqu'à ce qu'une ligne d'entrée commençant par zéro soit rencontrée.
    """
    while True:
        # Lire les quatre paramètres de la ligne d'entrée
        n, k, m, r = map(int, input().split())
        # Condition de sortie : n == 0
        if n == 0:
            break
        # Calculer et afficher le résultat formaté
        result = calculate_probability(n, k, m, r)
        print(result)

# Démarrer le programme si exécuté directement
if __name__ == "__main__":
    main()