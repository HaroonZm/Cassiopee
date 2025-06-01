from typing import List, Optional, Tuple, Iterator
import sys

class Nutrient:
    PROTEIN = "protein"
    FAT = "fat"
    CARBOHYDRATE = "carbohydrate"

class NutrientValue:
    __kcal_per_g = {
        Nutrient.PROTEIN: 4,
        Nutrient.FAT: 9,
        Nutrient.CARBOHYDRATE: 4
    }

    def __init__(self, protein: int, fat: int, carbohydrate: int) -> None:
        self.protein = protein
        self.fat = fat
        self.carbohydrate = carbohydrate

    def kcal(self) -> int:
        return (self.protein * self.__kcal_per_g[Nutrient.PROTEIN] +
                self.fat * self.__kcal_per_g[Nutrient.FAT] +
                self.carbohydrate * self.__kcal_per_g[Nutrient.CARBOHYDRATE])

    def exceeds(self, limit: 'NutrientLimit') -> bool:
        return (self.protein > limit.max_protein or
                self.fat > limit.max_fat or
                self.carbohydrate > limit.max_carbohydrate or
                self.kcal() > limit.max_calorie)

    def __repr__(self) -> str:
        return (f"NutrientValue(protein={self.protein}, fat={self.fat}, "
                f"carbohydrate={self.carbohydrate}, kcal={self.kcal()})")

class NutrientLimit:
    def __init__(self, max_protein: int, max_fat: int, max_carbohydrate: int, max_calorie: int) -> None:
        self.max_protein = max_protein
        self.max_fat = max_fat
        self.max_carbohydrate = max_carbohydrate
        self.max_calorie = max_calorie

    def __repr__(self) -> str:
        return (f"NutrientLimit(max_protein={self.max_protein}, max_fat={self.max_fat}, "
                f"max_carbohydrate={self.max_carbohydrate}, max_calorie={self.max_calorie})")

class Snack:
    def __init__(self, id_: int, nutrient: NutrientValue) -> None:
        self.id = id_
        self.nutrient = nutrient

    def is_acceptable(self, limit: NutrientLimit) -> bool:
        return not self.nutrient.exceeds(limit)

    def __repr__(self) -> str:
        return f"Snack(id={self.id}, {self.nutrient})"

class SnackEvaluator:
    def __init__(self, snacks: List[Snack], limit: NutrientLimit) -> None:
        self.snacks = snacks
        self.limit = limit

    def evaluate(self) -> List[int]:
        valid_snacks_ids = []
        for snack in self.snacks:
            if snack.is_acceptable(self.limit):
                valid_snacks_ids.append(snack.id)
        return valid_snacks_ids if valid_snacks_ids else []

class InputParser:
    def __init__(self, lines: Iterator[str]) -> None:
        self.lines = lines

    def parse_all_datasets(self) -> Iterator[Tuple[List[Snack], NutrientLimit]]:
        while True:
            line = self._next_non_empty_line()
            if line is None:
                break
            n = int(line)
            if n == 0:
                break
            snacks = []
            for _ in range(n):
                snack_line = self._next_non_empty_line()
                if snack_line is None:
                    raise ValueError("Unexpected end of input while reading snack data")
                parts = snack_line.split()
                if len(parts) != 4:
                    raise ValueError(f"Snack data line must have 4 elements, got {len(parts)}: {snack_line}")
                s, p, q, r = map(int, parts)
                nutrient = NutrientValue(p, q, r)
                snack = Snack(s, nutrient)
                snacks.append(snack)
            limit_line = self._next_non_empty_line()
            if limit_line is None:
                raise ValueError("Unexpected end of input while reading limits")
            P, Q, R, C = map(int, limit_line.split())
            limit = NutrientLimit(P, Q, R, C)
            yield (snacks, limit)

    def _next_non_empty_line(self) -> Optional[str]:
        for line in self.lines:
            stripped = line.strip()
            if stripped != "":
                return stripped
        return None

def main() -> None:
    parser = InputParser(iter(sys.stdin))
    for snacks, limit in parser.parse_all_datasets():
        evaluator = SnackEvaluator(snacks, limit)
        acceptable_snacks = evaluator.evaluate()
        if acceptable_snacks:
            for snack_id in acceptable_snacks:
                print(snack_id)
        else:
            print("NA")

if __name__ == "__main__":
    main()