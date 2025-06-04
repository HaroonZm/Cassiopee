from abc import ABC, abstractmethod
from typing import List, Tuple

class Participant(ABC):
    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_catch_count(self) -> int:
        pass

class WakasagiParticipant(Participant):
    def __init__(self, participant_id: int, catch_count: int):
        self._participant_id = participant_id
        self._catch_count = catch_count

    def get_id(self) -> int:
        return self._participant_id

    def get_catch_count(self) -> int:
        return self._catch_count

class TournamentInputStrategy(ABC):
    @abstractmethod
    def read_participants(self) -> List[Participant]:
        pass

class ConsoleInputStrategy(TournamentInputStrategy):
    def read_participants(self) -> List[Participant]:
        n = int(input())
        participants: List[Participant] = []
        for _ in range(n):
            line = input().strip()
            # Accept input either as 'a v' or possibly separate lines for extensibility
            if ' ' in line:
                a_str, v_str = line.split()
                a, v = int(a_str), int(v_str)
            else:
                a = int(line)
                v = int(input())
            participants.append(WakasagiParticipant(a, v))
        return participants

class TournamentResultStrategy(ABC):
    @abstractmethod
    def determine_winner(self, participants: List[Participant]) -> Participant:
        pass

class WakasagiWinnerDeterminationStrategy(TournamentResultStrategy):
    def determine_winner(self, participants: List[Participant]) -> Participant:
        # Sort primarily by descending catch count, secondarily by ascending participant id
        sorted_participants = sorted(participants, key=lambda p: (-p.get_catch_count(), p.get_id()))
        return sorted_participants[0]

class OutputStrategy(ABC):
    @abstractmethod
    def output_winner(self, winner: Participant) -> None:
        pass

class ConsoleOutputStrategy(OutputStrategy):
    def output_winner(self, winner: Participant) -> None:
        print(winner.get_id(), winner.get_catch_count())

class WakasagiTournament:
    def __init__(self,
                 input_strategy: TournamentInputStrategy,
                 result_strategy: TournamentResultStrategy,
                 output_strategy: OutputStrategy):
        self._input_strategy = input_strategy
        self._result_strategy = result_strategy
        self._output_strategy = output_strategy

    def execute(self):
        participants = self._input_strategy.read_participants()
        winner = self._result_strategy.determine_winner(participants)
        self._output_strategy.output_winner(winner)

if __name__ == "__main__":
    tournament = WakasagiTournament(
        input_strategy=ConsoleInputStrategy(),
        result_strategy=WakasagiWinnerDeterminationStrategy(),
        output_strategy=ConsoleOutputStrategy(),
    )
    tournament.execute()