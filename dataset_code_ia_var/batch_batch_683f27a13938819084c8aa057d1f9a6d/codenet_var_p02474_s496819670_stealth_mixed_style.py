def get_inputs():
    values = input().split()
    return map(int, values)

a, b = get_inputs()

result = (lambda x, y: x*y)(a, b)

import sys
sys.stdout.write(str(result) + "\n")