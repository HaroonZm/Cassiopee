class Drill:
    def __init__(self, total_pages: int, max_daily: int):
        self.total_pages = total_pages
        self.max_daily = max_daily

    def required_days(self) -> int:
        # Calcul du nombre de jours nécessaires pour finir ce drill
        days = (self.total_pages + self.max_daily - 1) // self.max_daily
        return days


class HomeworkPlan:
    def __init__(self, days_off: int, drills: list[Drill]):
        self.days_off = days_off
        self.drills = drills

    def max_play_days(self) -> int:
        days_needed = max(drill.required_days() for drill in self.drills)
        return self.days_off - days_needed


class InputReader:
    @staticmethod
    def read() -> HomeworkPlan:
        L = int(input())
        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        drills = [
            Drill(A, C),
            Drill(B, D)
        ]
        return HomeworkPlan(L, drills)


class SolutionExecutor:
    def __init__(self, plan: HomeworkPlan):
        self.plan = plan

    def execute(self) -> None:
        print(self.plan.max_play_days())


if __name__ == "__main__":
    plan = InputReader.read()
    executor = SolutionExecutor(plan)
    executor.execute()