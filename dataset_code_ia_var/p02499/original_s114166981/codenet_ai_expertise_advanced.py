from collections import Counter
import sys
import string

def main():
    counter = Counter()
    letters = string.ascii_lowercase
    for line in sys.stdin:
        counter.update(filter(letters.__contains__, line.lower()))
    print('\n'.join(f"{c} : {counter[c]}" for c in letters))

if __name__ == "__main__":
    main()