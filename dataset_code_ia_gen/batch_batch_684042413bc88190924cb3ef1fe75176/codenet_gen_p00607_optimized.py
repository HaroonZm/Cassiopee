lines = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    lines.append(list(s))
commands = []
while True:
    c = input()
    if c == '-':
        break
    commands.append(c)
buffer = None
cur_line = 0
cur_pos = 0
for cmd in commands:
    line = lines[cur_line]
    if cmd == 'a':
        cur_pos = 0
    elif cmd == 'e':
        cur_pos = len(line)
    elif cmd == 'p':
        if cur_line > 0:
            cur_line -= 1
            cur_pos = 0 if len(lines[cur_line])>0 else 0
        else:
            cur_pos = 0
    elif cmd == 'n':
        if cur_line < len(lines)-1:
            cur_line += 1
            cur_pos = 0 if len(lines[cur_line])>0 else 0
        else:
            cur_pos = 0
    elif cmd == 'f':
        if cur_pos < len(line):
            cur_pos += 1
        else:
            if cur_line < len(lines)-1:
                cur_line += 1
                cur_pos = 0
    elif cmd == 'b':
        if cur_pos > 0:
            cur_pos -= 1
        else:
            if cur_line > 0:
                cur_line -=1
                cur_pos = len(lines[cur_line])
    elif cmd == 'd':
        if cur_pos < len(line):
            del line[cur_pos]
        else:
            if cur_line < len(lines)-1:
                lines[cur_line].extend(lines[cur_line+1])
                del lines[cur_line+1]
    elif cmd == 'k':
        if cur_pos == len(line):
            if cur_line < len(lines)-1:
                # d command plus record linefeed
                lines[cur_line].extend(lines[cur_line+1])
                del lines[cur_line+1]
                buffer = '\n'
        else:
            buffer = ''.join(line[cur_pos:])
            del line[cur_pos:]
    elif cmd == 'y':
        if buffer is None:
            continue
        if buffer == '\n':
            new_line = lines[cur_line][cur_pos:]
            lines[cur_line] = lines[cur_line][:cur_pos]
            lines.insert(cur_line+1,new_line)
            cur_line += 1
            cur_pos = 0
        else:
            insert_chars = list(buffer)
            line[cur_pos:cur_pos] = insert_chars
            # Cursor stays pointing to character or end-of-line originally pointed
            # So cur_pos unchanged.
buffer = None
for line in lines:
    print(''.join(line))