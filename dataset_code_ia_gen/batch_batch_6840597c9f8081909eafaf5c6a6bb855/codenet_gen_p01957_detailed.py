import sys
sys.setrecursionlimit(10**7)

# Parser pour le tournoi selon la BNF donnée
# <winner> ::= <person> | "[" <winner> "-" <winner> "]"
# <person> ::= "a" | ... | "z"

class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.n = len(s)

    def parse_winner(self):
        # soit un personnage simple (une lettre)
        # soit un match avec format: [<winner>-<winner>]
        if self.pos >= self.n:
            raise ValueError("Unexpected end of input")

        ch = self.s[self.pos]
        if ch.isalpha():
            # personnage simple
            self.pos += 1
            return ch
        elif ch == '[':
            # match
            self.pos += 1  # consommer '['
            left = self.parse_winner()
            if self.pos >= self.n or self.s[self.pos] != '-':
                raise ValueError("Expected '-' in match")
            self.pos += 1  # consommer '-'
            right = self.parse_winner()
            if self.pos >= self.n or self.s[self.pos] != ']':
                raise ValueError("Expected ']' at end of match")
            self.pos += 1  # consommer ']'
            return [left, right]
        else:
            raise ValueError(f"Unexpected character {ch}")

# Calcul des victoires possibles selon l'arbre de tournoi donné.
# L'idée :
#   À chaque match, un seul des deux vient vainqueur et gagne 1 victoire.
#   On cherche une affectation des vainqueurs des sous-matches compatibles avec 
#   les comptes donnés.
#
# Cette fonction va compter les victoires qu'on peut attribuer et vérifier si les
# contraintes sont satisfaites.

# On modélise le problème par un DFS qui:
#   - pour une feuille (personnage simple), retourne la liste des victoires possibles:
#     c'est fixe : aucun match gagné dans cette "feuille", donc victoires 0
#   - pour un match (deux sous-arbres), on cherche des combinaisons de victoires combinées
#     sous contrainte : le vainqueur du match gagne +1 victoire, l'autre rien.
#
# Finalement, on doit vérifier le vecteur des victoires qu'on obtient globalement
# correspond exactement aux données v_i fournies.
#
# Pour résoudre ça on:
#   - Calcule toutes les combinaisons possibles des victoires réalisables dans l'arbre
#
# Vu que N <= 26 et chaque victoire <= 26, la recherche avec mémo est possible.

def get_all_scores(node):
    """
    Retourne un dict:
       clé: dict{personne: nombre_victoires}
       valeur: nombre d'affectations réalisant ce score
       
    Pour un noeud donné, on calcule toutes les affectations de victoires compatibles.
    """

    # cas feuille
    if isinstance(node, str):
        # seule affectation possible : 0 victoire pour ce joueur
        return { (node, 0): 1 }

    # cas match [left - right]
    left, right = node

    # Obtenir toutes les scores possibles à gauche et à droite
    left_scores = get_all_scores(left)
    right_scores = get_all_scores(right)

    combined = {}

    # Pour chaque score possible à gauche : dict (personne, victoire) avec occurrence
    # même chose à droite
    # à ce niveau:
    #   On fait un match entre les gagnants des deux groupes
    #
    # La victoire finale est attribuée au vainqueur du match (gagnant de gauche ou gagnant de droite)
    #   => Il faut choisir soit un membre dans left qui gagne ce match, ou un membre dans right.
    #
    # Mais left_score et right_score décrivent un dict per player des victoires
    # Comme joueur sont disjoints (unique dans chaque sous-arbre), on peut fusionner
    #
    # Le problème est qu'on ne connaît pas le vainqueur du match.
    #
    # Idea:
    # Pour chaque affectation gauche possible, et chaque affectation droite possible,
    # on peut choisir le vainqueur dans le groupe gauche OU dans le groupe droite.
    #
    # Le vainqueur prend +1 victoire.
    #
    # Tous les joueurs des sous-groupes gardent leur victoires
    #
    # Il faut donc, pour chaque possible vainqueur dans left,
    # construire un nouveau score qui ajoute 1 victoire au vainqueur, fusionne victoires,
    # idem pour chaque vainqueur dans right.
    #
    # Le nombre d’affectations possibles est somme des occurrences pour chaque cas

    # Pour faciliter la fusion, 
    # transform keys from (person, v) to dict{person:v}
    def scores_dict_to_map(scores):
        res = []
        for (p,v), count in scores.items():
            res.append( (p,v,count) )
        return res

    left_list = scores_dict_to_map(left_scores)
    right_list = scores_dict_to_map(right_scores)

    # players sets in left and right
    # Pour optimiser, on peut regrouper players à gauche et droite
    # mais on peut gérer ça simplement, car les joueurs sont disjoints

    # La clé est une frozenset de (personne,victoire) pour tout joueurs

    from collections import defaultdict

    # Pour faciliter, reconstruire les scores sous forme de dict de joueur->victoire
    def combine_scores(l_ps, r_ps, winner_in_left):
        # winner_in_left : bool, si True, vainqueur dans left, sinon dans right
        # Retourne dictionnaire clé={person:victoire}, et le count d'affectations.

        # on va parcourir tous les joueurs dans l_ps et r_ps
        # l_ps = (p,v,count)
        # Ici on a un seul joueur car à la feuille on a un tuple (p,v,count)
        # MAIS à la racine on veut les dictionnaires agrégées pour tous les joueurs du sous-arbre

        # Correction : en réalité left_scores et right_scores map de (person,vict) à count, i.e.
        # une liste de "états" mais en fait chaque état est un seul joueur car feuille.
        # Ici on reconstruira progressivement des dict de joueurs.
        # En fait l_calc et r_calc sont des feuilles initialement, puis en remontant c'est des dicts.

        # C'est la complexité: la structure est récursive, on doit retourner pour chaque noeud
        # une liste de dicts: combinaisons possibles totales du sous arbre.

        # Donc au lieu de manipuler des tuple simples, on va étudier le code en modifiant l'approche.

        pass

    # Pour simplifier, on va changer la conception:
    #
    # Dans get_all_scores, on retourne une liste de (score_dict, count)
    # Où score_dict est dict {joueur:int wins}
    #
    # Cas feuille : on retourne [{joueur:0}, 1]
    #
    # Cas noeud (left, right):
    #   - récupère list de (score_dict), count pour left et right
    #   - Pour chaque (sl, cl) dans left, (sr, cr) dans right:
    #       - Soit vainqueur dans sl: on incrémente victoire d'un joueur de sl de 1
    #       - Soit vainqueur dans sr: idem dans sr
    #     Chaque possibilité ajoute une entrée (fusion des score_dict + victorieux+1) avec count=cl*cr
    #
    #   - On regroupe et on renvoie la liste

    # Réécriture complète pour ce comportement:

