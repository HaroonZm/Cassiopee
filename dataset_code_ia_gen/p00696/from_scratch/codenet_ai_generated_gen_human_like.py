def wrap_line(line, width):
    """Wrap a line into multiple lines each with max length width."""
    wrapped = []
    for i in range(0, len(line), width):
        wrapped.append(line[i:i+width])
    if not wrapped:
        wrapped.append('')
    return wrapped

def fill_line(line, width):
    """Fill the line with '.' to make its length equal to width."""
    return line + '.' * (width - len(line))

def process_dataset(plen, cnum, width, cspace, lines):
    # First, wrap all input lines if longer than width
    wrapped_lines = []
    for l in lines:
        wrapped = wrap_line(l, width)
        wrapped_lines.extend(wrapped if wrapped else [''])
    if not wrapped_lines:
        # empty input text -> no page output
        return

    total_lines = plen * cnum
    pages = []
    # Pad wrapped_lines with empty line '' to fit pages, if needed
    n_pages = (len(wrapped_lines) + total_lines - 1) // total_lines
    # For each page, slice the lines
    for p in range(n_pages):
        page_lines = wrapped_lines[p*total_lines : (p+1)*total_lines]
        # Pad to total_lines if last page not full
        while len(page_lines) < total_lines:
            page_lines.append('')
        # Split page_lines into columns
        columns = []
        for c in range(cnum):
            col_start = c * plen
            col_end = col_start + plen
            col_lines = page_lines[col_start:col_end]
            columns.append(col_lines)
        # Now print row by row (plen lines)
        for row in range(plen):
            line_pieces = []
            for col in range(cnum):
                piece = columns[col][row]
                piece_filled = fill_line(piece, width)
                line_pieces.append(piece_filled)
                if col != cnum - 1:
                    line_pieces.append('.' * cspace)
            print(''.join(line_pieces))
        print('#')

def main():
    import sys
    input_lines = sys.stdin.read().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '0':
            break
        if not line.isdigit():
            # skip invalid line
            continue
        plen = int(line)
        if idx + 3 > len(input_lines):
            break
        cnum = int(input_lines[idx].strip())
        idx += 1
        width = int(input_lines[idx].strip())
        idx += 1
        cspace = int(input_lines[idx].strip())
        idx += 1
        # Read text lines until '?'
        text_lines = []
        while idx < len(input_lines):
            s = input_lines[idx]
            idx += 1
            if s == '?':
                break
            text_lines.append(s)
        process_dataset(plen, cnum, width, cspace, text_lines)
        print('?')

if __name__ == '__main__':
    main()