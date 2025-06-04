from collections import Counter

def solve():
    n = int(input())
    s = input()
    terms = s.split('+')
    count = Counter(terms)
    letters = sorted(count.keys())

    total_len = n
    min_len = total_len

    # length of term string
    def term_len(t):
        return 1

    # length of count string for digits 2..9
    def digit_len(d):
        return len(str(d))

    # Build candidate string length if replaced c times by t*c or (S)*c
    # Check repetition patterns for parentheses usage
    # Try replacements of patterns:
    # 1) single letter repeats: t*c → length: len(t) + 1 + digit_len(c)
    # 2) sum of letters repeated c times: (expr)*c
    # expr: letters separated by '+', length: sum letter len + number of plus signs
    # total length: 2 + len(expr) + 1 + digit_len(c) = len(expr) + digit_len(c) + 3

    # Try replacement only if shorten total length

    # First try single letter repeats
    # Minimal length: sum of letters as is: total_len = n
    # For single letter t repeated c times: length t + '*' + digit
    # that saves c - len(t)*c characters if c > 1

    # Build initial string length (sum of original letters plus plus signs)
    # Actually given by n

    # Try single letter replacement
    for t, c in count.items():
        if c > 1:
            rep_length = 1 + 1 + len(str(c))  # t + '*' + digit(s)
            cand_len = total_len - c*(1) + rep_length
            # t is length 1, each original term is 't' length 1
            # So we saved c - rep_length characters from originals
            # Actually, total_len - c + rep_length
            cand_len = total_len - c + rep_length
            if cand_len < min_len:
                min_len = cand_len

    # Try sum of letters repeated times with parentheses: (expr)*c
    # We try all subsets of letters repeated c times

    # Given problem, subsets must be sets of letters repeated c times, c>=2

    # Count how many times each letter occurs
    # The sum expression is letters separated by '+', length = sum letters (1 each) + (k-1) plus signs
    # total length len(expr) = k + (k-1) = 2k -1

    # We try all possible count values c from 2 to max count for any letter

    # For each c, we try to find subsets of letters whose count >= c

    # Let's find for c in 2..max count of a letter

    max_c = max(count.values())

    # Convert count to list of (letter,count)
    count_items = list(count.items())
    count_items.sort()

    # To find subsets with all counts >= c, for each c, select letters with count >= c
    # The total number of letters in that subset k

    # For that subset, length of replaced expr = 2k -1
    # total length after replacement = total_len - k*c + len((expr)*c) = total_len - k*c + (2k-1 + 3 + len(str(c)) - 1) ????
    # Actually original length for those terms: k * c (each letter length 1 + plus signs)
    # Actually, the terms are separated by plus, so total chars:
    # Each term length 1, plus signs (total terms -1)
    # Original length for those letters repeated c times = k*c + (k*c -1) (plus signs among the terms)
    # But problem states the input only has letters and plus, so total_len counts all plus signs punctuating all terms.
    # If we replace those c repeats of k letters (total k*c terms) with (expr)*c
    #   old length for those terms: k*c + (k*c -1) = 2*k*c -1
    #  new length: (expr) length + 1 (for '*') + digit length c
    #  len(expr) = 2*k -1, (expr) length = 2*k+1 (including parentheses)
    #  total = 2*k +1 + 1 + digit_len(c) = 2k + digit_len(c) + 2

    # length reduced = old length - new length
    # = (2k*c -1) - (2k + digit_len(c) + 2) = 2k*c - 1 - 2k - digit_len(c) - 2
    # = 2k*(c - 1) - digit_len(c) - 3

    # We get better when 2k*(c -1) > digit_len(c) +3

    for c_repeat in range(2, max_c + 1):
        subset = [l for l, cnt in count_items if cnt >= c_repeat]
        if not subset:
            continue
        k = len(subset)
        if k == 0:
            continue
        # Calculate saved length
        old_length = 2 * k * c_repeat - 1
        new_length = 2 * k + len(str(c_repeat)) + 2
        saved = old_length - new_length
        if saved <= 0:
            continue
        candidate_len = total_len - saved
        if candidate_len < min_len:
            min_len = candidate_len

    print(min_len)

solve()