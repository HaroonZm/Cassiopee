S = input()
maru = S.count('o')
print('YES' if maru + 15 - len(S) >= 8 else 'NO')