# Solution complète au problème du slot machine décrit
# Le programme lit plusieurs datasets, calcule le nombre de médailles restantes
# après une session de jeu, et affiche ce nombre par dataset.
# Les jeux incluent des jeux normaux et des bonus avec différentes règles.

def calculate_medals(b, r, g, c, s, t):
    # b: nombre de Big Bonus
    # r: nombre de Regular Bonus
    # g: nombre de fois où le raisin (ブドウ) a aligné en jeu normal
    # c: nombre de fois où la cerise a aligné (non impacté par la médaille)
    # s: nombre de jeux normaux joués
    # t: nombre total de jeux (normaux + bonus)

    # Médailles initiales
    medals = 100

    # Analyse des coûts et gains

    # 1) Jeux normaux (s jeux)
    # Coût par jeu normal : 3 médailles
    medals -= 3 * s

    # Chaque raisin aligné donne 15 médailles en jeu normal
    medals += 15 * g

    # Chaque cerise alignée ne rapporte pas de médailles, elle est ignorée

    # 2) Jeux bonus (t - s jeux)
    # Le total des jeux bonus = t - s
    games_bonus = t - s

    # Chaque big bonus octroie 5 jeux bonus
    # Chaque regular bonus octroie 3 jeux bonus
    # Vérification que le total correspond bien: (5 * b + 3 * r) == games_bonus
    # Cette vérification n'est pas nécessaire pour le calcul, on suppose cohérent

    # Coût par jeu bonus : 2 médailles
    medals -= 2 * games_bonus

    # Chaque jeu bonus rapporte 15 médailles (car raisin toujours aligné)
    medals += 15 * games_bonus

    # 3) Jeux gratuits (スター(triple étoiles)) s'ajoutent aux jeux normaux
    # Ils ne coûtent pas de médailles, ni ne rapportent
    # Le nombre de jeux gratuits est c (nombre de triple étoiles aligné)

    # Donc pas de modification pour c dans le calcul des médailles

    return medals


def main():
    import sys

    for line in sys.stdin:
        # Lecture des données, suppression d'espaces inutiles
        line = line.strip()
        if line == '':
            continue
        # Conversion des données en entiers
        b, r, g, c, s, t = map(int, line.split())
        # Si données toutes à zéro, fin de traitement
        if b == 0 and r == 0 and g == 0 and c == 0 and s == 0 and t == 0:
            break
        # Calcul et affichage du résultat
        result = calculate_medals(b, r, g, c, s, t)
        print(result)


if __name__ == "__main__":
    main()