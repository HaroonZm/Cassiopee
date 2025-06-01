class PocketMoney:
    def __init__(self, alice_amount: int, brown_amount: int):
        self.alice_amount = alice_amount
        self.brown_amount = brown_amount

    def total(self) -> int:
        return self.alice_amount + self.brown_amount

    def half_share(self) -> int:
        return self.total() // 2

class ShareCalculatorInterface:
    def calculate_share(self, pocket_money: PocketMoney) -> int:
        raise NotImplementedError

class EqualShareCalculator(ShareCalculatorInterface):
    def calculate_share(self, pocket_money: PocketMoney) -> int:
        return pocket_money.half_share()

class PocketMoneyReaderInterface:
    def read(self) -> PocketMoney:
        raise NotImplementedError

class StandardInputPocketMoneyReader(PocketMoneyReaderInterface):
    def read(self) -> PocketMoney:
        raw_input = input().strip()
        alice_str, brown_str = raw_input.split()
        return PocketMoney(int(alice_str), int(brown_str))

class PocketMoneyService:
    def __init__(self, reader: PocketMoneyReaderInterface, calculator: ShareCalculatorInterface):
        self.reader = reader
        self.calculator = calculator

    def process(self) -> None:
        pocket_money = self.reader.read()
        share = self.calculator.calculate_share(pocket_money)
        print(share)

if __name__ == "__main__":
    reader = StandardInputPocketMoneyReader()
    calculator = EqualShareCalculator()
    service = PocketMoneyService(reader, calculator)
    service.process()