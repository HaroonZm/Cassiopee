table = [".,!? ", "abc", "def", "ghi","jkl",
        "mno", "pqrs", "tuv", "wxyz"]

n = int(raw_input())

for _ in range(n):
    msg = raw_input().replace("\r", "")
    ans = ""; j = 0; t = "";

    for i in msg:
        if i == "0":
            ans += t
            j = 0; t = ""
        else:
            t = table[int(i)-1][j]
            j += 1
            j %= len(table[int(i)-1])

    print ans