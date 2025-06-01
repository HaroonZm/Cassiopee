s=input()
print(''.join(chr((ord(c)-ord('D'))%26+ord('A')) for c in s))