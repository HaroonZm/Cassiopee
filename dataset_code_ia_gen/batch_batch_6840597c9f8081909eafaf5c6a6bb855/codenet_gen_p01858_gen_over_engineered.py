from enum import Enum, auto
from typing import List, Optional, Tuple


class Pose(Enum):
    MAMORU = "mamoru"       # 防御 (Defend)
    TAMERU = "tameru"       # 溜め (Charge)
    KOUGEKIDA = "kougekida" # 攻撃 (Attack)

    @staticmethod
    def from_str(s: str) -> "Pose":
        mapping = {
            "mamoru": Pose.MAMORU,
            "tameru": Pose.TAMERU,
            "kougekida": Pose.KOUGEKIDA,
        }
        if s not in mapping:
            raise ValueError(f"Invalid pose string: {s}")
        return mapping[s]


class Player:
    """Represents a player in the game."""

    def __init__(self, name: str):
        self.name = name
        self.attack_power = 0
        self.current_pose: Optional[Pose] = None

    def set_pose(self, pose: Pose):
        self.current_pose = pose

    def charge(self):
        if self.attack_power < 5:
            self.attack_power += 1

    def reset_attack_power(self):
        self.attack_power = 0


class RoundResult(Enum):
    ONGOING = auto()
    ISONO_WINS = auto()
    NAKAJIMA_WINS = auto()
    DRAW = auto()


class Game:
    def __init__(self, isono_poses: List[Pose], nakajima_poses: List[Pose]):
        self.isono = Player("Isono-kun")
        self.nakajima = Player("Nakajima-kun")
        self.isono_poses = isono_poses
        self.nakajima_poses = nakajima_poses
        self.round_count = len(isono_poses)
        self.winner: Optional[str] = None
        self.winning_round: Optional[int] = None

    def _determine_round_winner(self) -> RoundResult:
        # Abbreviations for clarity
        ip = self.isono.current_pose
        np = self.nakajima.current_pose
        ia = self.isono.attack_power
        na = self.nakajima.attack_power

        # Helper functions
        def is_attack(p: Pose) -> bool:
            return p == Pose.KOUGEKIDA

        def is_charge(p: Pose) -> bool:
            return p == Pose.TAMERU

        def is_defend(p: Pose) -> bool:
            return p == Pose.MAMORU

        # Case: Both attack at attack power 0 -> no decision
        if is_attack(ip) and is_attack(np) and ia == 0 and na == 0:
            return RoundResult.DRAW

        # Case: Check for fouls and attack power zero attacker(s)
        # If one attacks with 0 and other not attack with 0 => other wins
        if is_attack(ip) and ia == 0 and not (is_attack(np) and na == 0):
            return RoundResult.NAKAJIMA_WINS
        if is_attack(np) and na == 0 and not (is_attack(ip) and ia == 0):
            return RoundResult.ISONO_WINS

        # Check simultaneous attacks with attack power > 0
        if is_attack(ip) and is_attack(np):
            if ia > na:
                return RoundResult.ISONO_WINS
            elif ia < na:
                return RoundResult.NAKAJIMA_WINS
            else:
                # Same attack power, no decision
                return RoundResult.DRAW

        # Check if one attacks and other charges
        if is_attack(ip) and is_charge(np):
            return RoundResult.ISONO_WINS
        if is_charge(ip) and is_attack(np):
            return RoundResult.NAKAJIMA_WINS

        # Check defense cases
        # If defender defends and attacker attacks with 5, attacker wins
        if is_defend(ip) and is_attack(np):
            if na == 5:
                return RoundResult.NAKAJIMA_WINS
            else:
                return RoundResult.DRAW  # ≤4 no decision

        if is_attack(ip) and is_defend(np):
            if ia == 5:
                return RoundResult.ISONO_WINS
            else:
                return RoundResult.DRAW  # ≤4 no decision

        # If no conditions above met, no decision this round
        return RoundResult.DRAW

    def _update_attack_power_post_round(self):
        # After the round ends, if player attacked, their attack power resets to 0
        if self.isono.current_pose == Pose.KOUGEKIDA:
            self.isono.reset_attack_power()
        if self.nakajima.current_pose == Pose.KOUGEKIDA:
            self.nakajima.reset_attack_power()

    def _apply_charges(self):
        # Apply charge poses (attack power increment)
        if self.isono.current_pose == Pose.TAMERU:
            self.isono.charge()
        # No change if defense

        if self.nakajima.current_pose == Pose.TAMERU:
            self.nakajima.charge()

    def play(self) -> Tuple[str, Optional[int]]:
        """Play the game, returns winner string and winning round number, or Hikiwake if no winner."""
        for i in range(self.round_count):
            # Set poses for this round
            self.isono.set_pose(self.isono_poses[i])
            self.nakajima.set_pose(self.nakajima_poses[i])

            # Determine winner of this round if no prior winner
            if self.winner is None:
                result = self._determine_round_winner()

                # Apply charges before resetting attack power due to attack at end of round.
                # But charges happen at pose, before attack resets, so order:
                self._apply_charges()

                if result == RoundResult.ISONO_WINS:
                    self.winner = "Isono-kun"
                    self.winning_round = i + 1
                    # Attack power reset for attacking player handled below
                elif result == RoundResult.NAKAJIMA_WINS:
                    self.winner = "Nakajima-kun"
                    self.winning_round = i + 1
                else:
                    # No winner, still must apply resets if any attack took place
                    pass

                # Reset attack powers if attacked
                self._update_attack_power_post_round()

            else:
                # Once winner decided, ignore further poses per specification
                break

        if self.winner is None:
            # No decision after all rounds
            return "Hikiwake-kun", None
        else:
            return self.winner, self.winning_round


def main():
    K = int(input())
    isono_poses = [Pose.from_str(input().strip()) for _ in range(K)]
    nakajima_poses = [Pose.from_str(input().strip()) for _ in range(K)]

    game = Game(isono_poses, nakajima_poses)
    winner, round_num = game.play()

    print(winner)
    # The problem only requires the winner string,
    # but test cases show that winner and round_no may be output together.
    # The problem statement requests only winner string, so omit printing round number.


if __name__ == "__main__":
    main()