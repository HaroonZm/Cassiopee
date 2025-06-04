class MultiColumnListProcessor:
    class PageFormat:
        def __init__(self, plen: int, cnum: int, width: int, cspace: int):
            self.plen = plen
            self.cnum = cnum
            self.width = width
            self.cspace = cspace
            # Validate combined width does not exceed constraints
            total_width = cnum * width + (cnum - 1) * cspace
            if total_width > 50 or plen < 1 or plen > 100 or cnum < 1 or width < 1 or cspace < 0:
                raise ValueError(f"Invalid page format parameters: plen={plen}, cnum={cnum}, width={width}, cspace={cspace}")

        def spacing_str(self) -> str:
            return '.' * self.cspace

    class InputText:
        def __init__(self, raw_lines):
            self.raw_lines = raw_lines
            # Preprocessing lines: empty lines must produce at least one empty output line
            # Non-empty lines may be wrapped

        def wrap_lines(self, width):
            wrapped_lines = []
            for line in self.raw_lines:
                if line == '':
                    # Single empty line output (dot-filled)
                    wrapped_lines.append('')
                else:
                    # Wrap lines that exceed width
                    start = 0
                    length = len(line)
                    while start < length:
                        wrapped_lines.append(line[start:start + width])
                        start += width
            return wrapped_lines

        def is_empty(self):
            # True if no input lines
            return len(self.raw_lines) == 0

    class Page:
        def __init__(self, wrapped_lines, fmt: 'MultiColumnListProcessor.PageFormat'):
            self.fmt = fmt
            self.wrapped_lines = wrapped_lines
            self.lines_per_page = fmt.plen * fmt.cnum
            # Chunk wrapped lines into pages of lines_per_page lines
            self.pages_lines = [
                wrapped_lines[i:i + self.lines_per_page]
                for i in range(0, len(wrapped_lines), self.lines_per_page)
            ]

        def format_page_lines(self, page_lines):
            # Fill missing lines with empty strings if needed to get full lines_per_page lines
            if len(page_lines) < self.lines_per_page:
                page_lines = page_lines + [''] * (self.lines_per_page - len(page_lines))

            # For mapping lines to columns:
            # Each column has plen lines
            # So index i-th line overall correspond to
            # row = i % plen, col = i // plen
            plen = self.fmt.plen
            cnum = self.fmt.cnum
            width = self.fmt.width
            cspace = self.fmt.cspace

            # Split lines into columns by groups of plen lines
            # Make a list of columns: each column is list of plen lines
            columns = [
                page_lines[i * plen:(i + 1) * plen]
                for i in range(cnum)
            ]

            # For each line of the page (plen lines), build the line by concatenating each column's line padded + dots + spacing dots
            lines_on_page = []
            for row in range(plen):
                row_items = []
                for col in range(cnum):
                    line = columns[col][row] if row < len(columns[col]) else ''
                    # Pad right to width with dots
                    padded = line.ljust(width, '.')
                    row_items.append(padded)
                # Between columns, insert spacing dots
                line_str = ('.' * cspace).join(row_items)
                # If the line is shorter than total page width, pad with dots (generally shouldn't happen)
                total_width = cnum * width + cspace * (cnum - 1)
                line_str = line_str.ljust(total_width, '.')
                lines_on_page.append(line_str)
            return lines_on_page

        def format_all_pages(self):
            all_pages = []
            for p_lines in self.pages_lines:
                formatted_lines = self.format_page_lines(p_lines)
                all_pages.append(formatted_lines)
            return all_pages

    def __init__(self):
        self.data_sets = []

    def parse_input(self, lines):
        # Parse multiple data sets
        idx = 0
        length = len(lines)
        data_sets = []
        while idx < length:
            line = lines[idx].strip()
            if line == '0':  # end condition
                break
            # try to parse plen:
            try:
                plen = int(line)
            except Exception:
                raise ValueError(f"Invalid plen integer at line {idx + 1}.")
            idx += 1
            if idx + 2 >= length:
                break
            cnum = int(lines[idx].strip())
            idx += 1
            width = int(lines[idx].strip())
            idx += 1
            cspace = int(lines[idx].strip())
            idx += 1

            # read input lines until '?'
            text_lines = []
            while idx < length:
                current_line = lines[idx].rstrip('\n')
                idx += 1
                if current_line == '?':
                    break
                # No characters except alphanumeric and empty lines allowed, but problem states they are guaranteed
                text_lines.append(current_line)
            data_sets.append((plen, cnum, width, cspace, text_lines))
        self.data_sets = data_sets

    def process_all(self):
        output_lines = []
        for (plen, cnum, width, cspace, text_lines) in self.data_sets:
            fmt = self.PageFormat(plen, cnum, width, cspace)
            input_text = self.InputText(text_lines)
            if input_text.is_empty():
                # No page output if text empty
                output_lines.append('?')
                continue
            wrapped = input_text.wrap_lines(fmt.width)
            pg = self.Page(wrapped, fmt)
            pages_formatted = pg.format_all_pages()
            for page_lines in pages_formatted:
                output_lines.extend(page_lines)
                output_lines.append('#')
            output_lines.append('?')
        return output_lines


def main():
    import sys
    lines = sys.stdin.readlines()
    processor = MultiColumnListProcessor()
    processor.parse_input(lines)
    result = processor.process_all()
    for l in result:
        print(l)

if __name__ == '__main__':
    main()