from abc import ABC, abstractmethod
from typing import Iterator, List


class AreaSequenceGenerator(ABC):
    """
    抽象クラス：可能なマンション面積のシーケンスを生成する
    """

    @abstractmethod
    def generate(self) -> Iterator[int]:
        """
        可能な面積を昇順で生成するイテレータ
        """
        pass


class FormulaAreaSequenceGenerator(AreaSequenceGenerator):
    """
    公式 2xy + x + y (x,yは正整数) に基づく面積のシーケンスを生成
    生成済みキャッシュにより高速化も視野に入れる設計
    """

    def __init__(self, max_area: int):
        self.max_area = max_area
        self._cache: List[int] = []

    def _generate_all(self) -> List[int]:
        candidates = set()
        # x,y は正整数で、計算結果が max_area 以下となる範囲を探索
        limit = 1
        while True:
            # 左辺 2xy + x + y <= max_area
            # より y <= (max_area - x)/(2x+1)
            # で y >=1 が必要なので続行判定
            if (self.max_area - limit) // (2 * limit + 1) < 1:
                break
            limit += 1
        for x in range(1, limit + 1):
            max_y = (self.max_area - x) // (2 * x + 1)
            for y in range(1, max_y + 1):
                area = 2 * x * y + x + y
                candidates.add(area)
        return sorted(candidates)

    def generate(self) -> Iterator[int]:
        if not self._cache:
            self._cache = self._generate_all()
        for area in self._cache:
            yield area


class InputReader:
    """
    入力を読み込むクラス
    """

    def __init__(self):
        self.room_count: int = 0
        self.areas: List[int] = []

    def read(self) -> None:
        import sys
        self.room_count = int(sys.stdin.readline().strip())
        self.areas = [int(sys.stdin.readline().strip()) for _ in range(self.room_count)]


class Validator:
    """
    入力面積リストの妥当性を判定し、誤りの数を数えるクラス
    """

    def __init__(self, valid_areas: List[int]):
        self.valid_areas = valid_areas

    def count_invalid(self, target_areas: List[int]) -> int:
        # valid_areas は昇順ソート済み
        valid_set = set(self.valid_areas)
        invalid_count = 0
        for area in target_areas:
            if area not in valid_set:
                invalid_count += 1
        return invalid_count


class IOIRealEstateProblemSolver:
    """
    上位レベルの問題解決クラス
    """

    MAX_AREA_LIMIT = 2_147_483_647

    def __init__(self):
        self.input_reader = InputReader()
        self.area_generator = FormulaAreaSequenceGenerator(self.MAX_AREA_LIMIT)
        self.validator: Validator = None

    def solve(self) -> None:
        # 1. 入力読み込み
        self.input_reader.read()
        # 2. 可能な面積生成
        valid_areas = list(self.area_generator.generate())
        # 3. Validator作成
        self.validator = Validator(valid_areas)
        # 4. 間違った面積数をカウント
        invalid_count = self.validator.count_invalid(self.input_reader.areas)
        # 5. 出力（最後に改行コードを入れること）
        print(invalid_count)


if __name__ == "__main__":
    solver = IOIRealEstateProblemSolver()
    solver.solve()