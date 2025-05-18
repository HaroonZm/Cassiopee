s = input()

stone = [s[0]] + [s[i] for i in range(1, len(s)) if s[i] != s[i - 1]]
print(len(stone) - 1)