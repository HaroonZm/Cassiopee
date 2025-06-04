n = int(input())
for _ in range(n):
    text = input()
    M = int(input())
    cursor = 0  # cursor position: between characters; 0 means before first character
    for __ in range(M):
        cmd = input()
        if cmd == "forward char":
            if cursor < len(text):
                cursor += 1
        elif cmd == "backward char":
            if cursor > 0:
                cursor -= 1
        elif cmd == "forward word":
            # move cursor to end of leftmost word in the right
            # words delimited also by cursor and blanks
            right = text[cursor:]
            if not right:
                continue
            i = 0
            n_right = len(right)
            # skip blanks first
            while i < n_right and right[i] == ' ':
                i += 1
            if i == n_right:
                cursor = len(text)
                continue
            # now i is at start of first right word
            # move i to end of word (until blank or end)
            while i < n_right and right[i] != ' ':
                i += 1
            cursor += i
        elif cmd == "backward word":
            # move cursor to beginning of rightmost word in the left
            left = text[:cursor]
            if not left:
                continue
            i = len(left) - 1
            # skip blanks backward
            while i >= 0 and left[i] == ' ':
                i -= 1
            if i < 0:
                cursor = 0
                continue
            # now i at last char of word before cursor
            # move i backward to beginning of word
            while i >= 0 and left[i] != ' ':
                i -= 1
            cursor = i + 1
        elif cmd.startswith("insert "):
            # extract text in quotes
            idx1 = cmd.find('"')
            idx2 = cmd.rfind('"')
            ins_text = cmd[idx1+1:idx2]
            text = text[:cursor] + ins_text + text[cursor:]
            cursor += len(ins_text)
        elif cmd == "delete char":
            # delete char right next to cursor if exists
            if cursor < len(text):
                text = text[:cursor] + text[cursor+1:]
        elif cmd == "delete word":
            # delete leftmost word in the right of the cursor plus blanks just after cursor
            right = text[cursor:]
            if not right:
                continue
            # count blanks after cursor
            i = 0
            while i < len(right) and right[i] == ' ':
                i += 1
            if i == len(right):
                # only blanks to right, delete them all
                text = text[:cursor]
                continue
            # now at start of first word
            j = i
            while j < len(right) and right[j] != ' ':
                j += 1
            # delete from cursor to cursor + j
            text = text[:cursor] + right[j:]
        else:
            # unknown command, ignore
            pass

    # print text with cursor as ^
    print(text[:cursor] + '^' + text[cursor:])