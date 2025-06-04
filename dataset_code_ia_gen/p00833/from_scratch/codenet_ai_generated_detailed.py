import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

def edges_of_polygon(vertices):
    """
    Given a list of vertices, return a set of edges.
    Each edge is represented as a tuple (min_vertex, max_vertex) to avoid duplicate edges.
    """
    edges = set()
    n = len(vertices)
    for i in range(n):
        a = vertices[i]
        b = vertices[(i+1)%n]
        # Ensure order for consistent edge representation
        if a < b:
            edges.add((a,b))
        else:
            edges.add((b,a))
    return edges

def read_map():
    """
    Read one map data from standard input.
    Returns:
      - territories: list of (country_name:str, list_of_vertices:[(x,y)])
      - num_territories: int
    """
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if not line:
            return 0, []
    n = int(line.strip())
    if n == 0:
        return 0, []
    territories = []
    for _ in range(n):
        # Read country name
        while True:
            country = sys.stdin.readline()
            if country is None:
                return 0, []
            country = country.strip()
            if country!='':
                break
        vertices = []
        while True:
            coord_line = sys.stdin.readline()
            if coord_line is None:
                break
            coord_line = coord_line.strip()
            if coord_line == '-1':
                break
            x_str, y_str = coord_line.split()
            x, y = int(x_str), int(y_str)
            vertices.append((x,y))
        territories.append((country, vertices))
    return n, territories

def build_adjacency(countries, territories, country_names):
    """
    Build adjacency graph between countries.
    countries: dict country_name -> list of polygons (each polygon is list of vertices)
    territories: input list for additional info, unused here but could be used for optimization
    country_names: list of country names for indexing
    Output: adjacency dict country_name -> set of adjacent country names
    """
    # For each country, gather all edges of all its territories
    country_edges = defaultdict(set)  # country_name -> set of edges
    
    for ctry, polys in countries.items():
        for poly in polys:
            country_edges[ctry].update(edges_of_polygon(poly))
            
    adjacency = defaultdict(set)
    names = list(countries.keys())
    n_countries = len(names)
    # For every pair of different countries, check if they share any edge
    for i in range(n_countries):
        c1 = names[i]
        edges1 = country_edges[c1]
        for j in range(i+1, n_countries):
            c2 = names[j]
            edges2 = country_edges[c2]
            # Check intersection of edges sets
            if edges1 & edges2:
                adjacency[c1].add(c2)
                adjacency[c2].add(c1)
    return adjacency

def can_color(country, color, assign, adjacency):
    """
    Check if it's safe to color the given country with 'color' given current assign.
    """
    for neighbor in adjacency[country]:
        if neighbor in assign and assign[neighbor] == color:
            return False
    return True

def backtrack(color_list, countries, adjacency, assign, index):
    """
    Try to color the countries with available colors from color_list.
    countries: list of country names in order
    assign: dict country_name -> assigned color index
    index: index of current country to color
    Returns True if success else False.
    """
    if index == len(countries):
        return True
    country = countries[index]
    
    for color in color_list:
        if can_color(country, color, assign, adjacency):
            assign[country] = color
            if backtrack(color_list, countries, adjacency, assign, index+1):
                return True
            del assign[country]  # backtrack
    return False

def solve_map(territories):
    """
    Given the list of territories (country_name, vertices), compute minimal colors needed.
    Approach:
      1. Group territories by countries.
      2. Build country adjacency based on shared edges.
      3. Try coloring countries with minimal colors by backtracking.
    """
    # Group territories by countries
    countries = defaultdict(list)  # country_name -> list of polygons
    country_set = set()
    for country, poly in territories:
        countries[country].append(poly)
        country_set.add(country)
    country_names = sorted(country_set)
    
    # Build adjacency graph
    adjacency = build_adjacency(countries, territories, country_names)
    
    # Try coloring from 1 up to 10 colors (max countries 10)
    for colors_count in range(1, 11):
        color_list = list(range(colors_count))
        assign = {}
        if backtrack(color_list, country_names, adjacency, assign, 0):
            return colors_count
    # fallback (should never reach here practically)
    return len(country_names)

def main():
    while True:
        n, territories = read_map()
        if n == 0:
            break
        result = solve_map(territories)
        print(result)

if __name__ == '__main__':
    main()