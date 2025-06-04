s = input()
n = len(s)
found = False

for i in range(n):
    for j in range(i, n):
        part1 = s[:i]
        part2 = s[j:]
        new_str = part1 + part2
        if new_str == "keyence":
            print("YES")
            found = True
            break
    if found:
        break

if not found:
    print("NO")