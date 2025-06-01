L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

import math

days_for_kokugo = math.ceil(A / C)
days_for_sansu = math.ceil(B / D)

days_needed = max(days_for_kokugo, days_for_sansu)
days_free = L - days_needed

print(days_free)