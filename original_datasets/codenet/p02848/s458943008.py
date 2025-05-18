n = int(input())
s = input()

def getChar(char, num):
    if num > 25:
        num %= 26

    if num + ord(char) > 90:
        num -= 26

    return chr(ord(char) + num)

result =""
for i in s:
    result += getChar(i, n)

print(result)