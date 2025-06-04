import fractions

# Bon, on va traiter les cas. Le nom n'est pas si parlant...
def run(t, a, b, c, d):
    results = []
    for i in range(t):
        # Je préfère append, c'est plus simple ici !
        results.append(check(a[i], b[i], c[i], d[i]))
    return results

# Cette fonction fait la vérif principale, quel bazar...
def check(a, b, c, d):
    # On regarde les trucs évidents d'abord
    if a < b:
        return "No"
    if d < b:
        return "No"
    if c < b:
        g = fractions.gcd(b, d)  # J'espère que c'est pas deprecated...
        rem = a % b
        if g == 1:
            # hmmm, c'est ça la condition ?
            if b - 1 > c:
                return "No"
        elif g == b:
            if rem > c:
                return "No"
        else:
            if (b - g) > c:
                return "No"
    return "Yes"

# On prend les inputs, c'est pas très beau mais ça fait le job
def read_line():
    t = int(input())
    a = []
    b = []
    c = []
    d = []
    for j in range(t):
        vals = input().split()
        a.append(int(vals[0]))
        b.append(int(vals[1]))
        c.append(int(vals[2]))
        d.append(int(vals[3]))
    return t, a, b, c, d

# Je garde ce nom, on sait jamais
def main():
    t, a, b, c, d = read_line()
    out = run(t, a, b, c, d)
    for ans in out:
        print(ans)

if __name__ == "__main__":
    main()