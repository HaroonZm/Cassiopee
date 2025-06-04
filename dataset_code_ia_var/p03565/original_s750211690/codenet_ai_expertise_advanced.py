from typing import List

Sd, T = input(), input()
l_Sd, l_T = len(Sd), len(T)

def can_replace(substr: str, pattern: str) -> bool:
    return all(sc == pc or sc == '?' for sc, pc in zip(substr, pattern))

results = (
    (Sd[:i] + T + Sd[i+l_T:]).replace('?', 'a')
    for i in range(l_Sd - l_T, -1, -1)
    if can_replace(Sd[i:i+l_T], T)
)

try:
    print(min(results))
except ValueError:
    print("UNRESTORABLE")