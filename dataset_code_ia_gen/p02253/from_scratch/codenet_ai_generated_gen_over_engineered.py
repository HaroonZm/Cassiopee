from abc import ABC, abstractmethod
from typing import List, Tuple


class Activity:
    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return f"Activity(start={self.start}, finish={self.finish})"


class InputParser(ABC):
    @abstractmethod
    def parse(self) -> List[Activity]:
        pass


class StdInParser(InputParser):
    def parse(self) -> List[Activity]:
        n = int(input())
        activities = []
        for _ in range(n):
            s, f = map(int, input().split())
            activities.append(Activity(s, f))
        return activities


class ActivitySelector(ABC):
    @abstractmethod
    def select_activities(self, activities: List[Activity]) -> List[Activity]:
        pass


class GreedyActivitySelector(ActivitySelector):
    def select_activities(self, activities: List[Activity]) -> List[Activity]:
        # Sort activities by finish time ascending
        sorted_activities = sorted(activities, key=lambda x: x.finish)

        selected = []
        current_finish_time = -1
        for activity in sorted_activities:
            if activity.start >= current_finish_time:
                selected.append(activity)
                current_finish_time = activity.finish
        return selected


class ResultPresenter(ABC):
    @abstractmethod
    def present(self, selected_activities: List[Activity]):
        pass


class StdOutPresenter(ResultPresenter):
    def present(self, selected_activities: List[Activity]):
        print(len(selected_activities))


class ActivitySelectionApp:
    def __init__(self,
                 parser: InputParser,
                 selector: ActivitySelector,
                 presenter: ResultPresenter):
        self.parser = parser
        self.selector = selector
        self.presenter = presenter

    def run(self):
        activities = self.parser.parse()
        selected = self.selector.select_activities(activities)
        self.presenter.present(selected)


if __name__ == "__main__":
    app = ActivitySelectionApp(
        parser=StdInParser(),
        selector=GreedyActivitySelector(),
        presenter=StdOutPresenter()
    )
    app.run()