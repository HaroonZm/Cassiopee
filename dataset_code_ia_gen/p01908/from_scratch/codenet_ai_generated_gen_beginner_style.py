n = int(input())
dangerous = [input() for _ in range(n)]

substrings = set()
for s in dangerous:
    length = len(s)
    for i in range(length):
        for j in range(i+1, length+1):
            substrings.add(s[i:j])

from string import ascii_lowercase

# On cherche la plus courte chaîne hors des sous-chaînes interdites,
# en commençant par les chaînes de longueur 1, puis 2, etc.
# En générant par ordre alphabétique.

def dfs(current, max_len):
    if len(current) > max_len:
        return None
    if current != "" and current not in substrings:
        return current
    for c in ascii_lowercase:
        res = dfs(current + c, max_len)
        if res is not None:
            return res
    return None

max_len = 1
while True:
    ans = dfs("", max_len)
    if ans is not None:
        print(ans)
        break
    max_len += 1