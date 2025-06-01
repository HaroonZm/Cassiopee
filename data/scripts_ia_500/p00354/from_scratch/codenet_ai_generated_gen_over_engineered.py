class DayOfWeekMapper:
    def __init__(self, reference_day: int, reference_day_name: str, days_in_month: int):
        self.days_in_month = days_in_month
        self.days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.reference_day = reference_day
        self.reference_day_index = self._day_name_to_index(reference_day_name)
    
    def _day_name_to_index(self, day_name: str) -> int:
        if day_name not in self.days:
            raise ValueError(f"Invalid day name: {day_name}")
        return self.days.index(day_name)
    
    def _normalize_day(self, day: int) -> int:
        if not (1 <= day <= self.days_in_month):
            raise ValueError(f"Day {day} is not within 1 and {self.days_in_month}")
        return day
    
    def day_for_date(self, day: int) -> str:
        normalized_day = self._normalize_day(day)
        # Calculate days difference from reference
        diff = normalized_day - self.reference_day
        # Compute day index with modular arithmetic
        target_index = (self.reference_day_index + diff) % len(self.days)
        return self.days[target_index]

class September2017DayOfWeekService:
    def __init__(self):
        # Given in the problem statement: 9 Sep 2017 is Saturday
        self.month_mapper = DayOfWeekMapper(reference_day=9, reference_day_name="sat", days_in_month=30)
    
    def get_weekday(self, day: int) -> str:
        return self.month_mapper.day_for_date(day)

class InputHandler:
    def __init__(self, service: September2017DayOfWeekService):
        self.service = service
    
    def read_input(self) -> int:
        try:
            raw_input = input()
            day = int(raw_input.strip())
            return day
        except Exception as e:
            raise ValueError(f"Invalid input for day: {e}")
    
    def output_day(self, day_name: str):
        print(day_name)

def main():
    service = September2017DayOfWeekService()
    input_handler = InputHandler(service)
    day = input_handler.read_input()
    day_name = service.get_weekday(day)
    input_handler.output_day(day_name)

if __name__ == "__main__":
    main()