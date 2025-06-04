class HorizonModel:
    def __init__(self, horizon_level=0):
        self.horizon_level = horizon_level

    def is_sunrise_or_sunset(self, sun):
        # The moment when sun's top (center + radius) is exactly on horizon
        return sun.center_height + sun.radius == self.horizon_level

    def is_daytime(self, sun):
        # Sun's top is above the horizon
        return sun.center_height + sun.radius > self.horizon_level

    def is_nighttime(self, sun):
        # Sun's top is below the horizon
        return sun.center_height + sun.radius < self.horizon_level


class CelestialBody:
    def __init__(self, center_height, radius):
        self.center_height = center_height
        self.radius = radius


class DaylightStatus:
    DAY = 1
    SUNRISE_OR_SUNSET = 0
    NIGHT = -1


class DaylightEvaluator:
    def __init__(self, horizon_model):
        self.horizon = horizon_model

    def evaluate(self, sun):
        if self.horizon.is_sunrise_or_sunset(sun):
            return DaylightStatus.SUNRISE_OR_SUNSET
        elif self.horizon.is_daytime(sun):
            return DaylightStatus.DAY
        else:
            return DaylightStatus.NIGHT


class InputParser:
    @staticmethod
    def parse(input_line):
        h_str, r_str = input_line.strip().split()
        return int(h_str), int(r_str)


class DaylightApp:
    def __init__(self):
        self.horizon = HorizonModel()
        self.evaluator = DaylightEvaluator(self.horizon)

    def run(self, input_line):
        h, r = InputParser.parse(input_line)
        sun = CelestialBody(center_height=h, radius=r)
        status = self.evaluator.evaluate(sun)
        print(status)


if __name__ == "__main__":
    import sys

    app = DaylightApp()
    input_line = sys.stdin.readline()
    app.run(input_line)