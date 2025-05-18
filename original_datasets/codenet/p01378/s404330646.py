s = input()
i = s.index("i")
s, t = "." + s[:i][::-1], "." + s[i + 3:]
s = s.translate(str.maketrans("(){}[]", ")(}{]["))
l = [[0 for _ in range(len(s))] for _ in range(len(t))]
for i in range(1, len(t)):
    for j in range(1, len(s)):
        if t[i] == s[j]:l[i][j] = l[i - 1][j - 1] + 1
        else:l[i][j] = max(l[i -1][j], l[i][j - 1])
print(3 + 2 * l[-1][-1])