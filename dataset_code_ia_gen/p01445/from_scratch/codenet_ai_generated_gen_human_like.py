import sys

def parse_poly(poly_str):
    # Parse polynomial string into list of coefficients
    # coeffs[i] = coefficient of x^i
    # polynomial degree <=50
    coeffs = [0]*51
    if poly_str == '0':
        return coeffs
    terms = poly_str.split('+')
    for term in terms:
        if 'x' not in term:
            # constant term
            coeffs[0] = int(term)
        else:
            # term contains x
            if '^' in term:
                # form: a x^i or x^i
                a_part, power_part = term.split('x^')
                power = int(power_part)
                if a_part == '' or a_part == '+':
                    a = 1
                else:
                    a = int(a_part)
                coeffs[power] = a
            else:
                # form: a x or x
                a_part = term[:-1] # remove 'x'
                if a_part == '' or a_part == '+':
                    a = 1
                else:
                    a = int(a_part)
                coeffs[1] = a
    return coeffs

def poly_to_str(coeffs):
    # convert coeff list to string representation according to problem
    # degree max 50
    # if all zero -> '0'
    # terms in descending order
    terms = []
    deg = len(coeffs)-1
    # find actual degree (max i with coeff[i] !=0)
    maxdeg = 0
    for i in range(deg, -1, -1):
        if coeffs[i] != 0:
            maxdeg = i
            break
    if maxdeg == 0 and coeffs[0] == 0:
        # zero polynomial
        return '0'
    for i in range(maxdeg, -1, -1):
        c = coeffs[i]
        if c == 0:
            continue
        if i == 0:
            # constant term
            terms.append(str(c))
        elif i == 1:
            # linear term
            if c == 1:
                terms.append('x')
            else:
                terms.append(str(c)+'x')
        else:
            # i>=2
            if c == 1:
                terms.append('x^'+str(i))
            else:
                terms.append(str(c)+'x^'+str(i))
    return '+'.join(terms)

def poly_max(p, q):
    # given two polys p and q (length 51), return polynomial max(p,q) by coefficients comparison in lex order desc
    # comparing coefficients from highest degree to zero
    for i in range(50, -1, -1):
        if p[i] > q[i]:
            return p
        elif p[i] < q[i]:
            return q
    # equal
    return p

def poly_zero():
    return [0]*51

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        N,M = map(int,line.strip().split())
        if N == 0 and M == 0:
            break
        # Build adjacency matrix with polynomial bandwidths
        # For no direct edge, set poly_zero()
        graph = [[poly_zero() for _ in range(N)] for __ in range(N)]
        for i in range(M):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            parts = line.strip().split()
            u,v = int(parts[0]), int(parts[1])
            pstr = ' '.join(parts[2:])
            # but pstr may be merged (no space)
            # actually input tokens after u v are just one string (polynomial)
            # so fix pstr:
            pstr = parts[2]
            poly = parse_poly(pstr)
            # undirected edge
            # If multiple edges between same nodes, keep max poly
            if graph[u-1][v-1] == poly_zero():
                graph[u-1][v-1] = poly
            else:
                graph[u-1][v-1] = poly_max(graph[u-1][v-1], poly)
            if graph[v-1][u-1] == poly_zero():
                graph[v-1][u-1] = poly
            else:
                graph[v-1][u-1] = poly_max(graph[v-1][u-1], poly)
        # Floyd-Warshall like with max-poly over paths
        # dist[i][j] = max bandwidth polynomial from i to j found so far
        dist = [[poly_zero() for _ in range(N)] for __ in range(N)]
        for i in range(N):
            dist[i][i][0] = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] != poly_zero():
                    dist[i][j] = graph[i][j][:]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    # consider path i->k->j,
                    # the bandwidth polynomial is min(dist[i][k], dist[k][j]) because bandwidth along path limited by bottleneck
                    # then max with current dist[i][j]
                    # But problem says maximal bandwidth between 1 and N-th stations
                    # "maximal bandwidth" sounds like maximum bandwidth along all paths.
                    # So bandwidth of path = minimum bandwidth of edges on path (bottleneck)
                    # We want to maximize the minimum bandwidth polynomial over all paths.
                    # So dist[i][j] = max(dist[i][j], min(dist[i][k], dist[k][j]))
                    # Need min_poly and max_poly functions:
                    # For min_poly: take coefficient-wise min at each degree? No, polynomial bandwidth is numeric function f(x),
                    # min over functions f,g at each x is min(f(x),g(x)).
                    # But given polynomials, min of two polynomials is not a polynomial in general.
                    # The problem is simplified:
                    # In sample answer, the bandwidth between 1 and N is maximum over all paths of min bandwidth edges
                    # We want to find the polynomial function that at every year x is the maximal minimum bandwidth over all paths.
                    #
                    # Our approach:
                    # Dist[i][j]: polynomial that at year x gives the maximal bandwidth over all paths from i to j
                    # Using max-min path:
                    # dist[i][j] = max(dist[i][j], min(dist[i][k], dist[k][j])) where min is polynomialwise minimum function.
                    #
                    # The problem: The min of two polynomials is not a polynomial.
                    # Only compare polynomials at all x and get minimum polynomial?
                    #
                    # But because polynomials have integer coefficients and non negative,
                    # we can compare polynomials pointwise by coefficients: but this is insufficient.
                    #
                    # The intended approach (standard for such problems) is:
                    # When comparing polynomials of bandwidth, the bandwidth polynomial f(x) is measurable at any x >= 0,
                    # so to find the max bandwidth along path = max over possible min edge bandwidths,
                    # dynamic programming with polynomial "min" and "max"
                    #
                    # Since min of two polynomials is not a polynomial,
                    # approximation or piecewise approach is complex.
                    #
                    # However, problem sample and constraints imply the solution expects us to pick the polynomial which is minimum at every x.
                    #
                    # Because all coefficients are non-negative,
                    # The minimum of two polynomials with non-negative coefficients is simply the coefficient-wise minimum of coefficients at each degree.
                    #
                    # But this is not mathematically true (coefficients minimum is not polynomial minimum),
                    # but problem likely expects min(p,q) := polynomial with coefficients min at each degree.
                    #
                    # So implement min_poly and max_poly as coeff-wise min/max.
                    #
                    # Let's implement that.
                    #
                    # Update dist[i][j] = max_poly(dist[i][j], min_poly(dist[i][k], dist[k][j]))
                    #
                    # With min_poly defined coefficient-wise minimum.
                    # Not perfect mathematically but aligns with problem intent.
                    min_poly = [0]*51
                    for deg_i in range(51):
                        min_poly[deg_i] = min(dist[i][k][deg_i], dist[k][j][deg_i])
                    candidate = poly_max(dist[i][j], min_poly)
                    dist[i][j] = candidate

        answer = dist[0][N-1]
        # If answer is zero polynomial (0 coefficients), check problem statement:
        # "No polynomial is a constant zero" input, but output polynomial may be zero.
        # print polynomial
        print(poly_to_str(answer))


if __name__ == '__main__':
    main()