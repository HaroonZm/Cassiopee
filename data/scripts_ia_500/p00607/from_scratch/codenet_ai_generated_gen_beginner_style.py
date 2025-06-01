lines = []
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    lines.append(line)

cursor_line = 0
cursor_pos = 0
buffer = None  # None means empty; str for string; '\n' for linefeed

def move_cursor_a():
    global cursor_pos
    cursor_pos = 0

def move_cursor_e():
    global cursor_pos
    cursor_pos = len(lines[cursor_line])

def move_cursor_p():
    global cursor_line, cursor_pos
    if cursor_line > 0:
        cursor_line -= 1
        if len(lines[cursor_line]) == 0:
            cursor_pos = 0
        else:
            cursor_pos = 0
    else:
        cursor_pos = 0

def move_cursor_n():
    global cursor_line, cursor_pos
    if cursor_line < len(lines) -1:
        cursor_line += 1
        if len(lines[cursor_line]) == 0:
            cursor_pos = 0
        else:
            cursor_pos = 0
    else:
        cursor_pos = 0

def move_cursor_f():
    global cursor_line, cursor_pos
    if cursor_pos < len(lines[cursor_line]):
        cursor_pos += 1
    else:
        if cursor_line < len(lines) - 1:
            cursor_line += 1
            cursor_pos = 0
        # else do nothing

def move_cursor_b():
    global cursor_line, cursor_pos
    if cursor_pos > 0:
        cursor_pos -= 1
    else:
        if cursor_line > 0:
            cursor_line -= 1
            cursor_pos = len(lines[cursor_line])
        # else do nothing

def command_d():
    global lines, cursor_line, cursor_pos
    if cursor_pos < len(lines[cursor_line]):
        # delete character at cursor
        lines[cursor_line] = lines[cursor_line][:cursor_pos] + lines[cursor_line][cursor_pos+1:]
    else:
        # cursor at end-of-line
        if cursor_line < len(lines) - 1:
            # append next line at end of current line
            lines[cursor_line] += lines[cursor_line+1]
            del lines[cursor_line+1]

def command_k():
    global buffer, lines, cursor_line, cursor_pos
    if cursor_pos == len(lines[cursor_line]):
        # cursor at end-of-line
        if cursor_line < len(lines) -1:
            command_d()
            buffer = '\n'
    else:
        # cut from cursor to end-of-line inclusive
        buffer = lines[cursor_line][cursor_pos:]
        lines[cursor_line] = lines[cursor_line][:cursor_pos]
        cursor_pos = len(lines[cursor_line])

def command_y():
    global buffer, lines, cursor_line, cursor_pos
    if buffer is None:
        return
    if buffer == '\n':
        # insert a new line at cursor position
        current_line = lines[cursor_line]
        left = current_line[:cursor_pos]
        right = current_line[cursor_pos:]
        lines[cursor_line] = left
        lines.insert(cursor_line + 1, right)
        cursor_line += 1
        cursor_pos = 0
    else:
        # insert the buffer string at cursor_pos
        current_line = lines[cursor_line]
        left = current_line[:cursor_pos]
        right = current_line[cursor_pos:]
        lines[cursor_line] = left + buffer + right
        cursor_pos += len(buffer)

while True:
    cmd = input()
    if cmd == '-':
        break
    if cmd == 'a':
        move_cursor_a()
    elif cmd == 'e':
        move_cursor_e()
    elif cmd == 'p':
        move_cursor_p()
    elif cmd == 'n':
        move_cursor_n()
    elif cmd == 'f':
        move_cursor_f()
    elif cmd == 'b':
        move_cursor_b()
    elif cmd == 'd':
        command_d()
    elif cmd == 'k':
        command_k()
    elif cmd == 'y':
        command_y()

for l in lines:
    print(l)