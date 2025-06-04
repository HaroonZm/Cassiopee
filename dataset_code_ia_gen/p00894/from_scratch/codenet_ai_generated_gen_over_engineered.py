from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple


@dataclass(frozen=True, order=True)
class DateTime:
    month: int
    day: int
    hour: int
    minute: int

    @staticmethod
    def from_string(date_str: str, time_str: str) -> 'DateTime':
        # date_str example: "04/21"
        # time_str example: "09:00"

        month, day = map(int, date_str.split('/'))
        hour, minute = map(int, time_str.split(':'))
        return DateTime(month, day, hour, minute)

    def to_minutes(self) -> int:
        # convert date and time to total minutes (from start of year)
        # assuming no leap year consideration, just days in months for simplicity
        # number of days in each month (non-leap)
        days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
        total_days = sum(days_in_months[:self.month - 1]) + (self.day - 1)  # zero based days
        return total_days * 24 * 60 + self.hour * 60 + self.minute

    def __sub__(self, other: 'DateTime') -> int:
        # get difference in minutes
        return self.to_minutes() - other.to_minutes()


class Visitor(ABC):
    def __init__(self, visitor_id: str):
        self.visitor_id = visitor_id

    @abstractmethod
    def is_goddess(self) -> bool:
        pass


class Programmer(Visitor):
    def __init__(self, visitor_id: str):
        super().__init__(visitor_id)
        self._sessions: List[Tuple[DateTime, DateTime]] = []

    def is_goddess(self) -> bool:
        return False

    def add_session(self, enter: DateTime, exit: DateTime):
        self._sessions.append((enter, exit))

    @property
    def sessions(self) -> List[Tuple[DateTime, DateTime]]:
        return self._sessions


class Goddess(Visitor):
    def __init__(self):
        super().__init__("000")
        self._sessions: List[Tuple[DateTime, DateTime]] = []

    def is_goddess(self) -> bool:
        return True

    def add_session(self, enter: DateTime, exit: DateTime):
        self._sessions.append((enter, exit))

    @property
    def sessions(self) -> List[Tuple[DateTime, DateTime]]:
        return self._sessions


class LogEntry:
    def __init__(self, date_str: str, time_str: str, e_type: str, visitor_id: str):
        self.datetime = DateTime.from_string(date_str, time_str)
        self.event_type = e_type  # 'I' or 'O'
        self.visitor_id = visitor_id

    def __repr__(self):
        return f"<LogEntry {self.visitor_id} {self.event_type} {self.datetime}>"


class AltarLogParser:
    def __init__(self):
        pass

    def parse_dataset(self, lines: List[str]) -> List[LogEntry]:
        # lines contains n lines of the log except the first line with n count
        entries = []
        for line in lines:
            date_str = line[0:5]
            time_str = line[6:11]
            e_type = line[12]
            visitor_id = line[14:17]
            entry = LogEntry(date_str, time_str, e_type, visitor_id)
            entries.append(entry)
        return entries


