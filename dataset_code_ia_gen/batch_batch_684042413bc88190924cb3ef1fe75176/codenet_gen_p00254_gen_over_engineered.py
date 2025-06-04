class Kaprekar6174Process:
    TARGET = 6174
    
    def __init__(self, number: str):
        self.original_number = self._normalize(number)
        self.current_number = self.original_number
    
    @staticmethod
    def _normalize(number: str) -> str:
        return number.zfill(4)
    
    @staticmethod
    def _all_digits_same(number: str) -> bool:
        return all(d == number[0] for d in number)
    
    def _digits_to_int_list(self, number: str) -> list[int]:
        return [int(d) for d in number]
    
    def _int_list_to_number(self, digits: list[int]) -> int:
        return int("".join(str(d) for d in digits))
    
    def _step(self) -> None:
        digits = self._digits_to_int_list(self.current_number)
        digits_sorted_asc = sorted(digits)
        digits_sorted_desc = digits_sorted_asc[::-1]
        L = self._int_list_to_number(digits_sorted_desc)
        S = self._int_list_to_number(digits_sorted_asc)
        next_number = L - S
        self.current_number = self._normalize(str(next_number))
    
    def execute_until_target_or_invalid(self) -> str | int:
        if self._all_digits_same(self.current_number):
            return "NA"
        if self.current_number == self._normalize(str(self.TARGET)):
            return 0
        
        step_count = 0
        while self.current_number != self._normalize(str(self.TARGET)):
            self._step()
            step_count += 1
            # In theory the loop should always end except all digits same case
            # Avoid infinite loop just in case
            if step_count > 10000:
                return "NA"
        return step_count

class InputOutputProcessor:
    def __init__(self, processor_cls):
        self.processor_cls = processor_cls
        
    def process_input(self, lines: list[str]) -> list[str]:
        results = []
        for line in lines:
            number = line.strip()
            if number == "0000":
                break
            processor = self.processor_cls(number)
            result = processor.execute_until_target_or_invalid()
            results.append(str(result))
        return results

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    io_processor = InputOutputProcessor(Kaprekar6174Process)
    results = io_processor.process_input(input_lines)
    print('\n'.join(results))

if __name__ == "__main__":
    main()