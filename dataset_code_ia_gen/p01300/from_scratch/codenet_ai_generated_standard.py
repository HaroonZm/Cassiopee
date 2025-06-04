import sys

def count_11_sequences(num):
    count = 0
    prefix_mod = {0:1}
    mod = 0
    power10 = 1
    n = len(num)
    for i in range(n-1, -1, -1):
        if num[i] == '0':
            power10 = (power10 * 10) % 11
            mod = (mod + 0 * power10) % 11
            prefix_mod = {0:1}
            continue
        # reset if leading zero in substring is invalid
        prefix_mod_new = {}
        mod = 0
        power10 = 1
        for j in range(i, n):
            if num[i] == '0':  # leading zero not allowed
                break
            mod = (mod * 10 + int(num[j])) % 11
            if mod == 0:
                count += 1
        break
    # Above code is incorrect, implement correct method:
    # We'll use prefix sums mod 11 from left to right.
    count = 0
    prefix_counts = [0]*11
    prefix_mod = 0
    prefix_counts[0] = 1
    for i, ch in enumerate(num):
        if ch == '0':
            prefix_mod = 0
            prefix_counts = [0]*11
            prefix_counts[0] = 1
            continue
        prefix_mod = (prefix_mod*10 + int(ch)) % 11
        count += prefix_counts[prefix_mod]
        prefix_counts[prefix_mod] += 1
    return count

for line in sys.stdin:
    line=line.strip()
    if line=='0':
        break
    print(count_11_sequences(line))