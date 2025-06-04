import collections
def main():
    s = input().strip()
    counts = dict()
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    t = len(s)
    result = [0]
    i = 0
    while i < len(s):
        counts[s[i]] -= 1
        t -= 1
        result[0] = result[0] + t - counts[s[i]]
        i += 1
    print((lambda x: x+1)(result[0]))

main()