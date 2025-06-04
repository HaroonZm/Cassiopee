N = int(input())
s1 = input()
s2 = input()

def count_characters(s):
    counts = {}
    for char in s:
        code = ord(char)
        if code in counts:
            counts[code] += 1
        else:
            counts[code] = 1
    freq = list(counts.values())
    freq.sort()
    freq = freq[::-1]
    return freq

counts1 = count_characters(s1)
counts2 = count_characters(s2)

result = 0
for a, b in zip(counts1, counts2):
    result += abs(a - b)

smallest = min(len(counts1), len(counts2))
result += sum(counts1[smallest:]) + sum(counts2[smallest:])

print(result // 2)