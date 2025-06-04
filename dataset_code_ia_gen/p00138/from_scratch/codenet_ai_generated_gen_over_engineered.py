from dataclasses import dataclass
from typing import List, Tuple, Callable


@dataclass(frozen=True)
class Athlete:
    number: int
    time: float


class Heat:
    def __init__(self, athletes: List[Athlete]):
        if len(athletes) != 8:
            raise ValueError("Each heat must have exactly 8 athletes.")
        self.athletes = athletes
        self._ranked = sorted(self.athletes, key=lambda a: a.time)

    def top_two(self) -> List[Athlete]:
        return self._ranked[:2]

    def others(self) -> List[Athlete]:
        return self._ranked[2:]


class SemiFinals:
    def __init__(self, heats: List[Heat]):
        if len(heats) != 3:
            raise ValueError("There must be exactly 3 heats in the semifinals.")
        self.heats = heats

    def advancing_athletes(self) -> List[Athlete]:
        # Top 2 from each heat
        direct_qualifiers = [athlete for heat in self.heats for athlete in heat.top_two()]
        # Collect all others from each heat
        others = [athlete for heat in self.heats for athlete in heat.others()]
        # Sort the "others" by time for wild cards
        others_sorted = sorted(others, key=lambda a: a.time)
        wild_cards = others_sorted[:2]
        return direct_qualifiers + wild_cards

    def results_ordered(self) -> List[Athlete]:
        # According to output order described:
        result = []
        # Add 1st and 2nd from each heat
        for heat in self.heats:
            result.extend(heat.top_two())
        # Then add 2 wild cards from others
        others = [athlete for heat in self.heats for athlete in heat.others()]
        others_sorted = sorted(others, key=lambda a: a.time)
        result.extend(others_sorted[:2])
        return result


class InputParser:
    def __init__(
        self,
        input_provider: Callable[[], str],
        lines_required: int = 24,
        athletes_per_heat: int = 8,
    ):
        self.input_provider = input_provider
        self.lines_required = lines_required
        self.athletes_per_heat = athletes_per_heat

    def parse(self) -> SemiFinals:
        raw_lines = [self.input_provider() for _ in range(self.lines_required)]
        if len(raw_lines) != self.lines_required:
            raise ValueError("Not enough input lines.")
        athletes: List[Athlete] = []
        for line in raw_lines:
            p_str, t_str = line.strip().split()
            p = int(p_str)
            t = float(t_str)
            athletes.append(Athlete(p, t))
        heats = [
            Heat(athletes[i : i + self.athletes_per_heat])
            for i in range(0, self.lines_required, self.athletes_per_heat)
        ]
        return SemiFinals(heats)


def main():
    import sys

    parser = InputParser(input_provider=sys.stdin.readline)
    semifinals = parser.parse()
    finalists = semifinals.results_ordered()
    for athlete in finalists:
        print(athlete.number, f"{athlete.time:.2f}")


if __name__ == "__main__":
    main()