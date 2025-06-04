import sys

def generate_codes(words, length):
    # Utilise des expressions génératrices et slicings intelligents
    for word in words:
        code = ''.join(
            word[j]
            for j in range(1, len(word))
            if word[j - 1] in 'aiueo'
        )[:length]
        yield code

def min_unique_length(words):
    maxlen = max(len(w) for w in words)
    for code_len in range(1, maxlen + 1):
        codes = list(generate_codes(words, code_len))
        # Utilise un ensemble pour tester unicité en temps constant
        if len(codes) == len(set(codes)):
            return code_len
    return -1

def main():
    lines = iter(sys.stdin.readline, '')
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            # Utilise a + input() de manière concise via une compréhension avancée
            s = ['a' + next(lines).rstrip() for _ in range(n)]
            print(min_unique_length(s))
        except StopIteration:
            break

if __name__ == "__main__":
    main()