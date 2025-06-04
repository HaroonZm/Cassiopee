def soroban_display(num_str):
    num_str = num_str.rjust(5, '0')
    digits_map = {
        '0': ['****', '*   ', '=====', '****', '****', '****'],
        '1': ['*   ', '*   ', '=====', '*   ', '****', '*   '],
        '2': ['****', '*   ', '=====', '* * ', '****', '****'],
        '3': ['****', '*   ', '=====', '* **', '*****', '*****'],
        '4': ['****', '* * ', '=====', '*   ', '*****', '*****'],
        '5': ['****', '*   ', '=====', '****', '*****', '*****'],
        '6': ['****', '* * ', '=====', '****', '*****', '*****'],
        '7': ['****', '*   ', '=====', '*   ', '*   ', '****'],
        '8': ['****', '* * ', '=====', '* * ', '****', '****'],
        '9': ['****', '* * ', '=====', '****', '*   ', '*   '],
    }
    lines = ['' for _ in range(6)]
    for d in num_str:
        patterns = digits_map[d]
        for i in range(6):
            lines[i] += patterns[i]
    return '\n'.join(lines)

import sys
inputs = [line.strip() for line in sys.stdin if line.strip()]
for i, num in enumerate(inputs):
    print(soroban_display(num))
    if i != len(inputs) - 1:
        print()