from collections import Counter

def main():
    D = input()
    target = "AIDUNYAN"
    target_len = len(target)
    target_count = Counter(target)
    res = list(D)

    for i in range(len(D) - target_len + 1):
        window = D[i:i+target_len]
        if Counter(window) == target_count:
            res[i:i+target_len] = list("AIZUNYAN")

    print("".join(res))

if __name__ == "__main__":
    main()