import sys
from sys import stdin
from collections import defaultdict

input = stdin.readline

def count_age_groups_using_dict(arguments):

    while True:

        number_of_visitors = int(input())

        if number_of_visitors == 0:
            break

        age_group_counts = defaultdict(int)

        for _ in range(number_of_visitors):

            visitor_age = int(input())

            if visitor_age < 10:
                age_group_counts['under_10'] += 1
            elif visitor_age < 20:
                age_group_counts['10s'] += 1
            elif visitor_age < 30:
                age_group_counts['20s'] += 1
            elif visitor_age < 40:
                age_group_counts['30s'] += 1
            elif visitor_age < 50:
                age_group_counts['40s'] += 1
            elif visitor_age < 60:
                age_group_counts['50s'] += 1
            else:
                age_group_counts['60_and_over'] += 1

        print(age_group_counts['under_10'])
        print(age_group_counts['10s'])
        print(age_group_counts['20s'])
        print(age_group_counts['30s'])
        print(age_group_counts['40s'])
        print(age_group_counts['50s'])
        print(age_group_counts['60_and_over'])


def count_age_groups_using_list(arguments):

    while True:

        number_of_visitors = int(input())

        if number_of_visitors == 0:
            break

        age_group_counters = [0] * 13  # Indices 0 to 12 to cover all decades

        for _ in range(number_of_visitors):

            visitor_age = int(input())

            decade_index = visitor_age // 10

            age_group_counters[decade_index] += 1

        print(age_group_counters[0])  # Under 10
        print(age_group_counters[1])  # Teens (10-19)
        print(age_group_counters[2])  # 20s
        print(age_group_counters[3])  # 30s
        print(age_group_counters[4])  # 40s
        print(age_group_counters[5])  # 50s
        print(sum(age_group_counters[6:]))  # 60 and over


if __name__ == '__main__':

    count_age_groups_using_list(sys.argv[1:])