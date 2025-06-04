class PastaType:
    TOMATO = 1
    CREAM = 2
    BASIL = 3
    ALL = (TOMATO, CREAM, BASIL)

class PastaPlanConstraints:
    MODULO = 10000
    MAX_CONSECUTIVE = 2

class PastaSchedule:
    def __init__(self, total_days):
        self.total_days = total_days
        # fixed_days_map: day (1-based) -> PastaType
        self.fixed_days_map = {}

    def add_fixed_day(self, day, pasta_type):
        if day < 1 or day > self.total_days:
            raise ValueError("Day out of schedule range")
        self.fixed_days_map[day] = pasta_type

    def is_fixed(self, day):
        return day in self.fixed_days_map

    def fixed_type(self, day):
        return self.fixed_days_map[day]

class PastaPlanner:
    def __init__(self, schedule: PastaSchedule):
        self.schedule = schedule
        self.N = schedule.total_days
        self.memo = {}

    def iter_possible_types(self, day):
        if self.schedule.is_fixed(day):
            yield self.schedule.fixed_type(day)
        else:
            for ptype in PastaType.ALL:
                yield ptype

    def count_schedules(self):
        # State: (day, last_type, consecutive_count)
        # last_type: last pasta type chosen (1,2,3), or 0 for none before day 1
        # consecutive_count: how many days consecutively last_type was chosen
        def dfs(day, last_type, cons_count):
            if day > self.N:
                return 1  # Valid complete schedule

            state = (day, last_type, cons_count)
            if state in self.memo:
                return self.memo[state]

            total_ways = 0
            for next_type in self.iter_possible_types(day):
                # Check no 3+ consecutive
                if next_type == last_type and cons_count == PastaPlanConstraints.MAX_CONSECUTIVE:
                    continue

                next_cons_count = cons_count + 1 if next_type == last_type else 1
                total_ways += dfs(day + 1, next_type, next_cons_count)

            total_ways %= PastaPlanConstraints.MODULO
            self.memo[state] = total_ways
            return total_ways

        return dfs(1, 0, 0)

class PastaInputParser:
    def __init__(self, raw_input_lines):
        self.raw_input_lines = raw_input_lines

    def parse(self):
        header = self.raw_input_lines[0].strip().split()
        N, K = map(int, header)
        schedule = PastaSchedule(N)
        for i in range(1, K+1):
            day_str, type_str = self.raw_input_lines[i].strip().split()
            day = int(day_str)
            ptype = int(type_str)
            schedule.add_fixed_day(day, ptype)
        return schedule

def main():
    import sys
    raw_input = sys.stdin.read().strip().split('\n')
    parser = PastaInputParser(raw_input)
    schedule = parser.parse()
    planner = PastaPlanner(schedule)
    answer = planner.count_schedules()
    print(answer)

if __name__ == "__main__":
    main()