import sys

def main():
    S = input()
    if not (1 <= len(S) <= 100):
        print("No")
        sys.exit()

    valid_even = {"L", "U", "D"}
    valid_odd  = {"R", "U", "D"}
    allowed    = valid_even | valid_odd

    for i, c in enumerate(S):
        if c not in allowed:
            print("No")
            sys.exit()
        if (i % 2 == 0 and c not in valid_odd) or (i % 2 == 1 and c not in valid_even):
            print("No")
            sys.exit()
    print("Yes")

if __name__ == "__main__":
    main()