import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.hypot(self.x - p.x, self.y - p.y)

    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Line:
    # line given by two points p1 and p2
    # represented as ax + by + c = 0
    def __init__(self, p1, p2):
        self.a = p2.y - p1.y
        self.b = p1.x - p2.x
        self.c = -(self.a * p1.x + self.b * p1.y)

    def __repr__(self):
        return f"Line({self.a}x+{self.b}y+{self.c}=0)"

    def reflect(self, p):
        # reflect point p over this line
        # formula:
        # d = (a x0 + b y0 + c)/(a^2 + b^2)
        a,b,c = self.a,self.b,self.c
        x0,y0 = p.x,p.y
        d = (a*x0 + b*y0 + c)/(a*a + b*b)
        xr = x0 - 2*a*d
        yr = y0 - 2*b*d
        return Point(xr, yr)

def intersect_lines(l1, l2):
    # Solve l1: a1x + b1y + c1=0
    #       l2: a2x + b2y + c2=0
    a1,b1,c1 = l1.a,l1.b,l1.c
    a2,b2,c2 = l2.a,l2.b,l2.c
    det = a1*b2 - a2*b1
    # not parallel guaranteed by problem
    x = (b1*c2 - b2*c1)/det
    y = (a2*c1 - a1*c2)/det
    return Point(x,y)

