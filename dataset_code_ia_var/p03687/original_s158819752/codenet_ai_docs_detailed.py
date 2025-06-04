import sys

def get_alphabet() -> list:
    """
    Retourne une liste contenant les 26 lettres minuscules de l'alphabet anglais.
    
    Returns:
        list: Liste des caractères de 'a' à 'z'.
    """
    return [chr(ord("a") + i) for i in range(26)]

def min_operations_to_unify_string(S: list) -> int:
    """
    Calcule le nombre minimal d'opérations requises pour transformer la chaîne S
    afin qu'elle soit composée d'un seul caractère, en utilisant la règle suivante :
    Lors de chaque opération, pour chaque paire de caractères adjacents, 
    si l'un des deux caractères correspond au caractère ciblé 'c', alors cette position prend la valeur 'c'.

    Args:
        S (list): Liste de caractères représentant la chaîne initiale.

    Returns:
        int: Nombre minimum d'opérations nécessaires pour unifier la chaîne.
    """
    chars = get_alphabet()
    ans = 10**5  # Initialise la réponse à une valeur suffisamment grande pour la minimiser ensuite

    # Parcourt chaque lettre de l'alphabet
    for c in chars:
        if c not in S:
            # Ignore les lettres qui ne sont pas présentes dans la chaîne
            continue
        cnt = 0  # Nombre d'opérations pour la lettre courante
        S_copy = S.copy()  # Travaille sur une copie de la chaîne d'origine

        # Répète jusqu'à ce que tous les caractères restants soient identiques
        while len(set(S_copy)) > 1:
            S_tmp = []  # Contiendra la chaîne transformée lors de cette étape
            # Parcourt la chaîne pour transformer chaque paire adjacente
            for i in range(len(S_copy) - 1):
                if S_copy[i] == c or S_copy[i + 1] == c:
                    S_tmp.append(c)
                else:
                    S_tmp.append(S_copy[i])
            S_copy = S_tmp.copy()  # Met à jour la copie pour l'étape suivante
            cnt += 1  # Incrémente le compteur d'étapes

        ans = min(ans, cnt)  # Met à jour le minimum d'opérations trouvées

    return ans

def main():
    """
    Point d'entrée du script. Lit une chaîne depuis l'entrée standard et affiche
    le minimum d'opérations nécessaires pour unifier la chaîne selon l'algorithme défini.
    """
    # Lecture de la chaîne depuis l'entrée standard avec suppression du retour à la ligne
    S = list(sys.stdin.readline().rstrip())
    # Calcule et affiche la réponse
    print(min_operations_to_unify_string(S))

if __name__ == "__main__":
    main()