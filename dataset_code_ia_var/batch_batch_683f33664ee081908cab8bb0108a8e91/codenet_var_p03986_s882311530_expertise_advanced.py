from itertools import accumulate

def solve(X: str) -> int:
    unmatched = 0
    balance = 0
    for c in X:
        if c == 'S':
            balance += 1
        elif balance:
            balance -= 1
        else:
            unmatched += 1
    return unmatched + balance

if __name__ == "__main__":
    print(solve(input()))