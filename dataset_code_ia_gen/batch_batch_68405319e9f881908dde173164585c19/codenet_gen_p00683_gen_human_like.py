def main():
    import sys
    input = sys.stdin.readline

    def split_words(text, cursor_pos):
        # Returns two lists of word boundaries: words left of cursor, words right of cursor
        # A word is a sequence of non-space characters delimited by spaces or cursor
        # We need to know the positions of words relative to text to move cursor.

        # Left of cursor
        left_part = text[:cursor_pos]
        right_part = text[cursor_pos:]

        # Find words in left part
        left_words = []
        start = None
        for i, c in enumerate(left_part):
            if c != ' ':
                if start is None:
                    start = i
            else:
                if start is not None:
                    left_words.append((start, i))
                    start = None
        if start is not None:
            left_words.append((start, len(left_part)))

        # Find words in right part
        right_words = []
        start = None
        for i, c in enumerate(right_part):
            if c != ' ':
                if start is None:
                    start = i
            else:
                if start is not None:
                    right_words.append((start, i))
                    start = None
        if start is not None:
            right_words.append((start, len(right_part)))

        return left_words, right_words

    def forward_char(text, cursor):
        if cursor < len(text):
            return cursor + 1
        return cursor

    def backward_char(cursor):
        if cursor > 0:
            return cursor - 1
        return cursor

    def forward_word(text, cursor):
        left_words, right_words = split_words(text, cursor)
        if not right_words:
            return len(text)
        else:
            # move cursor to the end of the leftmost word in right part
            start, end = right_words[0]
            # position in text is cursor + end
            return cursor + end

    def backward_word(text, cursor):
        left_words, right_words = split_words(text, cursor)
        if not left_words:
            return 0
        else:
            # move cursor to the beginning of the rightmost word in left part
            start, end = left_words[-1]
            return start

    def insert_text(text, cursor, ins):
        return text[:cursor] + ins + text[cursor:], cursor + len(ins)

    def delete_char(text, cursor):
        # delete character right next to cursor if exists
        if cursor < len(text):
            return text[:cursor] + text[cursor+1:]
        return text

    def delete_word(text, cursor):
        left_words, right_words = split_words(text, cursor)
        if not right_words:
            return text
        # delete blanks between cursor and leftmost word in right part (if any)
        # Find number of blanks after cursor and before word start:
        first_word_start = cursor + right_words[0][0]
        i = cursor
        while i < first_word_start and text[i] == ' ':
            i += 1
        delete_start = cursor
        delete_end = cursor + right_words[0][1]  # end of the word in right part
        return text[:delete_start] + text[delete_end:]

    N = int(input())
    for _ in range(N):
        text = input().rstrip('\n')
        cursor = 0  # initially at beginning
        M = int(input())
        for __ in range(M):
            line = input().rstrip('\n')
            parts = line.split(' ', 1)
            cmd = parts[0]
            if cmd == 'forward':
                arg = parts[1]
                if arg == 'char':
                    cursor = forward_char(text, cursor)
                elif arg == 'word':
                    cursor = forward_word(text, cursor)
            elif cmd == 'backward':
                arg = parts[1]
                if arg == 'char':
                    cursor = backward_char(cursor)
                elif arg == 'word':
                    cursor = backward_word(text, cursor)
            elif cmd == 'insert':
                # format is insert "any-text"
                arg = parts[1]
                # extract string inside quotes
                ins_text = arg[1:-1]
                text, cursor = insert_text(text, cursor, ins_text)
            elif cmd == 'delete':
                arg = parts[1]
                if arg == 'char':
                    text = delete_char(text, cursor)
                elif arg == 'word':
                    text = delete_word(text, cursor)
        # print final text with cursor as '^'
        print(text[:cursor] + '^' + text[cursor:])

if __name__ == '__main__':
    main()