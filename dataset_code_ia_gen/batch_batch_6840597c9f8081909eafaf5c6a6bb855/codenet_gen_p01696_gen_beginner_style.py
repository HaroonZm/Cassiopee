def next_char(c):
    if c == 'Z':
        return 'A'
    return chr(ord(c) + 1)

def prev_char(c):
    if c == 'A':
        return 'Z'
    return chr(ord(c) - 1)

def decode(s, i):
    res = ''
    while i < len(s):
        if s[i] == ']':
            # fin de ce niveau
            return res, i + 1
        elif s[i] == '[':
            # decode contenu entre []
            inside, next_i = decode(s, i+1)
            # reverse string
            inside_rev = inside[::-1]
            res += inside_rev
            i = next_i
        elif s[i] == '+' or s[i] == '-':
            sign = s[i]
            i += 1
            if i >= len(s):
                # pas normal mais on continue
                break
            c = s[i]
            if c == '?':
                # on essaie de mettre la lettre qui donne le minimum lex apres operation
                # on test toutes les lettres A-Z
                best = None
                for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if sign == '+':
                        cc = next_char(ch)
                    else:
                        cc = prev_char(ch)
                    if best is None or cc < best:
                        best = cc
                res += best
                i += 1
            else:
                if sign == '+':
                    res += next_char(c)
                else:
                    res += prev_char(c)
                i += 1
        else:
            # lettre ou '?'
            c = s[i]
            if c == '?':
                # lettre directement, on choisit 'A'
                res += 'A'
            else:
                res += c
            i += 1
    return res, i

while True:
    line = input()
    if line == '.':
        break
    decoded, _ = decode(line, 0)
    print(decoded)