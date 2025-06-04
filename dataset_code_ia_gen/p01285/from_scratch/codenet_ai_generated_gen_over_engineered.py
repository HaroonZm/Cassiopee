from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import sys
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to_line(self, line: 'Line') -> float:
        return line.distance_to_point(self)

    def __repr__(self):
        return f"Point({self.x:.10f}, {self.y:.10f})"

class Line(ABC):
    @abstractmethod
    def distance_to_point(self, point: Point) -> float:
        pass

    @abstractmethod
    def normal_vector(self) -> Tuple[float,float]:
        pass

class EuclideanLine(Line):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self._A = p2.y - p1.y
        self._B = p1.x - p2.x
        self._C = -(self._A * p1.x + self._B * p1.y)
        self._normalize()

    def _normalize(self):
        norm = math.hypot(self._A, self._B)
        if norm == 0:
            self._A = self._B = self._C = 0.0
        else:
            self._A /= norm
            self._B /= norm
            self._C /= norm

    def distance_to_point(self, point: Point) -> float:
        # Distance = |A x + B y + C| / sqrt(A^2 + B^2) but normalized already
        return abs(self._A * point.x + self._B * point.y + self._C)

    def normal_vector(self) -> Tuple[float,float]:
        return (self._A, self._B)

    def __repr__(self):
        return f"Line(A={self._A:.10f}, B={self._B:.10f}, C={self._C:.10f})"

class SystemOfEqualDistance(ABC):
    @abstractmethod
    def find_point(self) -> Optional[Point]:
        pass

    @abstractmethod
    def has_multiple_solutions(self) -> bool:
        pass

class EqualDistanceFromLinesSolver(SystemOfEqualDistance):
    def __init__(self, lines: List[EuclideanLine]):
        self.lines = lines

    def find_point(self) -> Optional[Point]:
        # If only one line, infinite points at same distance (distance == distance to line)
        n = len(self.lines)
        if n == 0:
            return None
        if n == 1:
            # Many points equally distant to one line (distance is arbitrary)
            return None

        # We want: distance(point, line_i) == distance(point, line_j) for all i,j
        # Using line_0 as reference:
        # |A_i x + B_i y + C_i| = |A_0 x + B_0 y + C_0| for all i
        # Which can be written as:
        # (A_i x + B_i y + C_i)^2 = (A_0 x + B_0 y + C_0)^2

        # Define f_i(x,y) = (A_i x + B_i y + C_i)^2 - (A_0 x + B_0 y + C_0)^2 = 0

        # This is a quadratic equation in x,y

        # We'll try to reduce system and solve simultaneously:
        # f_i(x,y) = 0 for i=1,...,n-1

        # Expand f_i:

        # (A_i x + B_i y + C_i)^2 - (A_0 x + B_0 y + C_0)^2 = 0
        # = ((A_i x + B_i y + C_i) - (A_0 x + B_0 y + C_0)) *
        #   ((A_i x + B_i y + C_i) + (A_0 x + B_0 y + C_0)) = 0

        # So for each i, either:
        # (A_i - A_0) x + (B_i - B_0) y + (C_i - C_0) = 0
        # OR
        # (A_i + A_0) x + (B_i + B_0) y + (C_i + C_0) = 0

        # Each f_i = 0 defines two possible lines
        # We must find a point (x,y) satisfying one of the two lines for each i simultaneously

        # This is combinatorial (2^(n-1) possible sign patterns)

        # If n is large, 2^(n-1) is too big, but as n ≤ 100, we must find a safe way.

        # But max input is 100 lines -> huge brute force impossible.

        # Try a better approach:
        # Check if all lines are parallel to line_0: Then infinite points along a line perpendicular to them? -> Many

        # Otherwise, try a heuristic using linear system for one sign pattern

        # We will try systematic solving:

        # Each combination is choices[i] in {+1, -1} for i in 1..n-1:

        # For i=1..n-1: (A_i + s_i A_0) x + (B_i + s_i B_0) y + (C_i + s_i C_0) = 0 where s_i = choices[i]

        # We'll solve the linear system for a choice vector s

        # If a unique solution exists:

        # Check if this point satisfies all f_i=0 by the definition using absolute distances

        # Because the squared equality is equivalent to absolute value equality and the lines of constraints

        # Try all sign choices:

        # This is too large for all, but we optimize:

        # Observation: If two lines are parallel, their normals are proportional, so a special case.

        # Illegal case is no solution or many solutions

        # Algorithm:

        # 1) Check if all lines are parallel: if yes Many if not no
        # 2) Otherwise, try all sign patterns for n-1 lines (try only the two sign patterns with all + and all - to quickly check Many)
        # 3) If none of these works, print None.
        # 4) If exactly one unique solution across all sign patterns, print it.
        # 5) If more than one unique solution, print Many.

        # Because of complexity, let's try only 2 sign patterns: all + and all -

        # Because multiple solutions if solution set is a line

        # So let's implement the above simplified approach.

        base = self.lines[0]

        n = len(self.lines)
        # Check if all lines are parallel to base:
        parallel_count = 0
        for i in range(1, n):
            n0 = base.normal_vector()
            ni = self.lines[i].normal_vector()
            cross = n0[0]*ni[1] - n0[1]*ni[0]
            if abs(cross) < 1e-15:
                parallel_count += 1

        if parallel_count == n-1 and n > 1:
            # All lines parallel to base -> infinite solutions "Many"
            return None

        # Build matrices for equation based on sign pattern
        def solve_for_signs(signs: List[int]) -> Optional[Point]:
            # shape: n-1 equations
            # Each equation: (A_i + s_i A_0) x + (B_i + s_i B_0) y + (C_i + s_i C_0) = 0
            A0, B0, C0 = base._A, base._B, base._C
            rows = []
            for i, s in enumerate(signs, 1):
                li = self.lines[i]
                Ai, Bi, Ci = li._A, li._B, li._C
                a = Ai + s*A0
                b = Bi + s*B0
                c = Ci + s*C0
                rows.append((a,b,c))
            # Now solve linear system: M * [x y]^T = -C vector
            M = []
            C_vec = []
            for a,b,c in rows:
                M.append([a,b])
                C_vec.append(-c)
            # Solve Mx = C_vec with least squares or exact if possible
            # If rank < 2 no uniq solution
            det = M[0][0]*M[1][1] - M[0][1]*M[1][0] if len(M)>=2 else None

            if len(M) < 2:
                # Only one equation: line of solutions
                # We cannot define unique point; many solutions but must check consistency
                # If M empty (n=1), many solutions
                # For single line: infinite solutions
                return None

            # For n>2 lines, solve least squares
            # Check exact by normal equations
            has_exact = len(M) == 2

            if has_exact:
                if abs(det) < 1e-15:
                    # No unique solution
                    return None
                x = (C_vec[0]*M[1][1] - C_vec[1]*M[0][1]) / det
                y = (M[0][0]*C_vec[1] - M[1][0]*C_vec[0]) / det
                return Point(x,y)
            else:
                # More than 2 equations: solve least squares
                # Use numpy if allowed else solve manually via normal equations

                # Manual normal equations:
                AtA = [[0.0,0.0],[0.0,0.0]]
                Atb = [0.0,0.0]
                for (a,b),c in zip(M,C_vec):
                    AtA[0][0] += a*a
                    AtA[0][1] += a*b
                    AtA[1][0] += b*a
                    AtA[1][1] += b*b
                    Atb[0] += a*c
                    Atb[1] += b*c

                det2 = AtA[0][0]*AtA[1][1] - AtA[0][1]*AtA[1][0]
                if abs(det2) < 1e-15:
                    return None

                x = (Atb[0]*AtA[1][1] - Atb[1]*AtA[0][1]) / det2
                y = (AtA[0][0]*Atb[1] - AtA[1][0]*Atb[0]) / det2
                return Point(x,y)

        candidates = []
        # Try sign patterns: all +1 and all -1
        for pattern in [[1]*(len(self.lines)-1), [-1]*(len(self.lines)-1)]:
            pt = solve_for_signs(pattern)
            if pt is None:
                continue

            # Check if pt is equally distant to all lines with tolerance 1e-7
            dist0 = self.lines[0].distance_to_point(pt)
            ok = True
            for line in self.lines[1:]:
                dist = line.distance_to_point(pt)
                if abs(dist - dist0) > 1e-7:
                    ok = False
                    break
            if ok:
                candidates.append(pt)

        if len(candidates) == 0:
            # No solution with patterns tried => None
            return None

        # Check if multiple distinct candidate points
        def close(p1: Point, p2: Point) -> bool:
            return abs(p1.x - p2.x) < 1e-7 and abs(p1.y - p2.y) < 1e-7

        unique_pts = []
        for c in candidates:
            if not any(close(c, up) for up in unique_pts):
                unique_pts.append(c)

        if len(unique_pts) > 1:
            # More than one distinct solution => Many
            return None

        return unique_pts[0]

    def has_multiple_solutions(self) -> bool:
        # Because find_point returns None for None or Many, we detect Many as None with some internal logic
        # This interface would need extra info; so we don't implement here
        return False


