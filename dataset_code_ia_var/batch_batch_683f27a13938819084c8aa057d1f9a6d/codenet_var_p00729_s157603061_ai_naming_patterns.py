import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class SolutionManager(object):

    def __init__(self):
        pass

    def process(self):
        while True:
            num_resources, num_intervals = map(int, raw_input().split())
            if num_resources == 0 and num_intervals == 0:
                break
            interval_activity = [[0] * 2000 for _ in range(num_intervals + 1)]
            num_events = input()
            for _ in range(num_events):
                event_time, resource_id, interval_id, event_type = map(int, raw_input().split())
                if event_type == 1:
                    interval_activity[interval_id][event_time] += 1
                else:
                    interval_activity[interval_id][event_time] -= 1
            for interval_index in range(1, num_intervals + 1):
                for time_point in range(540, 1261):
                    interval_activity[interval_index][time_point] += interval_activity[interval_index][time_point - 1]
            num_queries = input()
            for _ in range(num_queries):
                query_start, query_end, query_interval = map(int, raw_input().split())
                total_active = 0
                for time_point in range(query_start, query_end):
                    if interval_activity[query_interval][time_point] >= 1:
                        total_active += 1
                print total_active
        return None

if __name__ == '__main__':
    solution_manager = SolutionManager()
    solution_manager.process()