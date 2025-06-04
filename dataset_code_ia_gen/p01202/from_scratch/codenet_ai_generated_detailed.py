# Solution au problème Dance Dance Revolution
# On doit déterminer si une séquence d'arrows est "naturelle" selon les règles données.
# Conditions:
# 1) Les pas alternent entre pied gauche et pied droit.
# 2) Le même panneau ne peut pas être pressé deux fois de suite.
# 3 & 4) Sans tourner le haut du corps ni croiser les jambes:
#     - Les positions des pieds ont une relation d'ordre selon la disposition L < U,D < R,
#       ce qui empêche de croiser jambes ou tourner le corps.
# Approche:
# - On modélise l'état par la position du pied gauche et du pied droit.
# - On essaie d'appuyer chaque flèche avec un pied alterné.
# - Pour chaque étape, on teste toutes les combinaisons possibles d'état compatibles.
# - On utilise un codage efficace avec sets pour gérer jusqu'à 100 000 caractères.
# - Si on peut avancer jusqu'à la fin, on retourne "Yes", sinon "No".

import sys

def is_natural(score: str) -> str:
    # Map panels to indices pour faciliter les comparaisons
    # Ordre logique: L < U < D < R (U et D se considèrent égaux côte à côte)
    order_map = {'L': 0, 'U': 1, 'D': 1, 'R': 2}

    n = len(score)
    # Pied gauche (L), pied droit (R) initialement sur rien (-1)
    # On représente les états par un tuple (pos_gauche, pos_droit)
    # positions: 0-3 pour panels, -1 pour "aucun pied dessus encore" au départ
    # Cependant on commence directement à la première flèche.
    # Initialement les pieds peuvent être n'importe où (on peut assumer qu'ils démarent libres).

    # Pour respecter la règle d'interdiction "même panneau deux fois consécutives" et alternance
    # On doit considérer quelle jambe doit marcher (pied gauche ou pied droit)
    # Les pas commencent avec le pied gauche.

    # On encode les panels en 0..3
    panel_to_num = {'L':0,'U':1,'D':2,'R':3}

    # On définit une fonction qui vérifie si les jambes ne se croisent pas et corps reste face avant
    # Règle interprétée comme: la jambe gauche doit toujours être "à gauche" (ordre), jambe droite "à droite"
    # C'est-à-dire: position_gauche < position_droite selon l'ordre étendu.
    # On utilise l'ordre L<U,D<R, donc L=0, U=1, D=1, R=2
    # Pour U et D on met 1, ils se valent.
    def order_panel(p):
        if p=='L': return 0
        if p=='U' or p=='D': return 1
        return 2

    # Initialisation de l'ensemble des états possibles
    # Un état = (pos_gauche, pos_droite)
    # Au départ on n'a pas les pieds sur une flèche (on peut considérer qu'ils sont au repos hors des panels)
    # Pour démarrage, on peut considérer que les pieds sont 'hors de l'arène', par exemple -1
    # Mais il est plus simple d'initialiser avec le pied gauche appuyant sur la première flèche.
    # En fait le premier pas est sur la première flèche, forcément pied gauche, donc
    # Les pieds commencent avec gauche sur score[0], droite sur "rien" (-1)
    # On représentera l'absence de pied sur un panneau par -1

    # Les panneaux sont codés en 0..3:
    first_panel = panel_to_num[score[0]]
    
    # Les états sont stockés dans un set pour éviter doublons.
    # Au départ, pied gauche sur première flèche, pied droit n'a pas bougé
    states = set()
    states.add( (first_panel, -1) )  # (pos_gauche, pos_droite)
    
    # On va parcourir la séquence à partir de la seconde flèche,
    # en alternant le pied qui appuie: 0 -> gauche, 1 -> droite, 2 -> gauche, etc.
    # On commence à i=1, pied droit doit appuyer (i est la position dans la chaîne)
    for i in range(1,n):
        current_panel = panel_to_num[score[i]]
        new_states = set()
        foot = i % 2  # 0 = gauche, 1 = droite

        for (lg, ld) in states:
            if foot == 0:
                # Pied gauche doit appuyer sur current_panel
                # Conditions:
                # - On ne peut pas appuyer deux fois de suite sur même panneau pour un pied (condition 2)
                #   ici on vérifie pour pied gauche: donc current_panel != lg
                if current_panel == lg:
                    continue
                # - Pied gauche et pied droit ne peuvent pas être sur le même panneau (pas interdit explicitement mais c'est implicite car deux pieds sur même panneau impossible)
                if current_panel == ld:
                    continue
                # - Le corps doit rester face avant et jambes sans croiser
                # order_panel(pied gauche) < order_panel(pied droit)
                # pieds sur (current_panel, ld)
                # ld peut être -1 (pas encore posé), alors pas de problème
                if ld != -1:
                    if order_panel(score[i]) >= order_panel(score[ld]):
                        continue
                # ok, on ajoute le nouvel état
                new_states.add((current_panel, ld))
            else:
                # Pied droit appuie sur current_panel
                if current_panel == ld:
                    continue
                if current_panel == lg:
                    continue
                if lg != -1:
                    # pied gauche et pied droit doivent respecter l'ordre:
                    # order_panel(lg) < order_panel(current_panel)
                    if order_panel(score[lg]) >= order_panel(score[i]):
                        continue
                new_states.add((lg, current_panel))

        if not new_states:
            return "No"
        states = new_states

    return "Yes"



def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        score = input().strip()
        print(is_natural(score))

if __name__ == "__main__":
    main()