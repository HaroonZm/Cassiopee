from itertools import islice

S = input()

even = S[1::2]
odd = S[::2]

evencount0 = even.count('0')
evencount1 = len(even) - evencount0
unevencount0 = odd.count('0')
unevencount1 = len(odd) - unevencount0

k = min(evencount0 + unevencount1, evencount1 + unevencount0)
print(k)