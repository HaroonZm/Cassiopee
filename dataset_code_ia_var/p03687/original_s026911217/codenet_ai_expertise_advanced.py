from string import ascii_lowercase

def min_steps_to_uniform(s: str) -> int:
    s_list = list(s)
    result = float('inf')

    # Memoization for optimization (optional, but not hugely impactful here)
    for target in set(s_list):
        cur = s_list.copy()
        steps = 0
        while not all(ch == target for ch in cur):
            # Using list comprehension for transformation
            cur = [
                target if cur[i] == target or cur[i+1] == target else None
                for i in range(len(cur) - 1)
            ]
            steps += 1
        result = min(result, steps)
    return result

if __name__ == "__main__":
    import sys
    print(min_steps_to_uniform(sys.stdin.readline().strip()))