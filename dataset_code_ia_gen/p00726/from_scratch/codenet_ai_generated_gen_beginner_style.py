def decompress_length(s):
    # Return the length of the decompressed string without decompressing whole string
    stack = []
    i = 0
    n = len(s)
    length = 0
    while i < n:
        if s[i].isdigit():
            # read number
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if i < n and s[i] == '(':
                # find matching ')'
                start = i + 1
                cnt = 1
                i += 1
                while i < n and cnt > 0:
                    if s[i] == '(':
                        cnt += 1
                    elif s[i] == ')':
                        cnt -= 1
                    i += 1
                end = i -1
                seq_len = decompress_length(s[start:end])
                length += num * seq_len
            else:
                # single letter after number
                length += num
                i += 1
        else:
            # normal letter
            length += 1
            i += 1
    return length

def char_at(s, index):
    # Return the character at decompressed string position index or '0' if out of range
    n = len(s)
    i = 0
    while i < n:
        if s[i].isdigit():
            # get repeat number
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if i < n and s[i] == '(':
                # get sequence inside parentheses
                i += 1
                start = i
                count_p = 1
                while i < n and count_p > 0:
                    if s[i] == '(':
                        count_p += 1
                    elif s[i] == ')':
                        count_p -= 1
                    i += 1
                end = i - 1
                seq_len = decompress_length(s[start:end])
                total_len = num * seq_len
                if index < total_len:
                    # find which repetition of sequence contains the index
                    index_in_seq = index % seq_len
                    return char_at(s[start:end], index_in_seq)
                else:
                    index -= total_len
            else:
                # single letter repeated
                if index < num:
                    return s[i]
                else:
                    index -= num
                i += 1
        else:
            # normal letter
            if index == 0:
                return s[i]
            index -= 1
            i += 1
    return '0'


while True:
    line = input()
    if line == '0 0':
        break
    s,i_str = line.split()
    i = int(i_str)
    print(char_at(s, i))