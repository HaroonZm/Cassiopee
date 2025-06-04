S = input()
num = len(S)
found = False

for i in range(num):
    left = S[:i]
    right = S[num - 7 + i:]
    combined = left + right
    if combined == "keyence":
        print("YES")
        found = True
        break

if not found:
    print("NO")