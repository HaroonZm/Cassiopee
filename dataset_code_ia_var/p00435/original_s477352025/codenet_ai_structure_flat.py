x = input()
n = 3
answer = ''
for letter in x:
    answer += chr(ord('A') + (ord(letter) - ord('A') - n) % 26)
print(answer)