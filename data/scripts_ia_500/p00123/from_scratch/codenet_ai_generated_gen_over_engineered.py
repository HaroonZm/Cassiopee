class Distance:
    def __init__(self, meters: int):
        self.meters = meters

class TimeThreshold:
    def __init__(self, minutes: int, seconds: float):
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self) -> float:
        return self.minutes * 60 + self.seconds

class BadgeRequirement:
    def __init__(self, distance: Distance, max_time: TimeThreshold):
        self.distance = distance
        self.max_time = max_time

    def is_passed(self, time: float) -> bool:
        return time < self.max_time.total_seconds()

class BadgeLevel:
    def __init__(self, name: str, requirements: list[BadgeRequirement]):
        self.name = name
        self.requirements = requirements

    def is_achieved(self, t_500: float, t_1000: float) -> bool:
        # Check the proper time for each distance
        times = {500: t_500, 1000: t_1000}
        return all(req.is_passed(times[req.distance.meters]) for req in self.requirements)

class BadgeTest:
    def __init__(self, levels: list[BadgeLevel]):
        # Levels should be sorted from highest to lowest rank
        self.levels = levels

    def judge(self, t_500: float, t_1000: float) -> str:
        for level in self.levels:
            if level.is_achieved(t_500, t_1000):
                return level.name
        return "NA"

def build_badge_test() -> BadgeTest:
    # Defining distances
    dist_500 = Distance(500)
    dist_1000 = Distance(1000)

    # Define all badge levels with their time thresholds
    levels = [
        BadgeLevel("AAA", [
            BadgeRequirement(dist_500, TimeThreshold(0, 35.50)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 11.00))
        ]),
        BadgeLevel("AA", [
            BadgeRequirement(dist_500, TimeThreshold(0, 37.50)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 17.00))
        ]),
        BadgeLevel("A", [
            BadgeRequirement(dist_500, TimeThreshold(0, 40.00)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 23.00))
        ]),
        BadgeLevel("B", [
            BadgeRequirement(dist_500, TimeThreshold(0, 43.00)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 29.00))
        ]),
        BadgeLevel("C", [
            BadgeRequirement(dist_500, TimeThreshold(0, 50.00)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 45.00))
        ]),
        BadgeLevel("D", [
            BadgeRequirement(dist_500, TimeThreshold(0, 55.00)),
            BadgeRequirement(dist_1000, TimeThreshold(1, 56.00))
        ]),
        BadgeLevel("E", [
            BadgeRequirement(dist_500, TimeThreshold(1, 10.00)),
            BadgeRequirement(dist_1000, TimeThreshold(2, 28.00))
        ])
    ]
    return BadgeTest(levels)

def main():
    import sys
    badge_test = build_badge_test()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        t500_str, t1000_str = line.split()
        t500 = float(t500_str)
        t1000 = float(t1000_str)
        result = badge_test.judge(t500, t1000)
        print(result)

if __name__ == "__main__":
    main()