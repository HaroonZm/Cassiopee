# Mapping of buttons to their characters based on the problem statement
# Each button cycles through its characters according to the number of presses modulo length
# Button 0 is special and handled separately
button_chars = {
    '1': ["'", ",", ".", "!", "?", " "],       # 6 characters cycle
    '2': ['a', 'b', 'c', 'A', 'B', 'C'],      # 6 characters cycle
    '3': ['d', 'e', 'f', 'D', 'E', 'F'],      # 6 characters cycle
    '4': ['g', 'h', 'i', 'G', 'H', 'I'],      # 6 characters cycle
    '5': ['j', 'k', 'l', 'J', 'K', 'L'],      # 6 characters cycle
    '6': ['m', 'n', 'o', 'M', 'N', 'O'],      # 6 characters cycle
    '7': ['p', 'q', 'r', 's', 'P', 'Q', 'R', 'S'], # 8 characters cycle (standard 7-key phones have 7 for pqrs)
    '8': ['t', 'u', 'v', 'T', 'U', 'V'],      # 6 characters cycle
    '9': ['w', 'x', 'y', 'z', 'W', 'X', 'Y', 'Z'], # 8 characters cycle
}

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    result = []   # Final decoded message
    
    # We'll parse the input line by grouping presses by button, but 0 is special
    # 0 breaks the sequence into parts and allows pressing the same button after 0
    # So sequence segments are separated by '0' presses
    
    # We simulate to process presses consecutively.
    # Approach:
    # - Split input by '0' runs to get parts separated by one or more zero presses
    # - Number of zeros in a run > 1 means (n-1) spaces added
    # - Number of zeros == 1 means allowing next presses of same button without merging
    
    # We process the input by iterating over the characters while grouping consecutive same digits.
    # When we hit '0', count how many in a row.
    # If > 1 zero -> output spaces
    # If == 1 zero -> separator allowing next groups
    
    i = 0
    n = len(line)
    # last_ch_pressed: to know if with '0' we allow same button repeated or need separate groups
    last_button = None
    
    while i < n:
        ch = line[i]
        
        if ch == '0':
            # Count how many zeros in a row
            zero_count = 1
            i += 1
            while i < n and line[i] == '0':
                zero_count += 1
                i += 1
            # If multiple zeros output (zero_count-1) spaces
            if zero_count > 1:
                result.append(' ' * (zero_count - 1))
            # If exactly one zero, it is a separator allowing next presses of same button
            last_button = None
            continue
        
        # For non-zero digit, count the number of consecutive same digits
        count = 1
        i += 1
        while i < n and line[i] == ch:
            count += 1
            i += 1
        
        # Now decode this group of presses on button ch count times
        
        # For buttons 1 to 9:
        if ch in button_chars:
            chars_list = button_chars[ch]
            length = len(chars_list)
            # The characters cycle every length presses.
            # Pressing the button count times means character index = (count-1) % length
            index = (count - 1) % length
            c = chars_list[index]
            result.append(c)
            last_button = ch
        else:
            # Should not happen as input buttons are 0-9 only
            # Just ignore or continue
            last_button = None
    
    print(''.join(result))