def merge_dicts(d1, d2):
    """Fusionne deux dicts à clés disjointes en un seul"""
    d = d1.copy()
    d.update(d2)
    return d

def get_all_scores_v2(node):
    if isinstance(node, str):
        # Feuille: unique dict de victoire {node:0}
        return [ ({node:0}, 1) ]

    left, right = node
    left_results = get_all_scores_v2(left)   # liste de (score_dict, count)
    right_results = get_all_scores_v2(right)

    combined_dict = {}

    # À chaque combinaison possible des scores gauche et droite,
    # on attribue la victoire du match à un joueur gauche OU droite
    # On itère tous les joueurs gauche et droite pour attribuer cette victoire

    for (l_score, l_count) in left_results:
        for (r_score, r_count) in right_results:
            # candidats vainqueurs = tous joueurs de l_score + tous joueurs de r_score
            players_left = list(l_score.keys())
            players_right = list(r_score.keys())
            for winner in players_left:
                # Le vainqueur est winner dans left
                # On ajoute +1 victoire à winner
                new_score = merge_dicts(l_score, r_score)
                new_score = new_score.copy()
                new_score[winner] += 1
                # On stocke en clé frozenset des paires (person,victoire)
                key = frozenset(new_score.items())
                combined_dict[key] = combined_dict.get(key, 0) + l_count * r_count

            for winner in players_right:
                # Vainqueur dans right
                new_score = merge_dicts(l_score, r_score)
                new_score = new_score.copy()
                new_score[winner] += 1
                key = frozenset(new_score.items())
                combined_dict[key] = combined_dict.get(key, 0) + l_count * r_count

    # Convertir combined_dict en liste de (score_dict, count)
    result = []
    for key, c in combined_dict.items():
        d = dict(key)
        result.append( (d, c) )
    return result

def main():
    S = sys.stdin.readline().strip()
    parser = Parser(S)
    root = parser.parse_winner()
    if parser.pos != len(S):
        print("No")
        return

    # identifier les joueurs du tournoi (feuilles)
    # On peut déduire directement du parsing ou en parcourant l'arbre

    # but on reçoit N lignes avec joueur/victoire
    # on les stocke dans dict

    scores_query = {}
    lines = sys.stdin.read().strip().split('\n')
    for l in lines:
        if not l.strip():
            continue
        p, v = l.split()
        scores_query[p] = int(v)

    # calculer toutes les affectations possibles des victoires selon l'arbre
    possibilities = get_all_scores_v2(root)

    # vérifier si au moins un est égal à scores_query

    # Normaliser la clé pour comparaison : frozenset de (player, wins)
    target_key = frozenset(scores_query.items())

    for (score_dict, count) in possibilities:
        # Vérifier que score_dict correspond exactement à scores_query
        # 1) même clé set
        # 2) même valeur pour chaque
        if frozenset(score_dict.items()) == target_key:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    main()