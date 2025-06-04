s = input()
print(''.join(chr((ord(c)-ord('A')-3)%26+ord('A')) for c in s))