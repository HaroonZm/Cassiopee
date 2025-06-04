from collections import deque
import itertools as itertools_module
import sys
import math

sys.setrecursionlimit(10000000)

number_of_jobs = input()

list_of_jobs = []

for job_index in range(number_of_jobs):
    job_duration, job_deadline = map(int, raw_input().split())
    list_of_jobs.append((job_deadline, job_duration))

list_of_jobs.sort()

INFINITY_VALUE = 10 ** 18

min_total_time_for_jobs = [0] + [INFINITY_VALUE] * number_of_jobs

for job_deadline, job_duration in list_of_jobs:

    updated_total_time = list(min_total_time_for_jobs)

    for jobs_completed in range(1, number_of_jobs + 1):

        if min_total_time_for_jobs[jobs_completed - 1] + job_duration <= job_deadline:
            updated_total_time[jobs_completed] = min(
                min_total_time_for_jobs[jobs_completed],
                min_total_time_for_jobs[jobs_completed - 1] + job_duration
            )

    min_total_time_for_jobs = updated_total_time

for possible_completed_jobs in range(number_of_jobs + 1):
    if min_total_time_for_jobs[possible_completed_jobs] < INFINITY_VALUE:
        maximum_number_of_completed_jobs = possible_completed_jobs

print maximum_number_of_completed_jobs