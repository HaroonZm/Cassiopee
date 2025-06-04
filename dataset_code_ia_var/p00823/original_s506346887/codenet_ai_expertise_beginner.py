d = {}

def main(s, x=1):
    f = True
    l = 0
    r = 0
    index = 999999999  # Grande valeur
    res = 0
    i = 0
    lis = []
    # On découpe la chaîne s si x=1 sinon on suppose que c'est déjà découpé
    if x:
        while i < len(s):
            if s[i].isupper():
                tmp = s[i]
                i += 1
                while i < len(s) and s[i].islower():
                    tmp += s[i]
                    i += 1
                lis.append(tmp)
            elif s[i].isdigit():
                tmp = s[i]
                i += 1
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                lis.append(tmp)
            else:
                lis.append(s[i])
                i += 1
    else:
        lis = s
    s = lis
    ans = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            f = False
            l += 1
            if i < index:
                index = i
        elif s[i] == ")":
            r += 1
            if l == r:
                # Appel récursif pour la parenthèse, on prend l'intérieur
                res = main(s[index + 1 :i], 0)
                if res == "UNKNOWN":
                    return "UNKNOWN"
                f = True
                # Si un chiffre suit la parenthèse, multiplier
                if i != len(s) - 1:
                    if s[i + 1].isdigit():
                        i += 1
                        res = res * int(s[i])
                ans = ans + res
                index = 999999999
                l = 0
                r = 0
        else:
            if f:
                if not (s[i] in d):
                    return "UNKNOWN"
                res = d[s[i]]
                # Si un chiffre suit, multiplier
                if i != len(s) - 1:
                    if s[i + 1].isdigit():
                        i += 1
                        res = res * int(s[i])
                ans = ans + res
        i += 1
    return ans

if __name__ == "__main__":
    while True:
        n = input()
        if n == "END_OF_FIRST_PART":
            break
        a, b = n.split()
        b = int(b)
        d[a] = b
    while True:
        n = input()
        if n == "0":
            break
        print(main(n))