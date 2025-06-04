import sys
import math

def main():
    input = sys.stdin.readline
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    # Convert points to vectors relative to the first point to simplify rotation and translation
    # Actually, it's not necessary here but we keep the original points as is.

    # The main difficulty of the problem is:
    # We have a polyline with n vertices, no self-intersection and no three points collinear.
    # We want to find if there exists a rigid transformation (translation + rotation)
    # that moves the entire polyline so that all points are strictly below the x-axis (y<0),
    # and the polyline passes through (0,0), the location of the tiny hole in the wall (y=0).

    # Important properties:
    # - We cannot deform the polyline: length of edges and angles between them are fixed.
    # - We can rotate around (0,0), and translate anywhere.
    # - The wall is at y=0, and the polyline must be entirely in y<0 after transformation.
    # - The polyline must pass through (0,0) after transformation, i.e., the transformed polyline must intersect the hole.

    # Approach:
    # Let's call the original polyline P = (p0, p1,..., p_{n-1}).
    # After transformation T = R(θ)+v (rotation + translation),
    # the image points are T(pi) = R(pi) + v.

    # Since the polyline must go through hole at (0,0),
    # there exists some index k such that T(p_k) = (0,0) (the point of the polyline at the hole).
    # So,
    # 0 = R(p_k) + v => v = - R(p_k)

    # Therefore, the transformation is T(p) = R(p) - R(p_k).

    # So the problem reduces to:
    # - For each vertex p_k as candidate to "cross the hole",
    # - Find a rotation R by angle θ such that all transformed points have y-coordinate < 0:
    #    y(T(p_i)) = y(R(p_i) - R(p_k)) = y(R(p_i)) - y(R(p_k)) < 0  for all i
    # Equivalently,
    #    y(R(p_i)) < y(R(p_k))  for all i != k
    # and
    #    y(R(p_k)) = y(R(p_k))

    # Since rotation by angle θ is:
    # R(p) = (x cosθ - y sinθ, x sinθ + y cosθ)
    # So y-coordinate of R(p) is: x sinθ + y cosθ

    # Set f_i(θ) = x_i sinθ + y_i cosθ
    # We want to find θ such that ∀ i≠k : f_i(θ) < f_k(θ)

    # Rearranged:
    # f_i(θ) - f_k(θ) < 0 for all i≠k

    # Define g_i(θ) = f_i(θ) - f_k(θ) = (x_i - x_k) sinθ + (y_i - y_k) cosθ < 0

    # So for each i≠k, need g_i(θ) < 0

    # For a fixed k, find θ in [0,2π) such that all g_i(θ)<0.

    # Note: to have g_i(θ) < 0 for all i≠k, the intersection of all intervals where g_i(θ)<0 must be non-empty.

    # Since each g_i(θ) = A_i sinθ + B_i cosθ < 0, where A_i = x_i - x_k, B_i = y_i - y_k.

    # The set S_i = {θ | A_i sinθ + B_i cosθ < 0} is an open half-circle defined by the linear form.

    # The "zero set" of g_i(θ) is where g_i(θ)=0:
    # A_i sinθ + B_i cosθ = 0
    # => tanθ = -B_i / A_i (handle A_i=0 separately)

    # The function g_i(θ) = 0 has two zero crossings in [0,2π), defining where g_i(θ)<0.
    # The set where g_i(θ)<0 is a half-circle (an open interval of length π) on the unit circle.

    # So for each i, the set of θ satisfying g_i(θ) < 0 is an open interval of length π on [0,2π).

    # Our task is to find an angle θ ∈ [0,2π) contained in all these intervals simultaneously.
    # That means we want the intersection of all these half-circles to be non-empty.

    # Algorithm:
    # For each k:
    #   For each i≠k, compute the half-circle interval where g_i(θ)<0.
    #   Represent intervals as [start, end) modulo 2π.
    #   Then find intersection over i of these intervals.
    #   If intersection is non-empty for some k, answer is "Possible".
    # Otherwise "Impossible".

    def half_circle_interval(a, b):
        # Returns the interval (start, end) in [0, 2pi)
        # where a sin t + b cos t < 0
        # Since a sin t + b cos t = 0 at two points separated by π
        # The interval where expression < 0 is the half-circle opposite the vector (b,a)
        # Because a sin t + b cos t = 0 when tan t = -b/a
        # Compute angle θ0 where a sin θ0 + b cos θ0 = 0:
        # rearranged: a sin θ0 = -b cos θ0 => tan θ0 = -b/a
        # Compute θ0:
        theta0 = math.atan2(-b, a)  # Because tan θ0 = -b/a => θ0 = atan2(-b,a)
        if theta0 < 0:
            theta0 += 2 * math.pi
        # The zeros are at θ0 and θ0 + π, and expression < 0 in (θ0, θ0+π)
        start = theta0
        end = (theta0 + math.pi) % (2 * math.pi)
        return start, end

    def interval_intersection(intervals):
        # Intervals are all half-circles: open intervals (start, end) modulo 2pi
        # The intersection of intervals can be empty or a smaller arc

        # Because intervals wrap around 2pi, handle wrap:
        # Split each interval into one or two intervals in [0, 2pi)
        # If start < end: interval is (start, end)
        # If start > end: interval wraps around 2pi, so intervals are (start, 2pi) and (0, end)

        # To find intersection of all intervals:
        # We try to find angle θ that lies in all intervals.

        # Strategy:
        # For all intervals, break wrapped intervals into two parts.
        # We then try all candidate intersection intervals by considering start and end points.

        # For efficiency, since intervals are half-circles of length π,
        # the intersection of all intervals is non-empty iff
        # there exists some θ that lies inside all.

        # Alternative approach:
        # Since intervals are half circles, intersection of all intervals is also a circular arc.
        # We can represent intervals as points on circle: points where expression changes sign.

        # Let's find candidate θ by considering all interval endpoints
        # and checking if θ in all intervals.

        points = []
        for start, end in intervals:
            if start < end:
                # One interval
                points.append( (start, +1) )
                points.append( (end, -1) )
            else:
                # Wrapped interval: two intervals
                # (start, 2pi) and (0, end)
                points.append( (start, +1) )
                points.append( (2*math.pi, -1) )
                points.append( (0, +1) )
                points.append( (end, -1) )

        # Sort points by angle
        points.sort()

        # We sweep angle from 0 to 2pi maintaining count of intervals covering
        # Initially coverage =0, when we pass +1 coverage +=1, at -1 coverage -=1
        coverage = 0
        max_coverage = 0
        candidates = []

        # For each event point, we check coverage coverage after applying event
        for i in range(len(points)*2):
            # Use modulo for wrap around
            idx = i % len(points)
            angle, delta = points[idx]
            coverage += delta
            if coverage == len(intervals):
                # Fully covered, save angle interval start
                start_angle = angle
                # We try to find end angle of this full coverage interval
                # by moving forward until coverage < len(intervals)
                j = (idx+1)%len(points)
                end_angle = None
                coverage2 = coverage
                while True:
                    angle2, delta2 = points[j]
                    coverage2 += delta2
                    if coverage2 < len(intervals):
                        end_angle = angle2
                        break
                    j = (j+1)%len(points)
                    if j == idx:
                        # full circle covered?
                        end_angle = angle
                        break
                if end_angle is None:
                    # No end found
                    end_angle = start_angle
                # We found an intersection interval: (start_angle, end_angle)
                # There is at least one angle in intersection
                candidates.append( (start_angle, end_angle) )
                break  # one interval is enough to find intersection
        if candidates:
            return True
        else:
            return False

    for k in range(n):
        intervals = []
        xk, yk = points[k]
        # Build intervals for all i != k
        for i in range(n):
            if i == k:
                continue
            xi, yi = points[i]
            a = xi - xk
            b = yi - yk
            # if a==0 and b==0:
            # points distinct, so shouldn't be equal
            start, end = half_circle_interval(a, b)
            intervals.append( (start, end) )
        
        if interval_intersection(intervals):
            print("Possible")
            return

    print("Impossible")


if __name__ == "__main__":
    main()