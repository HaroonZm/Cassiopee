def main():
    import sys
    target_pattern = [5, 7, 5, 7, 7]
    lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n_line = lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        words = lines[idx:idx+n]
        idx += n
        # Precompute length of each word
        lengths = [len(w) for w in words]
        # Try all possible starting positions s
        # For each s, try to find 5 segments with letter counts matching target_pattern
        for s in range(n):
            pos = s
            matched = True
            for segment_len in target_pattern:
                count_letters = 0
                # collect words until count_letters == segment_len or exceed
                while pos < n and count_letters < segment_len:
                    count_letters += lengths[pos]
                    pos += 1
                if count_letters != segment_len:
                    matched = False
                    break
            if matched:
                print(s+1)
                break

if __name__ == '__main__':
    main()