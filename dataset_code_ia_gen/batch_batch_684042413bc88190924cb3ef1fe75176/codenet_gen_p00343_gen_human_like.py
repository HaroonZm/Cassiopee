import sys
sys.setrecursionlimit(10**7)

def can_place(card, table):
    # On peut poser si card est contigu à une carte sur table (card-1 ou card+1)
    return (card - 1 in table) or (card + 1 in table)

def dfs(table, p_hand, o_hand, memo):
    # table: ensemble des cartes sur la table
    # p_hand: tuple des cartes du joueur p (le joueur dont c'est le tour)
    # o_hand: tuple des cartes de l'autre joueur
    # memo: dictionnaire pour mémoriser les états déjà calculés
    key = (tuple(sorted(table)), tuple(sorted(p_hand)), tuple(sorted(o_hand)))
    if key in memo:
        return memo[key]
    # Si joueur p n'a plus de cartes: il a gagné
    if len(p_hand) == 0:
        memo[key] = True
        return True
    # Chercher les cartes que p peut poser (doit poser si possible)
    playable = [c for c in p_hand if can_place(c, table)]
    if playable:
        # p doit poser un de ces cartes
        # p gagne si y a au moins un choix qui mène à sa victoire, quel que soit ce que fait l'adversaire ensuite
        for c in playable:
            new_table = table | {c}
            new_p_hand = tuple(x for x in p_hand if x != c)
            # Après que p ait joué, c'est au tour de o. Intervertir les rôles et mains
            # Pour p gagner, il faut que, pour tout choix de o, p puisse contrer
            res = dfs_after_opponent_turn(new_table, new_p_hand, o_hand, memo)
            if res:
                memo[key] = True
                return True
        memo[key] = False
        return False
    else:
        # p ne peut pas poser, on passe à o
        res = dfs_after_opponent_turn(table, p_hand, o_hand, memo)
        memo[key] = res
        return res

def dfs_after_opponent_turn(table, p_hand, o_hand, memo):
    # Tour de o (adversaire)
    # o essaie tout pour empêcher p de gagner
    playable_o = [c for c in o_hand if can_place(c, table)]
    if playable_o:
        # o peut jouer plusieurs cartes, il va jouer celle qui minimise chance de p de gagner
        # donc on doit tester tous les coups de o; p doit gagner quelle que soit la réponse de o
        for c in playable_o:
            new_table = table | {c}
            new_o_hand = tuple(x for x in o_hand if x != c)
            # Ensuite c'est de nouveau au tour de p
            res = dfs(new_table, p_hand, new_o_hand, memo)
            if not res:
                # Il existe un coup de o empêchant p de gagner
                return False
        # p gagne quel que soit le coup de o
        return True
    else:
        # o ne peut pas jouer, c'est à p de jouer
        return dfs(table, p_hand, o_hand, memo)

def main():
    input = sys.stdin.readline
    N = int(input())
    full_cards = set(range(1,14))
    full_cards.remove(7)
    for _ in range(N):
        p_cards = list(map(int, input().split()))
        p_set = set(p_cards)
        o_set = full_cards - p_set
        table = {7}
        memo = {}
        # Premier joueur est p (先手), avec p_set
        # On cherche si p a un chemin gagnant quel que soit ce que fait o (後手)
        if dfs(table, tuple(sorted(p_set)), tuple(sorted(o_set)), memo):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()