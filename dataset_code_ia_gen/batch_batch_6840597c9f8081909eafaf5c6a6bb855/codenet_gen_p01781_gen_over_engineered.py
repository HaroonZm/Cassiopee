class Dimension:
    def __init__(self, size: int, origin: int):
        self.size = size
        self.origin = origin
        self.min_dist = None
        self.max_dist = None
        self.dist_count = {}

    def compute_distances(self):
        # Distance range in this dimension: from origin to edges
        self.min_dist = 0
        self.max_dist = max(self.origin, self.size - 1 - self.origin)
        # For each possible distance d in [min_dist ... max_dist], count how many positions have this distance
        dist_count = {}
        # Positions with distance d:
        # If d <= origin and d <= size-1-origin, count = 2
        # If d > origin and d <= size-1-origin, count = 1 (only on the side farther)
        # If d <= origin and d > size-1-origin, count = 1
        # If d == origin == size-1-origin then count=1
        left_count = self.origin + 1
        right_count = self.size - self.origin
        for d in range(self.max_dist + 1):
            count = 0
            # check if d in left part
            if d < left_count:
                count += 1
            # check if d in right part
            if d < right_count:
                count += 1
            # If origin at boundary (d=0), this counts double, fix:
            # Actually at d=0 only one position
            # Also when d=0= origin and size=1 count=1
            # So when d=0, count=1
            if d == 0:
                count = 1
            dist_count[d] = count
        self.dist_count = dist_count


class DimensionDistanceConvolver:
    def __init__(self, dim_dist_maps):
        self.dim_dist_maps = dim_dist_maps

    def convolve(self):
        # We have list of dict distance->count for each dimension
        # Combine them for sum of distances by convolution (since Manhattan distance sums distances over dims)
        # Initialize with first dim dist_count
        combined = self.dim_dist_maps[0]
        for dist_map in self.dim_dist_maps[1:]:
            combined = self._convolve_two(combined, dist_map)
        return combined

    @staticmethod
    def _convolve_two(dist_map1, dist_map2):
        # dist_map: dict dist -> count
        result = {}
        for d1, c1 in dist_map1.items():
            for d2, c2 in dist_map2.items():
                d = d1 + d2
                result[d] = result.get(d, 0) + c1 * c2
        return result


class CubeColoringEstimator:
    def __init__(self, X, Y, Z, A, B, C, N):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.A = A
        self.B = B
        self.C = C
        self.N = N
        # Initialize dimension objects
        self.dims = [
            Dimension(X, A),
            Dimension(Y, B),
            Dimension(Z, C)
        ]

    def estimate(self):
        # Compute distance distributions per dimension
        for dim in self.dims:
            dim.compute_distances()

        dimension_dist_maps = [dim.dist_count for dim in self.dims]
        convolver = DimensionDistanceConvolver(dimension_dist_maps)
        manhattan_dist_counts = convolver.convolve()

        # Distribute counts modulo N
        color_counts = [0] * self.N
        for dist, count in manhattan_dist_counts.items():
            idx = dist % self.N
            color_counts[idx] += count

        return color_counts


def main():
    import sys
    input_line = sys.stdin.readline().strip()
    X, Y, Z, A, B, C, N = map(int, input_line.split())
    estimator = CubeColoringEstimator(X, Y, Z, A, B, C, N)
    color_counts = estimator.estimate()
    print(" ".join(str(c) for c in color_counts))


if __name__ == '__main__':
    main()