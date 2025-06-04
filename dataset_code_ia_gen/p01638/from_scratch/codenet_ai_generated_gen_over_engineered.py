import math
from typing import List, Tuple

class PieChart:
    def __init__(self, radius: int, center_x: int, center_y: int, ratios: List[int]):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.ratios = ratios
        self.total_ratio = sum(ratios)
        self.angles = self._compute_angles()
        self.original_area = math.pi * radius * radius

    def _compute_angles(self) -> List[Tuple[float, float]]:
        """Compute start and end angles (in radians) for each segment clockwise starting at (0,r)."""
        # Starting angle corresponds to the vector pointing "up": (0, r) from origin
        # This corresponds to angle pi/2 in standard coordinate system.
        start_angle = math.pi / 2
        angles = []
        current_angle = start_angle
        for ratio in self.ratios:
            sweep = 2 * math.pi * (ratio / self.total_ratio)
            angles.append((current_angle, current_angle - sweep))
            current_angle -= sweep
        return angles

    def _sector_area(self, r: float, theta_start: float, theta_end: float) -> float:
        """Compute sector area for angles theta_start to theta_end (clockwise)."""
        angle = (theta_start - theta_end) % (2 * math.pi)
        return 0.5 * r * r * angle

    def _shifted_sector_area(self, theta_start: float, theta_end: float) -> float:
        """
        Calculate area of the shifted segment.
        Area = integral over angles of 0.5 * d^2 dtheta, where d is distance from
        shifted center to circumference point at angle theta.

        d(theta) = sqrt( (r*cos(theta))^2 + (r*sin(theta))^2 + x^2 + y^2 - 2r(x cos(theta) + y sin(theta)) )
                 = sqrt(r^2 + x^2 + y^2 - 2r(x cos(theta) + y sin(theta)))
        """
        steps = 1024  # sufficiently large number for precision
        delta_theta = ((theta_start - theta_end) % (2*math.pi)) / steps
        area = 0.0
        for i in range(steps):
            # Midpoint of theta interval to apply midpoint integration
            theta = (theta_start - (i + 0.5) * delta_theta) % (2 * math.pi)
            dx = self.radius * math.cos(theta) - self.center_x
            dy = self.radius * math.sin(theta) - self.center_y
            dist = math.hypot(dx, dy)
            # Sector area element: 0.5 * dist^2 * dtheta
            area += 0.5 * dist * dist * delta_theta
        return area

    def area_change_percentages(self) -> List[int]:
        result = []
        for start_ang, end_ang in self.angles:
            original_area = self._sector_area(self.radius, start_ang, end_ang)
            new_area = self._shifted_sector_area(start_ang, end_ang)
            percent = int((new_area / original_area) * 100)
            result.append(percent)
        return result


class PieChartFactory:
    @staticmethod
    def from_input() -> 'PieChart':
        r, x, y, n = map(int, input().split())
        ratios = list(map(int, input().split()))
        return PieChart(r, x, y, ratios)


def main():
    pie_chart = PieChartFactory.from_input()
    changes = pie_chart.area_change_percentages()
    print(' '.join(map(str, changes)))


if __name__ == '__main__':
    main()