import sys

def decrypt(text, shift):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(ch)
    return ''.join(result)

def contains_keyword(text):
    keywords = ["the", "this", "that"]
    return any(k in text for k in keywords)

for line in sys.stdin:
    line = line.rstrip('\n')
    for shift in range(26):
        decoded = decrypt(line, shift)
        if contains_keyword(decoded):
            print(decoded)
            break