class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.len = len(s)

    def peek(self):
        if self.pos < self.len:
            return self.s[self.pos]
        return ''

    def consume(self):
        ch = self.peek()
        if self.pos < self.len:
            self.pos += 1
        return ch

    def consume_spaces(self):
        while self.peek() == ' ':
            self.consume()

    def parse_expression(self):
        # <expression> ::= <point>
        return self.parse_point()

    def parse_point(self):
        # <point> ::= <point-factor> | <line> "@" <line-factor> | <line> "@" <point-factor> | <point> "@" <line-factor>
        # left-associative chain on '@' with point or line operands

        # parse left operand candidate:
        left = None
        # First parse either point-factor or line or point according to rules
        # But since <point> can be recursive, parse point-factor first
        if self.peek() == '(':
            # Could be point-factor or point in parentheses
            left = self.parse_point_factor()
        elif self.peek() == '\0' or self.peek() == '':
            # end of input? Shouldn't happen here
            left = self.parse_point_factor()
        else:
            # Try parse line or point?
            # Actually, all start with '(' or point-factor or line-factor.
            # So in BNF, <point> ::= ... but must start with '('
            # We'll parse point-factor here
            left = self.parse_point_factor()

        while True:
            self.consume_spaces()
            if self.peek() == '@':
                self.consume()  # consume '@'
                self.consume_spaces()

                # Determine right operand type by next token:
                # lookahead for '(' to parse <point-factor> or <line-factor> or <point> or <line>
                # We try parsing line first (line ::= <line-factor> | <point> '@' <point-factor>)
                # or point
                # Strategy:
                # Try parse line
                # if fail parse point

                save_pos = self.pos
                try:
                    right = self.parse_line_factor_or_line_or_point_factor()
                    # Now we have left and right
                    # Determine types: Point or Line
                    left_is_point = isinstance(left, Point)
                    left_is_line = isinstance(left, Line)
                    right_is_point = isinstance(right, Point)
                    right_is_line = isinstance(right, Line)

                    # now select op according to operand types
                    if left_is_point and right_is_point:
                        # two points -> line through them
                        # by problem statement distance > 1 always
                        left = Line(left, right)
                    elif left_is_point and right_is_line:
                        # (point) @ (line) -> symmetric point of the point about the line
                        # but syntax doesn't allow this, see BNF:
                        # <point> ::= ... | <point> "@" <line-factor>
                        # line-factor is (line) parenthesized line
                        # This case: yes
                        left = right.reflect(left)
                    elif left_is_line and right_is_point:
                        # <line> @ <point-factor> -> reflection of the point over line, but wait:
                        # line @ point-factor -> line @ point-factor <- line, point_factor => line-point op? no
                        # BNF says
                        # <point> ::= <line> "@" <point-factor>
                        # that yields a point symmetric to given point wrt line
                        # So operation line @ point-factor => symmetric point
                        # Our parse put right as point-factor (point) and left line, so reflect point over line
                        left = left.reflect(right)
                    elif left_is_line and right_is_line:
                        # two lines -> intersection point
                        left = intersect_lines(left, right)
                    else:
                        # else it's <point> "@" <line-factor> yields a point (symmetric)
                        # but if left is point and right line-factor (line) handled above
                        # Fall back: try to reflect if one point and one line? we should not end here.
                        # safety raise
                        raise ValueError("Invalid operands for '@'")
                except Exception:
                    # parsing right as line or point-factor failed, try parse point or line again
                    self.pos = save_pos
                    right = self.parse_point()

                    left_is_point = isinstance(left, Point)
                    left_is_line = isinstance(left, Line)
                    right_is_point = isinstance(right, Point)
                    right_is_line = isinstance(right, Line)

                    if left_is_point and right_is_point:
                        left = Line(left, right)
                    elif left_is_point and right_is_line:
                        left = right.reflect(left)
                    elif left_is_line and right_is_point:
                        left = left.reflect(right)
                    elif left_is_line and right_is_line:
                        left = intersect_lines(left, right)
                    else:
                        raise ValueError("Invalid operands for '@'")
            else:
                break
        return left

    def parse_point_factor(self):
        # <point-factor> ::= "(" <number> "," <number> ")" | "(" <point> ")"
        self.consume_spaces()
        if self.peek() != '(':
            raise ValueError("Expected '(' in point-factor")
        self.consume()  # '('
        self.consume_spaces()
        # check if next token is digit or '('
        c = self.peek()
        if c == '(':
            # nested point
            p = self.parse_point()
            self.consume_spaces()
            if self.consume() != ')':
                raise ValueError("Expected ')' after point in point-factor")
            return p
        else:
            # number ',' number ')'
            x = self.parse_number()
            self.consume_spaces()
            if self.consume() != ',':
                raise ValueError("Expected ',' in point-factor")
            self.consume_spaces()
            y = self.parse_number()
            self.consume_spaces()
            if self.consume() != ')':
                raise ValueError("Expected ')' in point-factor")
            return Point(x, y)

    def parse_line_factor(self):
        # <line-factor> ::= "(" <line> ")"
        self.consume_spaces()
        if self.peek() != '(':
            raise ValueError("Expected '(' in line-factor")
        self.consume()  # '('
        self.consume_spaces()
        line = self.parse_line()
        self.consume_spaces()
        if self.consume() != ')':
            raise ValueError("Expected ')' in line-factor")
        return line

    def parse_line(self):
        # <line> ::= <line-factor> | <point> '@' <point-factor>
        self.consume_spaces()
        if self.peek() == '(':
            # try line-factor first
            save_pos = self.pos
            try:
                return self.parse_line_factor()
            except Exception:
                self.pos = save_pos
        # else <point> '@' <point-factor>
        left = self.parse_point()
        self.consume_spaces()
        if self.peek() != '@':
            # not a line but line must contain '@' according to BNF here? Relax?
            raise ValueError("Expected '@' in line definition")
        self.consume()  # '@'
        self.consume_spaces()
        right = self.parse_point_factor()
        return Line(left, right)

    def parse_line_factor_or_line_or_point_factor(self):
        # helper to try to parse line-factor
        self.consume_spaces()
        if self.peek() == '(':
            save_pos = self.pos
            # try line-factor first
            try:
                return self.parse_line_factor()
            except Exception:
                self.pos = save_pos
                return self.parse_point_factor()
        else:
            return self.parse_point_factor()

    def parse_number(self):
        # <number> ::= <zero-digit> | <positive-number> | <negative-number>
        self.consume_spaces()
        neg = False
        if self.peek() == '-':
            neg = True
            self.consume()
        digits = ''
        if not self.peek().isdigit():
            raise ValueError("Expected digit in number")
        while self.peek().isdigit():
            digits += self.consume()
        if digits == '':
            raise ValueError("Expected digits in number")
        val = int(digits)
        if neg:
            val = -val
        return val

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        line = line.strip()
        if line == '#':
            break
        p = Parser(line)
        point = p.parse_expression()
        print(f"{point.x:.8f} {point.y:.8f}")

if __name__ == "__main__":
    main()