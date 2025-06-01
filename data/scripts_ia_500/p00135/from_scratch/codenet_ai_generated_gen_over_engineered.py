class Angle:
    def __init__(self, degrees: float):
        self.degrees = degrees % 360

    def difference(self, other: 'Angle') -> float:
        diff = abs(self.degrees - other.degrees) % 360
        return min(diff, 360 - diff)

    def __repr__(self):
        return f"Angle({self.degrees}°)"

class ClockHand:
    def get_angle(self) -> Angle:
        raise NotImplementedError()

class HourHand(ClockHand):
    def __init__(self, hour: int, minute: int):
        self.hour = hour % 12
        self.minute = minute

    def get_angle(self) -> Angle:
        # Hour hand moves 30° per hour + 0.5° per minute
        degrees = (self.hour * 30) + (self.minute * 0.5)
        return Angle(degrees)

class MinuteHand(ClockHand):
    def __init__(self, minute: int):
        self.minute = minute

    def get_angle(self) -> Angle:
        # Minute hand moves 6° per minute
        degrees = self.minute * 6
        return Angle(degrees)

class Time:
    def __init__(self, hh: int, mm: int):
        self.hh = hh
        self.mm = mm

    @classmethod
    def from_string(cls, time_str: str) -> 'Time':
        hh_str, mm_str = time_str.strip().split(":")
        return cls(int(hh_str), int(mm_str))

    def hour_hand(self) -> HourHand:
        return HourHand(self.hh, self.mm)

    def minute_hand(self) -> MinuteHand:
        return MinuteHand(self.mm)

class AlertLevel:
    ALERT = "alert"
    SAFE = "safe"
    WARNING = "warning"

class ClockAlertJudger:
    def __init__(self, time: Time):
        self.time = time
        self.hour_hand = time.hour_hand()
        self.minute_hand = time.minute_hand()

    def judge(self) -> str:
        angle_hour = self.hour_hand.get_angle()
        angle_minute = self.minute_hand.get_angle()
        diff = angle_hour.difference(angle_minute)
        if 0 <= diff < 30:
            return AlertLevel.ALERT
        elif 90 <= diff <= 180:
            return AlertLevel.SAFE
        else:
            return AlertLevel.WARNING

class InputHandler:
    def __init__(self, n: int, time_strings: list[str]):
        self.n = n
        self.time_strings = time_strings

    def parse_times(self) -> list[Time]:
        return [Time.from_string(t) for t in self.time_strings]

class OutputHandler:
    def output_results(self, results: list[str]):
        for r in results:
            print(r)

class ClockAlertSystem:
    def __init__(self, n: int, time_strings: list[str]):
        self.input_handler = InputHandler(n, time_strings)
        self.output_handler = OutputHandler()

    def process(self):
        times = self.input_handler.parse_times()
        results = []
        for time in times:
            judger = ClockAlertJudger(time)
            results.append(judger.judge())
        self.output_handler.output_results(results)

def main():
    n = int(input())
    time_strings = [input() for _ in range(n)]
    system = ClockAlertSystem(n, time_strings)
    system.process()

if __name__ == "__main__":
    main()