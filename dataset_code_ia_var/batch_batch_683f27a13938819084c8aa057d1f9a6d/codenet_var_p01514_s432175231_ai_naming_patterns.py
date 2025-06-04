import sys
from collections import defaultdict

class ContestProcessor:
    def __init__(self):
        pass

    def process_input(self):
        while True:
            task_count, problem_count, report_count = map(int, raw_input().split())
            if task_count == 0 and problem_count == 0 and report_count == 0:
                break
            team_data_list = [[set(), defaultdict(int), 0, team_index + 1] for team_index in range(task_count)]
            for _ in range(report_count):
                team_id_str, problem_id_str, time_str, verdict = raw_input().split()
                team_id = int(team_id_str)
                problem_id = int(problem_id_str)
                submission_time = int(time_str)
                current_team_data = team_data_list[team_id - 1]
                solved_problems_set, wrong_submissions_map, total_time, team_identifier = current_team_data
                if problem_id in solved_problems_set:
                    continue
                if verdict == 'CORRECT':
                    solved_problems_set.add(problem_id)
                    total_time_penalty = wrong_submissions_map[problem_id] * 1200
                    current_team_data[2] += submission_time + total_time_penalty
                elif verdict == 'WRONG':
                    wrong_submissions_map[problem_id] += 1
            sorted_team_data = sorted(team_data_list, key=lambda x: (-len(x[0]), x[2]))
            for team_entry in sorted_team_data:
                team_number = team_entry[3]
                solved_count = len(team_entry[0])
                penalty_time = team_entry[2]
                print team_number, solved_count, penalty_time

if __name__ == '__main__':
    contest_processor = ContestProcessor()
    contest_processor.process_input()