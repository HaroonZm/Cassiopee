class ElevationData:
    def __init__(self, elevations):
        self._elevations = elevations

    def max_elevation(self):
        return max(self._elevations) if self._elevations else 0.0

    def min_elevation(self):
        return min(self._elevations) if self._elevations else 0.0

    def elevation_difference(self):
        return self.max_elevation() - self.min_elevation()


class ElevationDataParser:
    @staticmethod
    def parse_from_stdin():
        elevations = []
        try:
            while True:
                line = input()
                if line.strip() == '':
                    break
                elevations.append(float(line.strip()))
        except EOFError:
            pass
        return ElevationData(elevations)


class ElevationDifferenceCalculator:
    def __init__(self, data: ElevationData):
        self.data = data

    def calculate(self):
        diff = self.data.elevation_difference()
        return round(diff, 4)


class ElevationDifferenceOutputter:
    @staticmethod
    def output(value):
        print(value)


class MountainElevationApp:
    def __init__(self):
        self.parser = ElevationDataParser()
        self.outputter = ElevationDifferenceOutputter()

    def run(self):
        data = self.parser.parse_from_stdin()
        calculator = ElevationDifferenceCalculator(data)
        difference = calculator.calculate()
        self.outputter.output(difference)


if __name__ == '__main__':
    app = MountainElevationApp()
    app.run()