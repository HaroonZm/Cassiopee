import sys

def levenshtein_damerau(s1, s2, max_dist):
    len1, len2 = len(s1), len(s2)
    if abs(len1 - len2) > max_dist:
        return max_dist + 1
    d = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        d[i][0] = i
    for j in range(len2+1):
        d[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            d[i][j] = min(
                d[i-1][j] + 1,     # deletion
                d[i][j-1] + 1,     # insertion
                d[i-1][j-1] + cost # substitution
            )
            if i>1 and j>1 and s1[i-1]==s2[j-2] and s1[i-2]==s2[j-1]:
                d[i][j] = min(d[i][j], d[i-2][j-2] + 1) # transposition
        if min(d[i]) > max_dist:
            return max_dist + 1
    return d[len1][len2]

def main():
    input=sys.stdin.read().splitlines()
    idx=0
    while True:
        if idx >= len(input):
            break
        n = input[idx].strip()
        if n == '0':
            break
        n = int(n)
        idx +=1
        d = int(input[idx])
        idx +=1
        names = input[idx:idx+n]
        idx += n
        confusing = []
        for i in range(n):
            for j in range(i+1, n):
                dist = levenshtein_damerau(names[i], names[j], d)
                if dist <= d:
                    pair = tuple(sorted((names[i], names[j])))
                    confusing.append(pair)
        confusing.sort()
        for a,b in confusing:
            print(f"{a},{b}")
        print(len(confusing))

if __name__=="__main__":
    main()