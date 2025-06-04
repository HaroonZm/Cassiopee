from typing import List, Tuple, Iterable


class Macronutrient:
    PROTEIN = 'protein'
    FAT = 'fat'
    CARBOHYDRATE = 'carbohydrate'

    _calorie_map = {
        PROTEIN: 4,
        FAT: 9,
        CARBOHYDRATE: 4
    }

    @classmethod
    def calorie_per_gram(cls, nutrient: str) -> int:
        return cls._calorie_map[nutrient]


class NutrientProfile:
    def __init__(self, protein: int, fat: int, carbohydrate: int):
        self._amounts = {
            Macronutrient.PROTEIN: protein,
            Macronutrient.FAT: fat,
            Macronutrient.CARBOHYDRATE: carbohydrate,
        }

    def amount(self, nutrient: str) -> int:
        return self._amounts[nutrient]

    def calories(self) -> int:
        return sum(
            self._amounts[nutrient] * Macronutrient.calorie_per_gram(nutrient)
            for nutrient in self._amounts
        )

    def exceeds(self, other: 'NutrientProfile') -> bool:
        return any(
            self._amounts[nutrient] > other._amounts[nutrient]
            for nutrient in self._amounts
        )


class Snack:
    def __init__(self, id_: int, nutrient_profile: NutrientProfile):
        self.id = id_
        self.nutrient_profile = nutrient_profile
        self.calories = nutrient_profile.calories()

    def is_within_limits(self, nutrient_limit: NutrientProfile, calorie_limit: int) -> bool:
        if self.nutrient_profile.exceeds(nutrient_limit):
            return False
        if self.calories > calorie_limit:
            return False
        return True


class NutrientLimits(NutrientProfile):
    # Inherits from NutrientProfile to use same interface
    pass


class SnackCollection:
    def __init__(self, snacks: List[Snack]):
        self.snacks = snacks

    def filter_allowed(self, limits: NutrientLimits, calorie_limit: int) -> List[int]:
        allowed = []
        for snack in self.snacks:
            if snack.is_within_limits(limits, calorie_limit):
                allowed.append(snack.id)
        return allowed


class InputParser:
    def __init__(self, input_lines: Iterable[str]):
        self.lines = iter(input_lines)

    def parse_dataset(self) -> Tuple[SnackCollection, NutrientLimits, int]:
        try:
            n_line = next(self.lines).strip()
        except StopIteration:
            return None  # No more datasets

        if n_line == '0':
            return None  # End of all datasets

        n = int(n_line)
        snacks = []
        for _ in range(n):
            line = next(self.lines).strip()
            s, p, q, r = map(int, line.split())
            nutrient_profile = NutrientProfile(p, q, r)
            snack = Snack(s, nutrient_profile)
            snacks.append(snack)
        limit_line = next(self.lines).strip()
        P, Q, R, C = map(int, limit_line.split())
        nutrient_limits = NutrientLimits(P, Q, R)
        calorie_limit = C
        return SnackCollection(snacks), nutrient_limits, calorie_limit

    def datasets(self) -> Iterable[Tuple[SnackCollection, NutrientLimits, int]]:
        while True:
            parsed = self.parse_dataset()
            if parsed is None:
                break
            yield parsed


class OutputFormatter:
    @staticmethod
    def format_allowed(allowed_ids: List[int]) -> str:
        if not allowed_ids:
            return "NA"
        return '\n'.join(str(id_) for id_ in allowed_ids)


def main():
    import sys
    parser = InputParser(sys.stdin)
    for snack_collection, nutrient_limits, calorie_limit in parser.datasets():
        allowed = snack_collection.filter_allowed(nutrient_limits, calorie_limit)
        print(OutputFormatter.format_allowed(allowed))


if __name__ == "__main__":
    main()