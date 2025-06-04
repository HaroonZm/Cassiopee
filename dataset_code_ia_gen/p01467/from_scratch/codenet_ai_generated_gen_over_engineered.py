class BorrowStrategy:
    """抽象的な繰り下がり忘れ戦略の基底クラス"""
    def should_forget(self, index: int, remaining: int) -> bool:
        raise NotImplementedError

class MaximizeResultStrategy(BorrowStrategy):
    """最大値を得るため、繰り下がり忘れをできるだけ使う戦略"""
    def should_forget(self, index: int, remaining: int) -> bool:
        return remaining > 0

class DigitNumber:
    """数字を桁のリストとして抽象化"""
    def __init__(self, number: int, length: int = None):
        self.digits = self._to_digits(number)
        if length is not None and length > len(self.digits):
            # 上位桁に0埋めをする
            self.digits.extend([0] * (length - len(self.digits)))

    @staticmethod
    def _to_digits(number: int):
        if number == 0:
            return [0]
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //=10
        return digits  # 下位桁から順に格納

    def __len__(self):
        return len(self.digits)

    def __getitem__(self, index):
        return self.digits[index]

    def __setitem__(self, index, value):
        self.digits[index] = value

    def to_int(self) -> int:
        # 上位桁から連続する0を除去して整数に変換
        d = self.digits[:]
        while len(d) > 1 and d[-1] == 0:
            d.pop()
        value = 0
        for digit in reversed(d):
            value = value * 10 + digit
        return value

class BorrowForgetSimulator:
    def __init__(self, A: int, B: int, K: int, strategy: BorrowStrategy):
        self.A = A
        self.B = B
        self.K = K
        self.strategy = strategy
        self.n = len(str(A))
        self.numA = DigitNumber(A, self.n)
        self.numB = DigitNumber(B, self.n)

    def simulate(self) -> int:
        borrow = [0] * (self.n + 1)
        C = [0] * self.n
        forget_count = 0

        for i in range(self.n):
            A_i = self.numA[i]
            B_i = self.numB[i]
            A_sub = A_i - borrow[i]
            if A_sub >= B_i:
                C[i] = A_sub - B_i
                borrow[i+1] = 0
            else:
                # 本来は borrow[i+1] = 1
                # だが繰り下がり忘れが許されているとき：
                if forget_count < self.K and self.strategy.should_forget(i, self.K - forget_count):
                    # 繰り下がり忘れの適用 → borrow[i+1] = 0 で大きくなる結果を優先
                    C[i] = 10 + A_sub - B_i
                    borrow[i+1] = 0
                    forget_count += 1
                else:
                    C[i] = 10 + A_sub - B_i
                    borrow[i+1] = 1
        result_num = DigitNumber(0, self.n)
        for i in range(self.n):
            result_num[i] = C[i]
        return result_num.to_int()

def main():
    import sys
    A, B, K = map(int, sys.stdin.readline().split())
    strategy = MaximizeResultStrategy()
    sim = BorrowForgetSimulator(A, B, K, strategy)
    print(sim.simulate())

if __name__ == "__main__":
    main()