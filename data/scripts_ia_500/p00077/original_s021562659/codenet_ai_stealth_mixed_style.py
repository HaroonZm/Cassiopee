def process_line(char):
    ans = ""
    i = 0
    while i < len(char):
        if char[i] == "@":
            count = int(char[i+1])
            ans += char[:i]
            char = char[i+2]*count + char[i+3:]
            i = 0
        else:
            i += 1
    return ans + char

try:
    while 1:
        char = raw_input()
        if char == '':
            break
        result = process_line(char)
        print result
except EOFError:
    pass