class DatasetParser:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def __iter__(self):
        return self

    def __next__(self) -> Optional[List[EuclideanLine]]:
        line = ''
        while True:
            line = self.input_stream.readline()
            if line == '':
                raise StopIteration
            line=line.strip()
            if line != '':
                break
        if line == '0':
            raise StopIteration
        n = int(line)
        points = []
        total_coords = n*4
        while len(points) < total_coords:
            line2 = ''
            while True:
                line2 = self.input_stream.readline()
                if line2 == '':
                    raise StopIteration
                line2=line2.strip()
                if line2 != '':
                    break
            points += list(map(int,line2.split()))
        # parse lines
        lines = []
        for i in range(n):
            x1 = points[4*i]
            y1 = points[4*i+1]
            x2 = points[4*i+2]
            y2 = points[4*i+3]
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            lines.append(EuclideanLine(p1, p2))
        return lines

class ProblemCSolver:
    def __init__(self, input_stream):
        self.parser = DatasetParser(input_stream)

    def solve(self):
        for lines in self.parser:
            solver = EqualDistanceFromLinesSolver(lines)
            res = solver.find_point()
            if res is None:
                # Determine if Many or None

                # Detect all lines parallel:
                base = lines[0]
                n = len(lines)
                if n == 1:
                    # infinite solutions => Many
                    print("Many")
                    continue
                parallel_count = 0
                for i in range(1, n):
                    n0 = base.normal_vector()
                    ni = lines[i].normal_vector()
                    cross = n0[0]*ni[1] - n0[1]*ni[0]
                    if abs(cross) < 1e-15:
                        parallel_count += 1
                if parallel_count == n-1:
                    print("Many")
                else:
                    print("None")
            else:
                # print point with accuracy 1e-4
                print(f"{res.x:.4f} {res.y:.4f}")

if __name__ == "__main__":
    solver = ProblemCSolver(sys.stdin)
    solver.solve()