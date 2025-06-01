import sys

def decode_caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            # shift letters backwards by shift
            new_char = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            result += new_char
        else:
            result += c
    return result

words_to_find = ["the", "this", "that"]

for line in sys.stdin:
    line = line.rstrip('\n')
    for shift in range(26):
        decoded = decode_caesar(line, shift)
        # check if any of the words appear as full words in decoded text
        # to keep it simple, just check if substring present
        found = False
        for w in words_to_find:
            if w in decoded:
                found = True
                break
        if found:
            print(decoded)
            break