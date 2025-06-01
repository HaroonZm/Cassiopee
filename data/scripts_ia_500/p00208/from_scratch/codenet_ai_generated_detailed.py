def old_to_new_room_number(n):
    """
    Convert the old room number n to the new room number system,
    where digits '4' and '6' are excluded from the numbering.
    
    Approach:
    - The new numbering can be thought of as a base-8 system excluding digits '4' and '6'.
    - Allowed digits in new numbering are: 0,1,2,3,5,7,8,9 (8 digits total).
    - We map the old room number n to a number in this base-8-like system, then convert it back to decimal,
      interpreting the digits as above.
    - Instead of converting to the new number directly, we convert n-1 to base 8 to get the index digits,
      then map each digit (0-7) to the allowed digits.
    - Finally, join these mapped digits to get the new room number.
    
    This works because:
    * Each old number corresponds to one unique new number excluding '4' and '6'.
    * Counting in this modified digit set is like counting in base 8 with a custom digit mapping.
    """
    # Mapping from base 8 digit to allowed digit
    digit_map = ['0', '1', '2', '3', '5', '7', '8', '9']
    
    n -= 1  # zero-based indexing for conversion
    
    if n == 0:
        # If n=1 originally, zero-based is 0, corresponds to digit_map[0] = '0',
        # but since room numbers start at 1, result is '1' (digit_map[1])
        # Actually for n=1 old room => new room = '1' according to sample.
        return '1'

    digits = []
    while n > 0:
        remainder = n % 8
        digits.append(digit_map[remainder])
        n //=8
    
    # Reverse digits because we computed digits from least-significant digit
    digits.reverse()
    
    # Join to form new room number string
    new_room_str = ''.join(digits)
    
    return int(new_room_str)

import sys

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    n = int(line)
    print(old_to_new_room_number(n))