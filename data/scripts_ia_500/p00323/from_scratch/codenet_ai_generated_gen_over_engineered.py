from typing import List, Tuple
from collections import defaultdict
from abc import ABC, abstractmethod

class Unit(ABC):
    @abstractmethod
    def to_base(self) -> int:
        pass

    @staticmethod
    @abstractmethod
    def from_base(value: int) -> 'Unit':
        pass

class Bocco(Unit):
    # ボッコ単位の重さは 2^x グラムで表現されるが、ここではxを直接扱う。
    def __init__(self, x: int):
        if x < 0:
            raise ValueError("Bocco unit index must be non-negative")
        self.x = x

    def to_base(self) -> int:
        # グラム単位に変換（2^x）
        return 1 << self.x

    @staticmethod
    def from_base(value: int) -> 'Bocco':
        # baseが2^x形式でない場合に備え、xを元に作るだけとする
        # 実際にはxを直接保持する問題設定から解くのでここは不使用
        raise NotImplementedError("Direct from_base with non exponent not supported")

    def __eq__(self, other):
        return isinstance(other, Bocco) and self.x == other.x

    def __lt__(self, other):
        return self.x < other.x

    def __hash__(self):
        return hash(self.x)

    def __repr__(self):
        return f"Bocco({self.x})"

class Marugu(Unit):
    # マルグ単位の個数は 2^y 個であるが、ここでは y を直接扱う。
    def __init__(self, y: int):
        if y < 0:
            raise ValueError("Marugu unit index must be non-negative")
        self.y = y

    def to_base(self) -> int:
        # 個数単位に変換（2^y）
        return 1 << self.y

    @staticmethod
    def from_base(value: int) -> 'Marugu':
        # 実装同様にyを元に作ることは想定しない
        raise NotImplementedError("Direct from_base with non exponent not supported")

    def __eq__(self, other):
        return isinstance(other, Marugu) and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y

    def __hash__(self):
        return hash(self.y)

    def __repr__(self):
        return f"Marugu({self.y})"

class AizuniumChunk:
    def __init__(self, bocco_weight: Bocco, marugu_count: Marugu):
        self.bocco = bocco_weight
        self.marugu = marugu_count

    def total_weight(self) -> int:
        # アイヅニウムの全重量＝ (2^x) * (2^y) = 2^(x+y)
        # ただし実際は整数として直接計算する
        return (1 << self.bocco.x) * (1 << self.marugu.y)

    def __repr__(self):
        return f"AizuniumChunk(Bocco={self.bocco.x}, Marugu={self.marugu.y})"

class CollectionProcessor:
    def __init__(self):
        self.chunks: List[AizuniumChunk] = []

    def add_chunk(self, a_i: int, b_i: int) -> None:
        # 入力はx,yで与えられている（a_i: Bocco単位の重さ； b_i: Marugu単位の個数）
        if a_i < 0 or b_i < 0:
            raise ValueError("a_i and b_i must be non-negative integers")
        chunk = AizuniumChunk(Bocco(a_i), Marugu(b_i))
        self.chunks.append(chunk)

    def aggregate_weight(self) -> int:
        # 全てのアイヅニウムの総重量を計算
        total = 0
        for chunk in self.chunks:
            total += chunk.total_weight()
        return total

class RecycleStrategy(ABC):
    @abstractmethod
    def minimize_chunks(self, total_weight: int) -> List[AizuniumChunk]:
        pass

class MinimalChunkCountStrategy(RecycleStrategy):
    """
    最小の塊の個数にする戦略：
    アイヅニウムの総重量total_weightは整数。
    これを、2^x単位の塊の和で表し、塊の数を最小化する。
    2進展開で1のビット数が塊の数の最小値となる。
    それぞれの塊の重さは2^xグラム、個数は2^0(1個)とする（マルグ単位は0）。
    """

    def minimize_chunks(self, total_weight: int) -> List[AizuniumChunk]:
        results = []
        bitpos = 0
        while total_weight > 0:
            if total_weight & 1:
                # 2^bitpos の重さの1個の塊として再生
                results.append(AizuniumChunk(Bocco(bitpos), Marugu(0)))
            total_weight >>= 1
            bitpos += 1

        # 重さの小さい順にソート済み（bitposが小さい順）
        results.sort(key=lambda c: c.bocco.x)
        return results

class RecycleFacility:
    def __init__(self, strategy: RecycleStrategy):
        self.strategy = strategy

    def recycle(self, processor: CollectionProcessor) -> List[AizuniumChunk]:
        total_weight = processor.aggregate_weight()
        return self.strategy.minimize_chunks(total_weight)

# --- 以下は実際の処理部分 ---

class InputParser:
    @staticmethod
    def parse_input() -> CollectionProcessor:
        import sys
        N = int(sys.stdin.readline().strip())
        processor = CollectionProcessor()
        for _ in range(N):
            a_i, b_i = map(int, sys.stdin.readline().strip().split())
            processor.add_chunk(a_i, b_i)
        return processor

class OutputPrinter:
    @staticmethod
    def print_chunks(chunks: List[AizuniumChunk]) -> None:
        for chunk in chunks:
            print(chunk.bocco.x, chunk.marugu.y)

def main():
    processor = InputParser.parse_input()
    strategy = MinimalChunkCountStrategy()
    facility = RecycleFacility(strategy)
    minimized_chunks = facility.recycle(processor)
    OutputPrinter.print_chunks(minimized_chunks)


if __name__ == "__main__":
    main()