class Era:
    def __init__(self, name:str, initial_year:int, length:int, symbol:str):
        self.name = name
        self.initial_year = initial_year  # 西暦の元年
        self.length = length  # 元号の期間（年数）
        self.symbol = symbol  # 和暦の略記

    def contains_gregorian(self, year:int) -> bool:
        return self.initial_year <= year <= self.initial_year + self.length -1

    def from_gregorian(self, year:int) -> int:
        if not self.contains_gregorian(year):
            raise ValueError(f"{year} is not in era {self.name}")
        return year - self.initial_year + 1

    def to_gregorian(self, year_in_era:int) -> int:
        if year_in_era < 1 or year_in_era > self.length:
            raise ValueError(f"{year_in_era} is not valid year for era {self.name}")
        return self.initial_year + year_in_era - 1

class JapaneseCalendarConverter:
    def __init__(self):
        # 明治 1868~1911 (44 years)
        meiji = Era("Meiji", 1868, 44, "M")
        # 大正 1912~1925 (14 years)
        taisho = Era("Taisho", 1912, 14, "T")
        # 昭和 1926~1988 (63 years)
        showa = Era("Showa", 1926, 63, "S")
        # 平成 1989~2016 (28 years)
        heisei = Era("Heisei", 1989, 28, "H")

        self.eras = [meiji, taisho, showa, heisei]
        self.symbol_to_era = {era.symbol: era for era in self.eras}
        self.name_to_era = {era.name: era for era in self.eras}

    def gregorian_to_japanese(self, year_gregorian:int) -> str:
        # 西暦から和暦への変換。year_gregorian は 1868～2016 の範囲内
        for era in self.eras:
            if era.contains_gregorian(year_gregorian):
                year_in_era = era.from_gregorian(year_gregorian)
                return f"{era.symbol}{year_in_era}"
        raise ValueError(f"西暦{year_gregorian}に対応する和暦がありません")

    def japanese_to_gregorian(self, era_num:int, year_in_era:int) -> int:
        # 和暦の種類と年から西暦へ変換
        # era_num: 1=明治,2=大正,3=昭和,4=平成
        if not (1 <= era_num <= 4):
            raise ValueError(f"和暦の種類 {era_num} は対応していません")
        era = self.eras[era_num-1]
        return era.to_gregorian(year_in_era)

    def convert(self, era_indicator:int, year:int) -> str:
        # era_indicator: 0=西暦, 1-4=和暦として変換
        if era_indicator == 0:
            # 西暦から和暦
            return self.gregorian_to_japanese(year)
        elif 1 <= era_indicator <= 4:
            # 和暦から西暦
            return str(self.japanese_to_gregorian(era_indicator, year))
        else:
            raise ValueError(f"不正な暦の種類: {era_indicator}")

class InputParser:
    def __init__(self, raw_input:str):
        self.raw_input = raw_input.strip()

    def parse(self) -> tuple[int,int]:
        parts = self.raw_input.split()
        if len(parts) != 2:
            raise ValueError("入力は2つの値である必要があります")
        e, y = parts
        e_int = int(e)
        y_int = int(y)
        self._validate(e_int, y_int)
        return e_int, y_int

    def _validate(self, e:int, y:int):
        if not (0 <= e <= 4):
            raise ValueError("暦の種類Eは0～4である必要があります")
        if e == 0 and not (1868 <= y <= 2016):
            raise ValueError("西暦は1868～2016の範囲である必要があります")
        if e == 1 and not (1 <= y <= 44):
            raise ValueError("明治の年は1～44の範囲である必要があります")
        if e == 2 and not (1 <= y <= 14):
            raise ValueError("大正の年は1～14の範囲である必要があります")
        if e == 3 and not (1 <= y <= 63):
            raise ValueError("昭和の年は1～63の範囲である必要があります")
        if e == 4 and not (1 <= y <= 28):
            raise ValueError("平成の年は1～28の範囲である必要があります")

def main():
    import sys
    raw_input = sys.stdin.readline()
    parser = InputParser(raw_input)
    e, y = parser.parse()
    converter = JapaneseCalendarConverter()
    result = converter.convert(e,y)
    print(result)

if __name__ == "__main__":
    main()