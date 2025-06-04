import sys
from collections import Counter

def main():
    input = sys.stdin.readline

    while True:
        line = input()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        elems = [input().strip() for _ in range(n)]
        text_lines = [input().strip() for _ in range(m)]
        text = "".join(text_lines)

        # Count total chars needed for the concatenation
        total_len = sum(len(e) for e in elems)

        # Count frequency of chars among all element strings (multiset)
        needed_freq = Counter()
        for e in elems:
            needed_freq.update(e)

        count = 0
        # Use a sliding window of length total_len over text
        # At each position, compute frequency of chars in substring and compare to needed_freq
        # To speed up, maintain a window counter updated incrementally
        window_freq = Counter(text[:total_len])

        if window_freq == needed_freq:
            # To deal with duplicates: verify that the substring can be partitioned into all elements in some order
            # This is ensured because frequency matches total frequency of elements
            count += 1

        for i in range(1, len(text) - total_len + 1):
            left_char = text[i - 1]
            right_char = text[i + total_len - 1]

            window_freq[left_char] -= 1
            if window_freq[left_char] == 0:
                del window_freq[left_char]

            window_freq[right_char] += 1

            if window_freq == needed_freq:
                count += 1

        print(count)

if __name__ == "__main__":
    main()