class SessionBuilder:
    """
    Build sessions (enter-exit pairs) from a sequence of LogEntries for all visitors.
    """
    def __init__(self, log_entries: List[LogEntry]):
        self.log_entries = log_entries
        self.visitors: Dict[str, Visitor] = {}
        self._active_visitors: Dict[str, DateTime] = {}

    def _get_or_create_visitor(self, visitor_id: str) -> Visitor:
        if visitor_id not in self.visitors:
            if visitor_id == "000":
                self.visitors[visitor_id] = Goddess()
            else:
                self.visitors[visitor_id] = Programmer(visitor_id)
        return self.visitors[visitor_id]

    def build_sessions(self):
        # The altar is emptied at midnight (00:00).
        # Since all times in the input are between 00:01 and 23:59, we don't get midnight events.
        # So we separate sessions by this emptying.
        # We'll track active visitors during the same day and cut at the day change.

        # But since input is sorted ascending by date/time, we can detect day changes.
        last_date = None
        self._active_visitors = {}

        for entry in self.log_entries:
            current_date = (entry.datetime.month, entry.datetime.day)
            if last_date is not None and current_date != last_date:
                # New day/fresh altar: close all active sessions at midnight (the altar closes at 00:00)
                self._close_all_active_sessions_at_midnight(last_date)
                self._active_visitors.clear()
            last_date = current_date

            if entry.event_type == 'I':
                # Visitor comes in
                if entry.visitor_id in self._active_visitors:
                    # Defensive check: entering again without exit? Ignore or reset? 
                    # The problem statement doesn't mention inconsistent data.
                    # We'll ignore such anomaly.
                    pass
                else:
                    self._active_visitors[entry.visitor_id] = entry.datetime
            else:
                # Visitor goes out
                if entry.visitor_id in self._active_visitors:
                    enter_time = self._active_visitors.pop(entry.visitor_id)
                    visitor = self._get_or_create_visitor(entry.visitor_id)
                    visitor.add_session(enter_time, entry.datetime)
                else:
                    # Defensive: Exit without entrance? Ignore.
                    pass

        # after all entries closed, close remaining active sessions at 23:59 same day.
        # But problem states altar closes at midnight so no entries at 00:00 - so this may not be needed.
        self._close_all_active_sessions_at_midnight(last_date)
        self._active_visitors.clear()

    def _close_all_active_sessions_at_midnight(self, date_tuple: Optional[Tuple[int, int]]):
        # For all active visitors, close their session at 00:00 of that day (which is previous day actually)
        # Since no event at 00:00, we consider sessions end at 00:00 next day, which means 00:00 of current date.
        if date_tuple is None:
            return
        month, day = date_tuple
        # midnight at start of day => 00:00 current date, but we don't have that in input.
        # For all active sessions that didn't exit, we close at 00:00 (start of this date).
        # But that means their session ends at DateTime(month, day, 0, 0), which is before any event (minimum time 00:01)
        # So session length is zero or negative, so ignore these sessions.
        # According to problem statement, "the altar is emptied at midnight"
        # and times in input are between 00:01 and 23:59 inclusive
        # So if user entered and didn't exit at the end of day, their session effectively ends at 00:00 (no minutes)
        # So nothing to add.
        # We just discard these open sessions because altar closes at midnight.
        # So no action needed to add sessions here.
        pass


class PresenceIntervalCalculator:
    """
    Calculate intervals when the goddess was present from her sessions.
    """
    def __init__(self, goddess: Goddess):
        self.goddess = goddess

    def get_presence_intervals(self) -> List[Tuple[int, int]]:
        # Returns a list of time intervals in minutes since year's start where goddess was present
        # intervals will be normalized and merged if overlap
        sessions_minutes = []
        for enter, exit in self.goddess.sessions:
            start = enter.to_minutes()
            end = exit.to_minutes()
            sessions_minutes.append((start, end))

        merged = self._merge_intervals(sessions_minutes)
        return merged

    def _merge_intervals(self, intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # overlap or adjacent
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged


class BlessedTimeCalculator:
    """
    Calculates the blessed time of a programmer given presence intervals of goddess.
    """
    def __init__(self, presence_intervals: List[Tuple[int, int]]):
        self.presence_intervals = presence_intervals

    def calculate_blessed_time(self, programmer: Programmer) -> int:
        total = 0
        presence = self.presence_intervals
        for enter, exit in programmer.sessions:
            start = enter.to_minutes()
            end = exit.to_minutes()
            if end < start:
                # Defensive, should not happen
                continue
            # For each session, sum intersection with goddess presence intervals
            total += self._sum_intersection(start, end, presence)
        return total

    def _sum_intersection(self, start: int, end: int, intervals: List[Tuple[int, int]]) -> int:
        total = 0
        for p_start, p_end in intervals:
            if p_end <= start:
                continue
            if p_start >= end:
                break
            # calculate intersection
            inter_start = max(start, p_start)
            inter_end = min(end, p_end)
            if inter_end > inter_start:
                total += inter_end - inter_start
        return total


class GiftFromGoddessSolver:
    def __init__(self):
        self.parser = AltarLogParser()

    def solve(self) -> None:
        while True:
            n_line = input().strip()
            if n_line == '0':
                break
            n = int(n_line)
            lines = [input() for _ in range(n)]
            log_entries = self.parser.parse_dataset(lines)
            sessions_builder = SessionBuilder(log_entries)
            sessions_builder.build_sessions()

            goddess = sessions_builder.visitors.get("000", Goddess())
            presence_calculator = PresenceIntervalCalculator(goddess)
            presence_intervals = presence_calculator.get_presence_intervals()

            blessed_calculator = BlessedTimeCalculator(presence_intervals)

            max_blessed = 0
            for vid, visitor in sessions_builder.visitors.items():
                if visitor.is_goddess():
                    continue
                blessed_time = blessed_calculator.calculate_blessed_time(visitor)
                if blessed_time > max_blessed:
                    max_blessed = blessed_time

            print(max_blessed)


if __name__ == "__main__":
    GiftFromGoddessSolver().solve()