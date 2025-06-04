def decrypt_candidates(s):
    # For each character c in s (encrypted string), find possible original characters that map to c after encryption.
    # Encryption replaces the first occurrence of letter x>='b' with the letter before it.
    # So for each character c in the encrypted string:
    # - The original was either c (if not changed), or
    # - If c is between 'a' and 'y' inclusive, original could be c or chr(ord(c)+1)
    # But only one character indexed from left to right got changed (the first occurrence of some letter x).
    # So for each candidate original string, exactly zero or one character must have been decremented during encryption.
    # Therefore, we must generate all possible strings that map to encrypted s by reversing this rule.

    n = len(s)
    candidates = []

    # We try all possibilities where we pick an index i at which the original had a letter c+1 instead of c.
    # If at index i, s[i] != 'z' (because encryption only decrements letters from b to z by 1)
    # then original can be s[i] or s[i]+1 (if s[i]+1 <= 'z')
    # And for all other positions j!=i, original[j] must be s[j].
    # Also we must respect the special rule that only the first occurrence of a letter can be changed.
    # The original encryption change rule decrements the first occurrence of one letter in the original string.
    # On decryption, we must find all strings that could have produced s by changing exactly one character (or none).

    # To find candidates, consider:
    # - No change candidate: original = s
    # - For every letter c in 'a'..'y', find the first occurrence of c in s,
    #   and try to change that occurrence back to chr(ord(c)+1).

    candidates_set = set()
    candidates_set.add(s)

    # Create a map of letter -> first occurrence indices in s
    first_occurrence = {}
    for i, ch in enumerate(s):
        if ch not in first_occurrence:
            first_occurrence[ch] = i

    for c in map(chr, range(ord('a'), ord('y') + 1)):
        if c in first_occurrence:
            i = first_occurrence[c]
            orig_char = chr(ord(c) + 1)
            # Replace s[i] by orig_char
            candidate = s[:i] + orig_char + s[i + 1:]
            candidates_set.add(candidate)

    candidates = sorted(candidates_set)

    return candidates


def main():
    while True:
        line = input()
        if line == '#':
            break
        candidates = decrypt_candidates(line)
        print(len(candidates))
        if len(candidates) <= 10:
            for c in candidates:
                print(c)
        else:
            for c in candidates[:5]:
                print(c)
            for c in candidates[-5:]:
                print(c)


if __name__ == '__main__':
    main()