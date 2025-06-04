def extract_parts(program):
    parts = []
    i = 0
    n = len(program)
    while i < n:
        if program[i] == '"':
            j = i + 1
            while j < n and program[j] != '"':
                j += 1
            # string literal is from i to j inclusive
            parts.append(program[i:j+1])
            i = j + 1
        else:
            j = i
            while j < n and program[j] != '"':
                j += 1
            parts.append(program[i:j])
            i = j
    return parts

def is_close(p1, p2):
    parts1 = extract_parts(p1)
    parts2 = extract_parts(p2)
    if len(parts1) != len(parts2):
        return False
    diff_count = 0
    for part1, part2 in zip(parts1, parts2):
        if part1 != part2:
            # differ, check if both are string literals and only one difference
            if not (part1.startswith('"') and part1.endswith('"') and part2.startswith('"') and part2.endswith('"')):
                return False
            diff_count += 1
            if diff_count > 1:
                return False
    if diff_count == 1:
        return True
    return False

while True:
    s1 = input()
    if s1 == '.':
        break
    s2 = input()
    if s1 == s2:
        print("IDENTICAL")
    elif is_close(s1, s2):
        print("CLOSE")
    else:
        print("DIFFERENT")