class CommitteeMember:
    def __init__(self, convenient_dates):
        self._convenient_dates = set(convenient_dates)

    def is_available_on(self, date):
        return date in self._convenient_dates

    @property
    def convenient_dates(self):
        return self._convenient_dates


class MeetingScheduler:
    def __init__(self, quorum, members):
        self._quorum = quorum
        self._members = members
        self._date_frequency = {}

    def _aggregate_date_frequencies(self):
        frequencies = {}
        for member in self._members:
            for date in member.convenient_dates:
                frequencies[date] = frequencies.get(date, 0) + 1
        self._date_frequency = frequencies

    def _find_best_date(self):
        # Filter dates that satisfy quorum
        valid_dates = [(date, count) for date, count in self._date_frequency.items() if count >= self._quorum]
        if not valid_dates:
            return 0
        # Find date with max count and earliest if tie
        valid_dates.sort(key=lambda x: (-x[1], x[0]))
        return valid_dates[0][0]

    def schedule(self):
        self._aggregate_date_frequencies()
        return self._find_best_date()


class InputParser:
    @staticmethod
    def parse_member_line(line):
        parts = list(map(int, line.split()))
        M = parts[0]
        convenient_dates = parts[1:] if M > 0 else []
        return CommitteeMember(convenient_dates)

    @staticmethod
    def parse_dataset(lines):
        n, q = map(int, lines[0].split())
        members = [InputParser.parse_member_line(lines[i+1]) for i in range(n)]
        return n, q, members


class ICPCMeetingCoordinator:
    def __init__(self):
        self._datasets = []

    def load_input(self, input_lines):
        idx = 0
        while idx < len(input_lines):
            line = input_lines[idx].strip()
            if line == '0 0':
                break
            n, q = map(int, line.split())
            dataset_lines = input_lines[idx:idx+n+1]
            self._datasets.append(dataset_lines)
            idx += n + 1
        return self

    def process(self):
        results = []
        for dataset_lines in self._datasets:
            n, q, members = InputParser.parse_dataset(dataset_lines)
            scheduler = MeetingScheduler(q, members)
            results.append(scheduler.schedule())
        return results


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    coordinator = ICPCMeetingCoordinator().load_input(input_lines)
    results = coordinator.process()
    for res in results:
        print(res)


if __name__ == '__main__':
    main()