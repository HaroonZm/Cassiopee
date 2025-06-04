class KeyboardLayout:
    def __init__(self, left_keys: str, right_keys: str):
        self.left_hand_keys = set(left_keys)
        self.right_hand_keys = set(right_keys)
    
    def which_hand(self, char: str) -> str:
        if char in self.left_hand_keys:
            return 'L'
        elif char in self.right_hand_keys:
            return 'R'
        else:
            raise ValueError(f"Character '{char}' not found in any hand keys")
        

class HandSwitchCounter:
    def __init__(self, layout: KeyboardLayout):
        self.layout = layout
    
    def count_switches(self, text: str) -> int:
        prev_hand = None
        switches = 0
        for ch in text:
            current_hand = self.layout.which_hand(ch)
            if prev_hand is not None and current_hand != prev_hand:
                switches += 1
            prev_hand = current_hand
        return switches


class InputProcessor:
    def __init__(self, counter: HandSwitchCounter):
        self.counter = counter
    
    def process_lines(self, lines):
        results = []
        for line in lines:
            line = line.strip()
            if line == '#':
                break
            result = self.counter.count_switches(line)
            results.append(result)
        return results


def main():
    # QWERTY left hand letters as per usual touch typing home row and upper/lower keys
    # Left hand keys based on the figure given in problem (assuming standard QWERTY left side)
    left_hand = "qwertasdfgzxcvb"
    right_hand = "yuiophjklnm"
    layout = KeyboardLayout(left_hand, right_hand)
    counter = HandSwitchCounter(layout)
    processor = InputProcessor(counter)
    
    import sys
    inputs = (line for line in sys.stdin)
    results = processor.process_lines(inputs)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()