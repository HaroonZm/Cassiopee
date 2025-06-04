import sys
from itertools import permutations

def solve(dataset):
    N = dataset[0]
    words = dataset[1:]
    unique_chars = set(''.join(words))
    # Map each unique character to an index
    chars = list(unique_chars)
    char_to_index = {c: i for i, c in enumerate(chars)}
    
    # Gather leading characters, which cannot be zero
    leading_chars = set(word[0] for word in words if len(word) > 1)

    # Precompute positional values for all words except last
    addends = []
    for word in words[:-1]:
        val = [0]*len(chars)
        for i, ch in enumerate(word[::-1]):
            val[char_to_index[ch]] += 10**i
        addends.append(val)
    
    # Precompute positional value for last word (result)
    result_val = [0]*len(chars)
    last_word = words[-1]
    for i, ch in enumerate(last_word[::-1]):
        result_val[char_to_index[ch]] += 10**i

    count = 0
    digits = range(10)
    # The number of unique letters is <= 10
    for perm in permutations(digits, len(chars)):
        # Check leading zero conditions
        skip = False
        for ch in leading_chars:
            if perm[char_to_index[ch]] == 0:
                skip = True
                break
        if skip:
            continue
        # Compute sum of addends
        sum_addends = 0
        for val in addends:
            s = 0
            for i, coeff in enumerate(val):
                s += coeff * perm[i]
            sum_addends += s
        # Compute result value
        res = 0
        for i, coeff in enumerate(result_val):
            res += coeff * perm[i]
        if sum_addends == res:
            count += 1
    return count

def main():
    datasets = []
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(input_lines):
        line = input_lines[idx]
        if line == '0':
            break
        N = int(line)
        dataset = [N]
        idx += 1
        for _ in range(N):
            dataset.append(input_lines[idx])
            idx += 1
        datasets.append(dataset)
    for dataset in datasets:
        print(solve(dataset))

if __name__ == "__main__":
    main()