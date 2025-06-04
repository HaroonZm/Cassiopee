from decimal import Decimal, getcontext

def compute_value(n, k, m, r):
    """
    Calcule la valeur selon les paramètres donnés.
    
    Args:
        n (int): Le diviseur principal.
        k (int): Paramètre inutilisé mais inclus pour compatibilité.
        m (int): Indicateur pour le calcul supplémentaire.
        r (int): Précision désirée pour l'affichage du résultat.

    Returns:
        str: Représentation formatée de la valeur calculée, à r décimales.
    """
    # Crée un objet Decimal avec la valeur 1 pour assurer la précision
    d1 = Decimal(1)
    # Définit la précision globale du contexte Decimal à r+1 chiffres
    getcontext().prec = r + 1
    # Calcule la valeur de base : 1/n sous forme de Decimal
    ans = d1 / Decimal(n)
    # Si m est différent de 0, ajoute le terme supplémentaire
    if m:
        # Somme des inverses de 1 à n-1, ajoutée à 1, multipliée à la base
        ans *= 1 + sum(d1 / Decimal(i) for i in range(1, n))
    # Formate la réponse avec r+1 chiffres après la virgule, puis retire le dernier chiffre
    formatted = '{{:.{}f}}'.format(r + 1).format(ans)[:-1]
    return formatted

def main():
    """
    Boucle principale pour la saisie et le traitement des requêtes.
    S'arrête lorsque n vaut 0.
    """
    while True:
        # Lit l'entrée, attend quatre entiers séparés par des espaces
        n, k, m, r = map(int, input().split())
        # Condition de sortie : si n est 0, la boucle s'arrête
        if not n:
            break
        # Calcule et affiche le résultat formaté
        print(compute_value(n, k, m, r))

if __name__ == "__main__":
    main()