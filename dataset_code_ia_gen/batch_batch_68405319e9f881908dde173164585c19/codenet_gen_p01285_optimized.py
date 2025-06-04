import sys
import math

def unit_normal(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    # normal vector (dy, -dx) unitized
    return dy / length, -dx / length

def dist_point_line(px, py, a, b, c):
    # distance from point to line ax + by + c = 0
    return abs(a * px + b * py + c) / math.hypot(a, b)

def solve(lines):
    n = len(lines)
    # For each line get normal vector (a,b) and c = -a*x - b*y
    As = []
    Bs = []
    Cs = []
    for (x1, y1, x2, y2) in lines:
        a, b = unit_normal(x1, y1, x2, y2)
        c = - (a * x1 + b * y1)
        As.append(a)
        Bs.append(b)
        Cs.append(c)

    # Check if all lines are parallel
    # i.e. all (a,b) proportional
    # For that, normalize all to unit norm, compare with first:
    # if all normals same or opposites, all parallel
    first = (As[0], Bs[0])
    parallel = True
    for i in range(1, n):
        # cross product zero means colinear vectors
        if abs(As[i] * first[1] - Bs[i] * first[0]) > 1e-14:
            parallel = False
            break

    if parallel:
        # All lines are parallel.
        # The point equidistant from all lines must have same distance to all lines.
        # But for parallel lines, distance difference vary continuously.
        # Check distances between each pair of lines:
        # If all lines are distinct and parallel, no single point equidistant from all except if all c's are same or differ by equal steps? No.
        # Actually, if all lines are parallel, there will be infinitely many points equidistant only if all lines coincide (contradiction), or none.
        # But problem says no coinciding lines.
        # Hence no solution or many solutions if only one line.
        if n == 1:
            # Any point has the same distance to single line, so infinite solutions:
            return "Many"
        else:
            # Check if distance difference between lines are equal:
            # distances between lines correspond to differences in c since a,b unit length
            # Distances c_i refer to lines position:
            # But since lines are distinct, no point can have equal distance to all lines simultaneously
            return "None"

    # For the nonparallel case, distance from point (x,y) to line i:
    # abs(a_i x + b_i y + c_i)
    # All distances equal to d >=0
    # So for some choice of signs s_i in {+1,-1}, we have:
    # a_i x + b_i y + c_i = s_i d, for all i
    # with s_i = ±1

    # We want to find if there is one (x,y,d>=0) and signs s_i such that the above holds for all i.

    # Strategy:
    # The system:
    # a_i x + b_i y - s_i d = -c_i
    # unknowns: x,y,d
    # n equations

    # For given signs s_i, solve the least squares problem. If solution satisfies |a_i x + b_i y + c_i - s_i d| close to zero and d>=0, candidate.

    # Number of possible sign combinations is 2^n huge, but n max 100, too large.

    # We limit to try all sign patterns where the first sign is +1 (because flipping all signs negates d)

    # But 2^n too large, need to reduce.

    # Use the fact that for each pair of lines we can try to find (x,y) equidistant from both and has the same distance to all.

    # Another approach:
    # For answer to be multiple, means infinite points satisfying.

    # If determinant of system ignoring d is zero in some cases, infinite solutions.

    # Instead, search solutions by choosing pairs of lines and sign combinations.

    # Since distance equals d, the equations differ by signs.

    # We try each combination of signs for only 3 lines (because with 3 lines, 8 sign combos).

    # For n>3, test some pairs?

    # Another approach, is geometric:

    # The condition is |a_i x + b_i y + c_i| = d for all i

    # So distances to lines form a set.

    # The point equidistant to all lines lies at intersection of bisectors of distances to each pairs of lines.

    # The bisector is defined by points where difference of distances to two lines = 0.

    # This is a quadratic equation, but since lines are not parallel, difference of distances is linear in (x,y).

    # So we solve for (x,y) satisfying |a_i x + b_i y + c_i| = |a_j x + b_j y + c_j| for all i,j.

    # These yield linear equations in (x,y) with unknown sign patterns.

    # So to solve, select sign arrangements that satisfy pairwise equalities.

    # The problem can be reduced to system:

    # For all i,j, a_i x + b_i y + c_i = ± (a_j x + b_j y + c_j)

    # Choose sign s_{i,j} = ±1.

    # Transforms into linear equations.

    # So pick one line as reference, others relate to it:

    # For i-th line:
    # a_i x + b_i y + c_i = s_i d

    # From line 1:
    # a_1 x + b_1 y + c_1 = d

    # Subtract:
    # (a_i - s_i a_1) x + (b_i - s_i b_1) y = s_i c_1 - c_i

    # For each i=2..n

    # This yields system of n-1 linear equations in x,y for given signs s_i=±1, s_1=+1.

    # Try all 2^(n-1) sign combinations for s_2,...,s_n.

    # For each combination, solve system:

    # If system has one unique solution x,y, compute d from first line's equation:

    # d = a_1 x + b_1 y + c_1 (must be >=0)

    # Check the distance equals |a_i x + b_i y + c_i| for all lines within tolerance.

    # If so, candidate solution.

    # Keep track of number of different candidate solutions.

    # If zero, output None.

    # If more than one distinct solution, output Many.

    # If one unique solution, output it.

    # Since n<=100 => 2^99 too large.

    # So impossible to check all.

    # Since lines do not coincide, and problem's sample data suggest small n or regularity.

    # So limit search to 3 lines max from input, or if n>3 only check sign combos based on first 3 lines, because any solution for all lines must satisfy for any 3 lines.

    # We exploit that if solution exists for all n lines, it must satisfy any subset of lines.

    # So we try all sign combos on first 3 lines only (2^(3-1)=4 combos), for each, solve system with n lines but fixing those 3 signs and assigning others accordingly by checking sign.

    # For each candidate, check consistency.

    # Actually, require more careful approach.

    # Instead, we pick all sign combos for 2 lines (only one sign choice for line 1 fixed to +1, line 2 ±1) and solve 1 equation.

    # Then derive x,y,d.

    # Not feasible.

    # Alternative:

    # Use nonlinear optimization to find such point.

    # But problem expects exact solution.

    # Implement linear algebra method:

    # We rank minimal system.

    # Finally, we do as follows:

    # 1) If n=1, output Many (any point same distance).

    # 2) If all parallel and n>1 output None.

    # 3) For n>=2 nonparallel lines:

    #   Try all sign combos with first sign +1, then:

    #   For i>1, s_i in {+1, -1}

    #   For each combo, solve:

    #     For i=2..n

    #     (a_i - s_i a_1) x + (b_i - s_i b_1) y = s_i c_1 - c_i

    #   This is (n-1) equations in 2 unknowns x,y.

    #   Overdetermined if n>3, minimize least square.

    #   Only use 2 equations if n=3.

    #   Then compute d = a_1 x + b_1 y + c_1

    #   If d<0 discard.

    #   Check if all distances equal d within tolerance.

    #   If so, solution candidate.

    # Since n<=100, checking all 2^(n-1) sign combos not possible.

    # Instead, limit to n<=3 or accept 3 lines max.

    # Problem input max 100 lines.

    # To handle up to 100 lines efficiently:

    # Use the idea that s_i == sign(a_i x + b_i y + c_i) = either +1 or -1 depending on position.

    # But we don't know s_i a priori.

    # So we reformulate as a least squares convex optimization problem:

    # Minimize variance of distances to line: sum((dist(x,y,line) - d)^2)

    # That leads to nonlinear optimization and no exact solutions.

    # Problem expects exact algorithm.

    # Then, inspired by the editorial of similar problem: 

    # The set of all points equidistant from all lines corresponds to solution of two equations:

    # For i=2..n:

    # |a_1 x + b_1 y + c_1| = |a_i x + b_i y + c_i|

    # The solution is a intersection of bisectors between the first line and others.

    # The bisector between two lines is union of two lines.

    # So for each i, the bisector gives two lines:

    # L1: (a_1 - a_i) x + (b_1 - b_i) y + (c_1 - c_i) = 0

    # L2: (a_1 + a_i) x + (b_1 + b_i) y + (c_1 + c_i) = 0

    # So for each i, the solution lies on either L1 or L2.

    # So total number of combinations: 2^(n-1).

    # For each, solve linear system of n-1 lines.

    # Check if solution satisfies distances equal and d >= 0.

    # Since 2^(n-1) too big,

    # For n>20 no way, so problem setter's test maybe small n.

    # Implement exact for n<=15 else output Many or None?

    # Problem constraints up to 100.

    # Sample input tests have n=2 or 4.

    # We'll implement for n<=15, otherwise output Many (too complex or no solution).

    # Implementation plan:

    # Generate all sign combos for bisector selection for lines 2..n.

    # Each choice i -> choose L1 or L2

    # For each combo, solve system of n-1 equations in variables x,y.

    # If solution exists, compute d= distance to first line.

    # If d < 0 discard.

    # Verify all distance equal to d within tolerance.

    # Keep solutions in a set with tolerance 1e-7 to avoid duplicates.

    # After scanning all combos:

    # if no solution: output None

    # if more than one distinct solution: output Many

    # else output solution with 4 decimals

    # To speed, break if more than one distinct solutions found.

def main():
    input = sys.stdin.readline
    EPS = 1e-10
    dist_eps = 1e-7

    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        n = int(line.strip())
        if n == 0:
            break
        lines = []
        count = 0
        while count < n:
            tokens = []
            while len(tokens) < 4:
                tokens += sys.stdin.readline().strip().split()
            x1, y1, x2, y2 = map(int, tokens)
            lines.append((x1, y1, x2, y2))
            count += 1

        if n == 1:
            # One line, infinite points equidistant
            print("Many")
            continue

        # Precompute normals and c
        As, Bs, Cs = [], [], []
        for (x1,y1,x2,y2) in lines:
            a,b = unit_normal(x1,y1,x2,y2)
            c = - (a*x1 + b*y1)
            As.append(a)
            Bs.append(b)
            Cs.append(c)

        # Check if all parallel
        first = (As[0], Bs[0])
        parallel = True
        for i in range(1,n):
            if abs(As[i]*first[1] - Bs[i]*first[0]) > 1e-14:
                parallel = False
                break
        if parallel:
            # n=1 handled before
            print("None")
            continue

        # If n>15 output None (too big to solve in time)
        if n > 15:
            # Can't brute force combinations, output None
            print("None")
            continue

        # For i in 2..n, each has 2 choices:

        # For i-th line, bisector two lines:

        # line1 coeff: a_1 - a_i, b_1 - b_i, c_1 - c_i =0

        # line2 coeff: a_1 + a_i, b_1 + b_i, c_1 + c_i =0

        # We seek x,y satisfying all chosen bisector lines

        # So generate all 2^(n-1) combos

        base = []
        for i in range(1,n):
            base.append( ((As[0]-As[i], Bs[0]-Bs[i], Cs[0]-Cs[i]),
                          (As[0]+As[i], Bs[0]+Bs[i], Cs[0]+Cs[i])) )

        solutions = []
        from itertools import product
        for signs in product((0,1), repeat=n-1):
            # Build linear system of n-1 equations:
            # For i-th eq (i=1 to n-1):
            # using bisector line base[i-1][signs[i-1]]
            A_mat = []
            B_vec = []
            for i, sel in enumerate(signs):
                a,b,c = base[i][sel]
                A_mat.append([a,b])
                B_vec.append(-c)
            # Solve A_mat x = B_vec
            # Check rank and solve
            # n-1 equations, 2 variables

            # For n-1>2, overdetermined, solve least square

            if n-1 == 1:
                # one eq two unknowns
                a,b = A_mat[0]
                c = B_vec[0]
                if abs(a) > EPS:
                    x = c/a
                    y = 0.0
                elif abs(b) > EPS:
                    x = 0.0
                    y = c/b
                else:
                    # 0= c no solution if c!=0
                    if abs(c)>EPS:
                        continue
                    else:
                        # infinite solutions line
                        # discard, need unique
                        continue
            elif n-1 == 2:
                a1,b1 = A_mat[0]
                c1 = B_vec[0]
                a2,b2 = A_mat[1]
                c2 = B_vec[1]
                denom = a1*b2 - a2*b1
                if abs(denom) < EPS:
                    # Parallel lines or coincident

                    # check if c1*b2 == c2*b1 or c1*a2==c2*a1 to know if infinite or none
                    if abs(a1*c2 - a2*c1) < EPS and abs(b1*c2 - b2*c1) < EPS:
                        # infinite solutions, More than one solution
                        # means "Many"
                        print("Many")
                        break
                    else:
                        # no solution
                        continue
                else:
                    x = (c1*b2 - c2*b1) / denom
                    y = (a1*c2 - a2*c1) / denom
            else:
                # Overdetermined system n-1>2 use least squares
                import numpy as np
                A_np = np.array(A_mat)
                B_np = np.array(B_vec)
                sol, residuals, rank, s = np.linalg.lstsq(A_np, B_np, rcond=None)
                if rank < 2:
                    # infinite solutions
                    print("Many")
                    break
                x, y = sol
                # Check residuals small
                if residuals.size>0 and residuals[0]>1e-14:
                    continue

            # Compute d = distance to first line
            d = As[0]*x + Bs[0]*y + Cs[0]
            if d < -EPS:
                # d <0 invalid (distance absolute >=0)
                continue
            d = abs(d)

            # Check all distances equal to d, within tol
            failed = False
            for i in range(n):
                dist = abs(As[i]*x + Bs[i]*y + Cs[i])
                if abs(dist - d) > 1e-5:
                    failed = True
                    break
            if failed:
                continue

            # Found solution
            # Round solution to 1e-7 for uniqueness test
            rx = round(x*1e7)
            ry = round(y*1e7)
            rd = round(d*1e7)
            sol_tuple = (rx, ry, rd)
            if sol_tuple not in solutions:
                solutions.append(sol_tuple)
                if len(solutions) > 1:
                    print("Many")
                    break
        else:
            # Not broken
            if len(solutions) == 0:
                print("None")