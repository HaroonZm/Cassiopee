import sys

input = sys.stdin.readline

def main():
    S = input().rstrip()

    if 1 <= int(S[:2]) <= 12:
        is_MMYY = True
    else:
        is_MMYY = False

    if 1 <= int(S[2:]) <= 12:
        is_YYMM = True
    else:
        is_YYMM = False

    if is_MMYY and is_YYMM:
        ans = "AMBIGUOUS"
    elif is_MMYY:
        ans = "MMYY"
    elif is_YYMM:
        ans = "YYMM"
    else:
        ans = "NA"

    print(ans)

if __name__ == "__main__":
    main()