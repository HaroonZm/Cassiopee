from string import ascii_uppercase
from functools import lru_cache

# Préparer la liste des lettres A-Z
LETTERS = ascii_uppercase

@lru_cache(maxsize=None)
def shift_letter(c, offset):
    # Décalage circulaire dans A-Z, gère les surpassements négatifs/positifs
    if c == '?':
        return 'A'
    idx = (ord(c) - ord('A') + offset) % 26
    return LETTERS[idx]

def process_letters(s):
    stack = 0
    output = []
    for char in s:
        if char == '+':
            stack += 1
        elif char == '-':
            stack -= 1
        elif 'A' <= char <= 'Z' or char == '?':
            output.append(shift_letter(char, stack))
            stack = 0
        elif char in '[]':
            output.append(char)
    return ''.join(output)

def reverse_brackets(s):
    result = []
    it = iter(enumerate(s))
    for idx, ch in it:
        if ch == '[':
            sub, new_idx = extract_and_reverse(s, idx + 1)
            result.append(sub)
            # Avancer jusqu'à new_idx après le sous-bloc traité
            for _ in range(idx + 1, new_idx + 1):
                next(it, None)
        else:
            result.append(ch)
    return ''.join(result)

def extract_and_reverse(s, start):
    buf = []
    i = start
    while i < len(s):
        c = s[i]
        if c == '[':
            sub, end = extract_and_reverse(s, i + 1)
            buf.append(sub)
            i = end
        elif c == ']':
            return ''.join(buf)[::-1], i
        else:
            buf.append(c)
        i += 1
    return ''.join(buf), i  # Should not occur if brackets are balanced

def main():
    import sys
    readline = sys.stdin.readline
    while True:
        s = readline()
        if not s:
            break
        s = s.rstrip('\n')
        if s == ".":
            break
        expanded = process_letters(s)
        result = reverse_brackets(expanded)
        print(result)

if __name__ == "__main__":
    main()