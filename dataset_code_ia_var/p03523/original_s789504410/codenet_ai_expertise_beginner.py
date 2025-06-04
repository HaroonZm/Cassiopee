S = input()
found = False
n = 4
positions = [0, 4, 6, 8]

for i in range(16):
    word = ["A", "K", "I", "H", "A", "B", "A", "R", "A"]
    for j in range(n):
        if (i >> j) & 1:
            word[positions[j]] = ""
    temp = "".join(word)
    if temp == S:
        print("YES")
        found = True
        break

if not found:
    print("NO")