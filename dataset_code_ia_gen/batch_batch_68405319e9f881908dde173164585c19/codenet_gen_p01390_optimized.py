import sys

used = set()

def out(word):
    print(f"?{word}")
    sys.stdout.flush()
    used.add(word)

def err():
    print("!OUT")
    sys.stdout.flush()
    exit()

def main():
    # start with 'a'
    first = "a"
    out(first)
    prev = first
    while True:
        ai = input().strip()
        if ai in used:
            err()
        if not (1 <= len(ai) <= 2) or not ai.islower():
            err()
        if ai[0] != prev[-1]:
            err()
        used.add(ai)
        # Now respond with a word starting with ai[-1] not used yet
        # because AI words length max 2, we use 1 length words for simplicity
        start_char = ai[-1]
        # try single letter from start_char to 'z'
        found = False
        for c in range(ord(start_char), ord('z')+1):
            w = chr(c)
            if w not in used:
                out(w)
                prev = w
                found = True
                break
        if not found:
            # no new word found (should not happen within limits), call error (won't happen)
            err()

if __name__ == "__main__":
    main()