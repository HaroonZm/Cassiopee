from collections.abc import Sequence

def Inn(s: Sequence[str]) -> str:
    evens = set('RUD')
    odds = set('LUD')
    checks = [(evens if i % 2 == 0 else odds) for i in range(len(s))]
    if all(c in chk for c, chk in zip(s, checks)):
        return "Yes"
    return "No"

print(Inn(input()))