class Dataset:
    def __init__(self, planets):
        self.planets = planets

    def max_hourly_volume(self):
        max_volume = 0
        for planet in self.planets:
            max_volume = max(max_volume, planet.max_access_volume())
        return max_volume


class Planet:
    def __init__(self, day_length, current_time, hourly_volumes):
        self.day_length = day_length
        self.current_time = current_time
        self.hourly_volumes = hourly_volumes

    def max_access_volume(self):
        # As volumes are one per hour, just return the max volume in the cycle
        return max(self.hourly_volumes)


class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        while True:
            line = input()
            if line == '0':
                break
            N = int(line)
            planets = []
            for _ in range(N):
                parts = input().split()
                d = int(parts[0])
                t = int(parts[1])
                q = list(map(int, parts[2:] ))
                planets.append(Planet(d, t, q))
            self.datasets.append(Dataset(planets))


class GalaxyWideWebService:
    def __init__(self):
        self.parser = InputParser()

    def run(self):
        self.parser.parse()
        for dataset in self.parser.datasets:
            print(dataset.max_hourly_volume())


if __name__ == '__main__':
    service = GalaxyWideWebService()
    service.run()