import sys
import math

class Point:
    __slots__ = ('x','y')
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def __repr__(self):
        return f'P({self.x},{self.y})'
class Line:
    __slots__ = ('a','b','c')
    def __init__(self,p1,p2):
        # line through p1,p2: a x + b y + c =0
        self.a = p2.y - p1.y
        self.b = p1.x - p2.x
        self.c = -(self.a * p1.x + self.b * p1.y)
    def __repr__(self):
        return f'L({self.a}x+{self.b}y+{self.c}=0)'

def intersect(l1,l2):
    d = l1.a*l2.b - l2.a*l1.b
    x = (l2.c*l1.b - l1.c*l2.b)/d
    y = (l1.c*l2.a - l2.c*l1.a)/d
    return Point(x,y)

def symmetric_point(p,l):
    # reflect p about line l: project p on l, get p', then p_sym=2p'-p
    a,b,c = l.a,l.b,l.c
    d = a*a + b*b
    x0,y0 = p.x,p.y
    x = (b*b*x0 - a*b*y0 - a*c)/d
    y = (-a*b*x0 + a*a*y0 - b*c)/d
    return Point(2*x - x0, 2*y - y0)

class Parser:
    def __init__(self,s):
        self.s = s
        self.i = 0
        self.n = len(s)
    def peek(self):
        return self.s[self.i] if self.i < self.n else ''
    def eat(self,c=None):
        if c is None:
            ch = self.peek()
            self.i+=1
            return ch
        else:
            if self.peek()==c:
                self.i+=1
                return True
            else:
                return False
    def skip_spaces(self):
        while self.peek() in ' \t\n\r':
            self.i+=1
    def parse_number(self):
        # number: digit or -digit+
        self.skip_spaces()
        start = self.i
        if self.peek()=='-':
            self.i+=1
        while self.peek().isdigit():
            self.i+=1
        return int(self.s[start:self.i])
    def parse_point_factor(self):
        # (number,number) or (point)
        self.skip_spaces()
        if not self.eat('('):
            return None
        self.skip_spaces()
        if self.peek()=='(' or self.peek()=='-':
            # nested point
            if self.peek()=='(':
                pt = self.parse_point()
            else:
                # Try parse number, if comma after, parse number
                # Direct coordinates (x,y)
                x = self.parse_number()
                self.skip_spaces()
                if self.eat(','):
                    y = self.parse_number()
                    pt = Point(x,y)
                else:
                    # no comma, nested point ?
                    pt = Point(x,0)
            self.skip_spaces()
            self.eat(')')
            return pt
        else:
            # parse number, comma, number
            x = self.parse_number()
            self.skip_spaces()
            self.eat(',')
            self.skip_spaces()
            y = self.parse_number()
            self.skip_spaces()
            self.eat(')')
            return Point(x,y)
    def parse_line_factor(self):
        self.skip_spaces()
        if self.peek()!='(':
            return None
        self.i+=1
        ln = self.parse_line()
        self.skip_spaces()
        self.eat(')')
        return ln
    def parse_point(self):
        # point ::= point_factor | line "@" line_factor | line "@" point_factor | point "@" line_factor
        self.skip_spaces()
        # parse point_factor or point
        # point_factor can be (number,number), (point)
        # First parse point_factor or line or point
        c = self.peek()
        if c=='(':
            # could be point_factor or point or line_factor
            # try point_factor 
            backup = self.i
            pt = self.parse_point_factor()
            if pt is None:
                self.i=backup
                pt = self.parse_point()
            cur=self.process_suffix_point(pt)
            return cur
        elif c=='-': # number start
            pt = self.parse_point_factor()
            cur=self.process_suffix_point(pt)
            return cur
        else:
            # start with something else, parse point as rec
            pt = self.parse_point_factor()
            if pt is None:
                pt = self.parse_point()
            cur=self.process_suffix_point(pt)
            return cur
    def process_suffix_point(self,left):
        # try to parse "@" with line or point_factor or line_factor on right
        while True:
            self.skip_spaces()
            if self.peek()!='@':
                return left
            self.i+=1
            # now parse right operand depending on left type
            if isinstance(left,Point):
                # right can be line_factor or point_factor
                self.skip_spaces()
                if self.peek()=='(':
                    # try line_factor first
                    backup = self.i
                    ln = self.parse_line_factor()
                    if ln is not None:
                        # point @ line_factor => symm_point
                        left = symmetric_point(left,ln)
                        continue
                    else:
                        self.i=backup
                        pt = self.parse_point_factor()
                        left = symmetric_point(left,Line(pt,left)) if False else left # never used, fallback
                        left = pt
                        continue
                else:
                    # maybe line or point_factor
                    ln = self.parse_line()
                    left = symmetric_point(left,ln)
                    continue
            elif isinstance(left,Line):
                # right can be point_factor or line_factor (after line)
                self.skip_spaces()
                # try line_factor
                backup = self.i
                ln2 = self.parse_line_factor()
                if ln2 is not None:
                    # line @ line_factor => intersection point
                    left = intersect(left,ln2)
                    continue
                else:
                    self.i=backup
                    # parse point_factor
                    pt = self.parse_point_factor()
                    if pt is not None:
                        # line @ point_factor => symmetrical point
                        left = symmetric_point(pt,left)
                        continue
                    else:
                        # parse line (two points)
                        ln2 = self.parse_line()
                        if ln2 is not None:
                            left = intersect(left,ln2)
                            continue
                        # fallback
                        # error (should not happen)
                        return left
            else:
                # already a point/result
                return left
    def parse_line(self):
        # line ::= line_factor | point "@" point_factor
        self.skip_spaces()
        if self.peek()=='(':
            backup=self.i
            ln = self.parse_line_factor()
            if ln is not None:
                return ln
            self.i=backup
        # parse point @ point_factor
        p1 = self.parse_point()
        self.skip_spaces()
        if self.peek()!='@':
            # not line
            return p1
        self.i+=1
        p2 = self.parse_point_factor()
        return Line(p1,p2)

for line in sys.stdin:
    line=line.strip()
    if line=='#': break
    p=Parser(line)
    pt=p.parse_point()
    print(f"{pt.x:.8f} {pt.y:.8f}")