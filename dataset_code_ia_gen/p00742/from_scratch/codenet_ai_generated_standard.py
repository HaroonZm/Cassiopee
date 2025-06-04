import sys
from itertools import permutations

def solve_case(words):
    first_letters = set(word[0] for word in words if len(word) > 1)
    letters = set(''.join(words))
    letters = list(letters)
    n = len(letters)
    if n > 10:
        return 0
    indices = {c:i for i,c in enumerate(letters)}
    nums = [[indices[c] for c in word] for word in words]

    count = 0
    digits = tuple(range(10))
    for perm in permutations(digits, n):
        if any(perm[indices[c]] == 0 for c in first_letters):
            continue
        total = 0
        for i in range(len(words)-1):
            val = 0
            for d in nums[i]:
                val = val*10 + perm[d]
            total += val
        val = 0
        for d in nums[-1]:
            val = val*10 + perm[d]
        if total == val:
            count += 1
    return count

def main():
    lines = sys.stdin.read().strip().split('\n')
    i = 0
    while True:
        if i >= len(lines):
            break
        n = lines[i]
        i += 1
        if n == '0':
            break
        n = int(n)
        words = lines[i:i+n]
        i += n
        print(solve_case(words))

if __name__ == '__main__':
    main()