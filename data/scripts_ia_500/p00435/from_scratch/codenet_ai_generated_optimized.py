s = input()
print(''.join(chr((ord(c)-68)%26+65) for c in s))