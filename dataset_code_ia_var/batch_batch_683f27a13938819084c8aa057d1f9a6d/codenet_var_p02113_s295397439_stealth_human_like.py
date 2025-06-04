import sys

def main():
    # Ok, let's parse inputs (I prefer lists, maybe it's bad)
    n, l = map(int, input().split())
    counter = dict()
    for _ in range(n):
        word = input()
        # not sure if this is the most efficient way, but works
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

    out = ""
    mid = ""
    lst = sorted(counter.keys())  # using sorted, hope it doesn't matter

    for k in lst:
        v = counter[k]
        if k == k[::-1]:  # palindromic
            count = v // 2
            out += k * count
            counter[k] = v - 2*count
            # chose the longest palindrome for the middle
            if counter[k] > 0:
                if len(k) > len(mid):
                    mid = k
        else:
            r = k[::-1]
            if r in counter:
                pair = min(counter[k], counter[r])
                out += k * pair
                counter[k] -= pair
                counter[r] -= pair
            # If not, well, too bad, can't do much

    final = out + mid + out[::-1]
    print(final)

if __name__ == "__main__":
    main()