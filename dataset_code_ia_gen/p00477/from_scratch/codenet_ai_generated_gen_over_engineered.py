class TimeInterval:
    def __init__(self, seconds: int):
        if seconds < 0:
            raise ValueError("TimeInterval cannot be negative.")
        self.seconds = seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            return NotImplemented
        return TimeInterval(self.seconds + other.seconds)

    def to_minutes_seconds(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return minutes, seconds

class JourneySegment:
    def __init__(self, start_location: str, end_location: str, duration: TimeInterval):
        self.start_location = start_location
        self.end_location = end_location
        self.duration = duration

class Route:
    def __init__(self, segments: list):
        self.segments = segments

    def total_duration(self) -> TimeInterval:
        total = TimeInterval(0)
        for segment in self.segments:
            total += segment.duration
        return total

class TimeInputProvider:
    def __init__(self, num_segments: int):
        self.num_segments = num_segments

    def read_times(self) -> list:
        times = []
        for _ in range(self.num_segments):
            line = input()
            value = int(line.strip())
            times.append(TimeInterval(value))
        return times

class JourneyManager:
    LOCATIONS = ["House", "Shop1", "Shop2", "Shop3", "House"]

    def __init__(self, time_intervals: list):
        # There must be 4 intervals for the route: House -> Shop1, Shop1 -> Shop2, Shop2 -> Shop3, Shop3 -> House
        if len(time_intervals) != 4:
            raise ValueError("There must be exactly 4 time intervals.")
        self.segments = []
        for i in range(4):
            segment = JourneySegment(
                start_location=self.LOCATIONS[i],
                end_location=self.LOCATIONS[i+1],
                duration=time_intervals[i]
            )
            self.segments.append(segment)
        self.route = Route(self.segments)

    def get_total_time_minutes_seconds(self):
        total_duration = self.route.total_duration()
        return total_duration.to_minutes_seconds()

def main():
    provider = TimeInputProvider(num_segments=4)
    intervals = provider.read_times()
    manager = JourneyManager(intervals)
    minutes, seconds = manager.get_total_time_minutes_seconds()
    print(minutes)
    print(seconds)

if __name__ == "__main__":
    main()