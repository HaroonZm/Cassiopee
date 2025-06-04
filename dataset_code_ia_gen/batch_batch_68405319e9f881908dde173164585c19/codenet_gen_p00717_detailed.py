import sys

def normalize_shape(points):
    """
    Normalize the shape of a polygonal line given by points list.
    The normalization involves:
    - Representing the polygonal line as a sequence of vectors (dx, dy)
      between consecutive vertices.
    - Rotating the shape to four possible orientations (0°, 90°, 180°, 270°)
      by applying rotation transformation to vectors.
    - Normalize each orientation by translating to start at (0,0).
    - Also consider the reversed order as valid.
    - Return the lexicographically smallest sequence of coordinates among all
      these transformations to uniquely identify the shape.
    """
    # Compute vector differences between consecutive points
    vectors = []
    for i in range(1, len(points)):
        dx = points[i][0] - points[i-1][0]
        dy = points[i][1] - points[i-1][1]
        vectors.append((dx, dy))
    
    # Function to reconstruct points from vectors starting at (0,0)
    def vectors_to_points(vs):
        pts = [(0, 0)]
        for dx, dy in vs:
            x, y = pts[-1]
            pts.append((x + dx, y + dy))
        return pts
    
    # Rotation functions (rotate vectors by 90°, 180°, 270°)
    def rotate_90(vs):
        # (x, y) -> (-y, x)
        return [(-dy, dx) for dx, dy in vs]
    def rotate_180(vs):
        # (x, y) -> (-x, -y)
        return [(-dx, -dy) for dx, dy in vs]
    def rotate_270(vs):
        # (x, y) -> (y, -x)
        return [(dy, -dx) for dx, dy in vs]
    
    # Generate all orientations of vectors: 0°, 90°, 180°, 270°
    orientations = [
        vectors,
        rotate_90(vectors),
        rotate_180(vectors),
        rotate_270(vectors)
    ]
    
    # For each orientation, also consider reversed vectors (reverse the vector list and negate vectors)
    # Because reversing means traversing in reverse order from end point to start point.
    def reverse_vectors(vs):
        # Reverse order and invert directions
        return [(-dx, -dy) for dx, dy in reversed(vs)]
    
    all_variants = []
    for ori in orientations:
        all_variants.append(orientation_points := vectors_to_points(ori))
        all_variants.append(reverse_points := vectors_to_points(reverse_vectors(ori)))
    
    # For each variant (list of points), translate so that first point is at (0,0)
    # Then get a tuple of coordinates to use as canonical representation
    def translate_to_zero(pts):
        x0, y0 = pts[0]
        return tuple((x - x0, y - y0) for x, y in pts)
    
    normalized_variants = [translate_to_zero(v) for v in all_variants]
    
    # Return lex smallest tuple to have a unique canonical representation of this polygonal line shape
    return min(normalized_variants)

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':
            # End of input
            break
        n = int(n_line)
        polygonal_lines = []
        for _ in range(n+1):
            m = int(input_lines[idx].strip())
            idx += 1
            coords = []
            for __ in range(m):
                x, y = map(int, input_lines[idx].split())
                idx += 1
                coords.append((x, y))
            polygonal_lines.append(coords)
        
        # polygonal_lines[0] is template
        template_shape = normalize_shape(polygonal_lines[0])
        
        results = []
        # Check which polygonal lines have the same shape as the template [1..n] with numbering 1..n
        for i in range(1, n+1):
            shape = normalize_shape(polygonal_lines[i])
            if shape == template_shape:
                results.append(i)
        
        # Output results in ascending order, one per line
        for r in sorted(results):
            print(r)
        print("+++++")

if __name__ == '__main__':
    main()