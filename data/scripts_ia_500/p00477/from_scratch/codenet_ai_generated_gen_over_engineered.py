class TimeInterval:
    def __init__(self, seconds: int):
        if seconds < 0:
            raise ValueError("TimeInterval cannot be negative")
        self._seconds = seconds

    @property
    def seconds(self) -> int:
        return self._seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            return NotImplemented
        return TimeInterval(self._seconds + other._seconds)

    def __repr__(self):
        return f"TimeInterval({self._seconds}s)"


class JourneySegment:
    def __init__(self, start: str, destination: str, duration: TimeInterval):
        self.start = start
        self.destination = destination
        self.duration = duration

    def __repr__(self):
        return f"JourneySegment({self.start} -> {self.destination}, {self.duration})"


class Journey:
    def __init__(self, segments: list[JourneySegment]):
        if not segments:
            raise ValueError("Journey must have at least one segment")
        self.segments = segments

    def total_duration(self) -> TimeInterval:
        total = TimeInterval(0)
        for segment in self.segments:
            total += segment.duration
        return total


class TimeConverter:
    @staticmethod
    def seconds_to_minutes_seconds(total_seconds: int) -> tuple[int, int]:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return minutes, seconds


class InputReader:
    def read_durations(self) -> list[int]:
        durations = []
        for _ in range(4):
            line = input()
            line = line.strip()
            if not line.isdigit():
                raise ValueError("Input must be a positive integer")
            durations.append(int(line))
        return durations


class OutputWriter:
    def write_minutes_seconds(self, minutes: int, seconds: int) -> None:
        print(minutes)
        print(seconds)


class TotalTimeCalculator:
    def __init__(self):
        self.input_reader = InputReader()
        self.output_writer = OutputWriter()

    def run(self):
        durations = self.input_reader.read_durations()

        names = ["家", "1つ目の店", "2つ目の店", "3つ目の店", "家"]
        segments = []
        for i in range(4):
            duration = TimeInterval(durations[i])
            segment = JourneySegment(names[i], names[i + 1], duration)
            segments.append(segment)

        journey = Journey(segments)
        total_duration = journey.total_duration()
        minutes, seconds = TimeConverter.seconds_to_minutes_seconds(total_duration.seconds)

        self.output_writer.write_minutes_seconds(minutes, seconds)


if __name__ == "__main__":
    TotalTimeCalculator().run()