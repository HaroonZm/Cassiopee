from abc import ABC, abstractmethod
from typing import Tuple, Optional, Dict

class PlayerId:
    ISONO = 0
    NAKAJIMA = 1

class HandPosition:
    LEFT = 0
    RIGHT = 1

class HandState:
    """Représente les doigts levés sur une main. 0 signifie main disparue."""
    def __init__(self, fingers: int):
        self.fingers = fingers

    def is_active(self) -> bool:
        return self.fingers > 0

    def clone(self) -> 'HandState':
        return HandState(self.fingers)

    def __hash__(self):
        return hash(self.fingers)

    def __eq__(self, other):
        return isinstance(other, HandState) and self.fingers == other.fingers

class PlayerState:
    """État des deux mains d’un joueur."""
    def __init__(self, left: HandState, right: HandState):
        self.left = left
        self.right = right

    def is_defeated(self) -> bool:
        return not (self.left.is_active() or self.right.is_active())

    def active_hands(self):
        hands = []
        if self.left.is_active():
            hands.append(HandPosition.LEFT)
        if self.right.is_active():
            hands.append(HandPosition.RIGHT)
        return hands

    def hand_fingers(self, hand_pos: int) -> int:
        return self.left.fingers if hand_pos == HandPosition.LEFT else self.right.fingers

    def clone(self) -> 'PlayerState':
        return PlayerState(self.left.clone(), self.right.clone())

    def __hash__(self):
        return hash((self.left, self.right))

    def __eq__(self, other):
        return isinstance(other, PlayerState) and self.left == other.left and self.right == other.right

class GameState:
    """État complet du jeu, avec mémorisation pour recherche optimale."""
    def __init__(self, player_states: Tuple[PlayerState, PlayerState], turn: int):
        self.player_states = player_states  # (isono, nakajima)
        self.turn = turn  # 0 ou 1 : joueur courant
        self._hash = None

    def is_finished(self) -> bool:
        # Vérifie si un joueur est défait (deux mains disparues)
        return any(player.is_defeated() for player in self.player_states)

    def winner(self) -> Optional[int]:
        # Retourne le gagnant si fini, sinon None
        isono_defeat = self.player_states[PlayerId.ISONO].is_defeated()
        nakajima_defeat = self.player_states[PlayerId.NAKAJIMA].is_defeated()
        if isono_defeat and nakajima_defeat:
            return None  # égalité impossible d'après l'énoncé
        if isono_defeat:
            return PlayerId.NAKAJIMA
        if nakajima_defeat:
            return PlayerId.ISONO
        return None

    def possible_moves(self) -> Tuple[Tuple[int,int,int,int], ...]:
        # Génère les coups possibles (attache main_joueur_courant -> main_adversaire)
        current = self.player_states[self.turn]
        opponent = self.player_states[1 - self.turn]
        moves = []
        for attacker_hand in current.active_hands():
            attacker_fingers = current.hand_fingers(attacker_hand)
            for defender_hand in opponent.active_hands():
                defender_fingers = opponent.hand_fingers(defender_hand)
                # coup : (main_courant, doights_courant, main_adversaire, doigts_adversaire)
                # Mais on stocke simplement les mains (attaquants, défenseurs)
                moves.append( (attacker_hand, defender_hand) )
        return tuple(moves)

    def apply_move(self, move: Tuple[int,int]) -> 'GameState':
        # Applique un coup et retourne un nouvel état
        attacker_hand, defender_hand = move
        new_player_states = [self.player_states[0].clone(), self.player_states[1].clone()]
        attacker = new_player_states[self.turn]
        defender = new_player_states[1 - self.turn]

        # doigts à ajouter: doigts de la main attaquante
        attack_fingers = attacker.hand_fingers(attacker_hand)
        # doigts actuels défenseur
        defender_fingers = defender.hand_fingers(defender_hand)

        new_fingers = attack_fingers + defender_fingers
        if new_fingers >= 5:
            new_fingers = 0  # main disparait

        # Mise à jour main défenseur
        if defender_hand == HandPosition.LEFT:
            defender.left.fingers = new_fingers
        else:
            defender.right.fingers = new_fingers

        # changement de tour
        return GameState(tuple(new_player_states), 1 - self.turn)

    def __hash__(self):
        if self._hash is None:
            self._hash = hash((self.player_states[0], self.player_states[1], self.turn))
        return self._hash

    def __eq__(self, other):
        return (self.player_states == other.player_states) and (self.turn == other.turn)

class GameSolver:
    """Recherche minimax avec mémo pour déterminer le gagnant."""
    def __init__(self):
        # Memo: {GameState: bool}, True si joueur courant a victoire assurée
        self.memo: Dict[GameState, bool] = {}

    def can_win(self, state: GameState) -> bool:
        if state.is_finished():
            winner = state.winner()
            return winner == state.turn  # joueur courant gagne ?

        if state in self.memo:
            return self.memo[state]

        moves = state.possible_moves()
        # Exploitation minmax:
        # si un coup mène à une position perdante pour l'adversaire (donc gagnante pour le joueur),
        # alors le joueur courant peut gagner
        for move in moves:
            next_state = state.apply_move(move)
            # Si l'adversaire ne peut pas gagner depuis next_state,
            # alors joueur courant peut gagner
            if not self.can_win(next_state):
                self.memo[state] = True
                return True

        # Sinon, joueur courant perd
        self.memo[state] = False
        return False

def main():
    L_i, R_i = map(int, input().split())
    L_n, R_n = map(int, input().split())

    isono_state = PlayerState(HandState(L_i), HandState(R_i))
    nakajima_state = PlayerState(HandState(L_n), HandState(R_n))

    initial_state = GameState((isono_state, nakajima_state), PlayerId.ISONO)
    solver = GameSolver()
    if solver.can_win(initial_state):
        print("ISONO")
    else:
        print("NAKAJIMA")


if __name__ == '__main__':
    main()