class EnergyDrink:
    def __init__(self, index: int, climb: int, slide: int):
        self.index = index
        self.climb = climb
        self.slide = slide
        self.net_gain = climb - slide

    def __repr__(self):
        return f"EnergyDrink(idx={self.index}, climb={self.climb}, slide={self.slide}, net={self.net_gain})"

class Sinner:
    def __init__(self, climb_per_night: int):
        self.climb_per_night = climb_per_night

class EscapeFromHell:
    def __init__(self, N: int, L: int, energy_drinks: list, sinners: list):
        self.N = N
        self.L = L
        self.energy_drinks = energy_drinks
        self.sinners = sinners
        self.best_order = []
        self.earliest_escape_day = -1

    def _preprocess_and_sort_drinks(self):
        # Sophisticated sorting logic anticipating future criteria
        # Sort by net gain descending primarily, then by climb descending
        self.energy_drinks.sort(
            key=lambda d: (d.net_gain, d.climb),
            reverse=True
        )

    def _simulate_escape(self):
        position = 0  # The current height of the worker on silk
        sinners_positions = [0] * self.N  # track sinners positions per night
        max_sinner_height = 0

        for day in range(self.N):
            drink = self.energy_drinks[day]

            # Daytime climb
            position += drink.climb

            # Check if escaped before sliding down
            if position >= self.L:
                # Check if no sinner catch
                # Sinners climb after daytime, so check sinners' height before next night
                # Because conflict occurs if sinners catch him at any time
                # All previous sinners positions except current day (which hasn't climbed yet)
                max_sinner_height = max(sinner.climb_per_night * day for sinner in self.sinners)

                if position > max_sinner_height:
                    self.earliest_escape_day = day + 1
                    return

            # Nighttime slide
            position -= drink.slide
            if position < 0:
                position = 0

            # After worker slides, sinners climb this night
            sinners_positions[day] = self.sinners[day].climb_per_night * (day + 1)
            max_sinner_height = max(max_sinner_height, sinners_positions[day])

            # If sinners catch up or exceed worker position
            if max_sinner_height >= position:
                # Silk cuts now, no further progress
                break

    def compute_earliest_escape_day(self):
        self._preprocess_and_sort_drinks()
        self._simulate_escape()
        return self.earliest_escape_day

def main():
    import sys
    input = sys.stdin.readline

    N, L = map(int, input().split())
    energy_drinks = []
    for i in range(N):
        A, B = map(int, input().split())
        energy_drinks.append(EnergyDrink(i, A, B))
    sinners = []
    for _ in range(N):
        C = int(input())
        sinners.append(Sinner(C))

    escape = EscapeFromHell(N, L, energy_drinks, sinners)
    result = escape.compute_earliest_escape_day()
    print(result)

if __name__ == "__main__":
    main()