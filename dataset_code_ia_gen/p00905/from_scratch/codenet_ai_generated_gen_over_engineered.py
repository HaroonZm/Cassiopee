class IndentationStyle:
    def __init__(self, R: int, C: int, S: int):
        self.R = R
        self.C = C
        self.S = S

    def compute_indent(self, ro, rc, co, cc, so, sc):
        return self.R * (ro - rc) + self.C * (co - cc) + self.S * (so - sc)

    def __repr__(self):
        return f"IndentationStyle(R={self.R}, C={self.C}, S={self.S})"


class BracketCounter:
    def __init__(self):
        self.open_round = 0
        self.close_round = 0
        self.open_curly = 0
        self.close_curly = 0
        self.open_square = 0
        self.close_square = 0

    def update_from_line(self, line: str):
        for ch in line:
            if ch == '(':
                self.open_round += 1
            elif ch == ')':
                self.close_round += 1
            elif ch == '{':
                self.open_curly += 1
            elif ch == '}':
                self.close_curly += 1
            elif ch == '[':
                self.open_square += 1
            elif ch == ']':
                self.close_square += 1

    def prefix_tuple(self):
        return (self.open_round, self.close_round,
                self.open_curly, self.close_curly,
                self.open_square, self.close_square)

    def clone(self):
        bc = BracketCounter()
        bc.open_round = self.open_round
        bc.close_round = self.close_round
        bc.open_curly = self.open_curly
        bc.close_curly = self.close_curly
        bc.open_square = self.open_square
        bc.close_square = self.close_square
        return bc


class StylishProgram:
    def __init__(self, lines):
        self.lines = lines
        self.indentations = []
        self.bracket_counters = []

    def parse_indentations_and_prefixes(self):
        bc = BracketCounter()
        self.indentations = []
        self.bracket_counters = []
        for line in self.lines:
            indent = 0
            i = 0
            while i < len(line) and line[i] == '.':
                indent += 1
                i += 1
            self.indentations.append(indent)
            self.bracket_counters.append(bc.clone())
            bc.update_from_line(line[i:])


class StylishMasterFinder:
    def __init__(self, p_program: StylishProgram):
        self.p_program = p_program
        self.valid_styles = []

    def find_all_valid_styles(self):
        p = len(self.p_program.lines)
        self.p_program.parse_indentations_and_prefixes()
        for R in range(1, 21):
            for C in range(1, 21):
                for S in range(1, 21):
                    if self.is_style_valid(R, C, S):
                        self.valid_styles.append(IndentationStyle(R, C, S))

    def is_style_valid(self, R, C, S):
        # First line must have indentation 0 always
        if self.p_program.indentations[0] != 0:
            return False
        for i in range(1, len(self.p_program.lines)):
            prev_bc = self.p_program.bracket_counters[i]
            indent = R * (prev_bc.open_round - prev_bc.close_round) \
                     + C * (prev_bc.open_curly - prev_bc.close_curly) \
                     + S * (prev_bc.open_square - prev_bc.close_square)
            if indent != self.p_program.indentations[i]:
                return False
        return True


class StylishIndentator:
    def __init__(self, p_program: StylishProgram, q_program: StylishProgram, valid_styles):
        self.p_program = p_program
        self.q_program = q_program
        self.valid_styles = valid_styles

    def indent_lines(self):
        self.q_program.parse_indentations_and_prefixes()

        results = []
        for i in range(len(self.q_program.lines)):
            possible_indentations = set()
            bc = self.q_program.bracket_counters[i]
            ro = bc.open_round
            rc = bc.close_round
            co = bc.open_curly
            cc = bc.close_curly
            so = bc.open_square
            sc = bc.close_square
            for style in self.valid_styles:
                indent = style.compute_indent(ro, rc, co, cc, so, sc)
                possible_indentations.add(indent)
            if len(possible_indentations) == 1:
                results.append(possible_indentations.pop())
            else:
                results.append(-1)
        return results


def read_dataset():
    while True:
        line = ''
        while line.strip() == '':
            line = input()
        if not line:
            return None
        p, q = map(int, line.split())
        if p == 0 and q == 0:
            return None
        p_lines = []
        for _ in range(p):
            p_lines.append(input())
        q_lines = []
        for _ in range(q):
            q_lines.append(input())
        yield p_lines, q_lines


def main():
    while True:
        dataset = next(read_dataset(), None)
        if dataset is None:
            break
        p_lines, q_lines = dataset
        p_program = StylishProgram(p_lines)
        q_program = StylishProgram(q_lines)
        master_finder = StylishMasterFinder(p_program)
        master_finder.find_all_valid_styles()
        indentator = StylishIndentator(p_program, q_program, master_finder.valid_styles)
        indentations = indentator.indent_lines()
        print(' '.join(map(str, indentations)))


if __name__ == "__main__":
    main()