import sys

def decode_caesar(text, shift):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            # Shift character backward by shift positions
            shifted = ord(ch) - shift
            if shifted < ord('a'):
                shifted += 26
            result.append(chr(shifted))
        else:
            result.append(ch)
    return ''.join(result)

def contains_key_words(text):
    return any(word in text for word in ["the", "this", "that"])

for line in sys.stdin:
    line = line.rstrip('\n')
    for shift in range(26):
        decoded = decode_caesar(line, shift)
        if contains_key_words(decoded):
            print(decoded)
            break